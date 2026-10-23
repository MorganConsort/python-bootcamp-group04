from datetime import date
from pathlib import Path
import importlib
import pytest

TODAY = date(2026, 10, 26)
ROOT = Path(__file__).resolve().parents[1]


def planner(name):
    return importlib.import_module(f"shared.study_planner.{name}")


def task(title="Exam", importance=5, effort=6, due=date(2026, 10, 30)):
    return importlib.import_module("shared.contract").Task(title, importance, effort, due)


def test_parse_returns_contract_tasks(tmp_path):
    tasks = planner("parse").parse_csv(ROOT / "samples/tasks.csv")
    assert [t.title for t in tasks] == ["DS exam", "Assignment"]
    assert all(isinstance(t, importlib.import_module("shared.contract").Task) for t in tasks)
    source = tmp_path / "bad.csv"
    source.write_text(
        "title,importance,effort_h,deadline\na,3,1,2026-10-30\nb,8,1,2026-10-30\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="line 3"):
        planner("parse").parse_csv(source)


@pytest.mark.parametrize(
    "text,line",
    [
        ("", 1),
        ("wrong,header\n", 1),
        ("title,importance,effort_h,deadline\na,3,nan,2026-10-30", 2),
        ('title,importance,effort_h,deadline\n"unfinished', 2),
        ("title,importance,effort_h,deadline\na,3,1,invalid", 2),
        ("title,importance,effort_h,deadline\na,3,1", 2),
    ],
)
def test_parse_rejects_invalid_records(tmp_path, text, line):
    source = tmp_path / "tasks.csv"
    source.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError, match=f"line {line}"):
        planner("parse").parse_csv(source)
