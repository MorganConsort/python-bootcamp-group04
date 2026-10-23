"""Student-owned regression tests; instructor tests remain unchanged."""

import importlib
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TODAY = date(2026, 10, 26)


def module(name):
    return importlib.import_module(f"members.minh_vg.w2.{name}")


def test_task_dates_and_bounds():
    task = module("models").Task("Exam", 5, 6.0, date(2026, 10, 30))
    assert task.days_left(TODAY) == 4
    assert task.days_left(task.deadline) == 0
    assert task.days_left(date(2026, 11, 1)) == 0
    for importance in (0, 6):
        with pytest.raises(ValueError):
            module("models").Task("Exam", importance, 1, TODAY)


@pytest.mark.parametrize("effort", [-1, float("nan"), float("inf")])
def test_task_rejects_invalid_effort(effort):
    with pytest.raises(ValueError):
        module("models").Task("Exam", 1, effort, TODAY)


def test_csv_json_roundtrip(tmp_path):
    io = module("io_utils")
    tasks = io.load_tasks(ROOT / "samples/tasks.csv")
    assert [t.title for t in tasks] == ["DS exam", "Assignment"]
    assert tasks[0].deadline == date(2026, 10, 30)
    out = tmp_path / "plan.json"
    io.save_json(tasks, out)
    assert json.loads(out.read_text(encoding="utf-8")) == [
        {"title": "DS exam", "importance": 5, "effort_h": 6.0, "deadline": "2026-10-30"},
        {"title": "Assignment", "importance": 4, "effort_h": 1.5, "deadline": "2026-10-27"},
    ]
    io.save_json([], out)
    assert json.loads(out.read_text(encoding="utf-8")) == []


@pytest.mark.parametrize(
    "row",
    [
        "bad,9,1,2026-10-30",
        "bad,3,no,2026-10-30",
        "bad,3,1,no-date",
        "bad,3,1",
        "bad,3,1,2026-10-30,extra",
        ",3,1,2026-10-30",
        "bad,3,nan,2026-10-30",
        '"unterminated,3,1,2026-10-30',
    ],
)
def test_bad_csv_reports_line(tmp_path, row):
    source = tmp_path / "bad.csv"
    source.write_text(
        "title,importance,effort_h,deadline\nOK,3,1,2026-10-30\n" + row, encoding="utf-8"
    )
    with pytest.raises(ValueError, match="line 3"):
        module("io_utils").load_tasks(source)


def test_csv_headers_unicode_and_quoted_title(tmp_path):
    source = tmp_path / "tasks.csv"
    for text in ("", "wrong,header\n"):
        source.write_text(text, encoding="utf-8")
        with pytest.raises(ValueError, match="line 1"):
            module("io_utils").load_tasks(source)
    source.write_text(
        'title,importance,effort_h,deadline\n"Ôn, Python",1,0,2026-10-30\n', encoding="utf-8"
    )
    assert module("io_utils").load_tasks(source)[0].title == "Ôn, Python"
    source.write_text("title,importance,effort_h,deadline\n", encoding="utf-8")
    assert module("io_utils").load_tasks(source) == []


def test_feasibility_exception():
    errors = module("errors")
    tasks = [module("models").Task("Exam", 3, 6, TODAY), module("models").Task("HW", 3, 4, TODAY)]
    with pytest.raises(errors.InfeasiblePlan) as exc:
        errors.check_feasible(tasks, 2)
    assert (exc.value.needed_h, exc.value.available_h) == (10, 2)
    assert "10" in str(exc.value) and "2" in str(exc.value)
    assert errors.check_feasible(tasks, 10) is None
    assert errors.check_feasible([], 0) is None
    for hours in (-1, float("nan"), float("inf")):
        with pytest.raises(ValueError):
            errors.check_feasible(tasks, hours)


def test_package_runs_from_repo_root():
    run = subprocess.run(
        [sys.executable, "-m", "members.minh_vg.w2"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert run.returncode == 0, run.stderr
    assert "DS exam" in run.stdout and "Assignment" in run.stdout
    assert "2026-10-30" in run.stdout
    run = subprocess.run(
        [sys.executable, "-m", "members.minh_vg.w2", "missing.csv"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert run.returncode == 1
    assert "missing.csv" in run.stderr and "Traceback" not in run.stderr


def test_main_prints_tasks_and_reports_invalid_csv(tmp_path, monkeypatch, capsys):
    main = module("__main__").main
    monkeypatch.setattr(sys, "argv", ["w2"])
    assert main() == 0
    assert "Assignment" in capsys.readouterr().out
    bad = tmp_path / "bad.csv"
    bad.write_text("wrong header", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["w2", str(bad)])
    assert main() == 1
    assert "line 1" in capsys.readouterr().err


def test_fractional_equality_is_feasible():
    errors = module("errors")
    tasks = [module("models").Task("a", 1, 0.1, TODAY), module("models").Task("b", 1, 0.2, TODAY)]
    assert errors.check_feasible(tasks, 0.3) is None
    with pytest.raises(errors.InfeasiblePlan):
        errors.check_feasible(tasks, 0.29999999)
