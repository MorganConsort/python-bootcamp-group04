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


def write_csv(tmp_path, text, *, encoding="utf-8"):
    source = tmp_path / "tasks.csv"
    source.write_text(text, encoding=encoding)
    return source


def test_parse_converts_every_field_in_file_order(tmp_path):
    source = write_csv(
        tmp_path,
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6,2026-10-30\n"
        "Assignment,4,1.5,2026-10-27\n",
    )

    tasks = planner("parse").parse_csv(source)

    assert [(t.title, t.importance, t.effort_h, t.deadline) for t in tasks] == [
        ("DS exam", 5, 6.0, date(2026, 10, 30)),
        ("Assignment", 4, 1.5, date(2026, 10, 27)),
    ]


def test_parse_accepts_utf8_bom_and_crlf(tmp_path):
    source = tmp_path / "tasks.csv"
    source.write_bytes(
        "title,importance,effort_h,deadline\r\nRead,3,1.5,2026-10-30\r\n".encode("utf-8-sig")
    )

    [parsed] = planner("parse").parse_csv(source)

    assert parsed.title == "Read"
    assert parsed.deadline == date(2026, 10, 30)


def test_parse_accepts_a_quoted_title_with_a_comma(tmp_path):
    source = write_csv(
        tmp_path,
        'title,importance,effort_h,deadline\n"Read, review",3,1.5,2026-10-30\n',
    )

    [parsed] = planner("parse").parse_csv(source)

    assert parsed.title == "Read, review"


@pytest.mark.parametrize(
    "header",
    [
        "Title,importance,effort_h,deadline",
        "title,importance,effort_h",
        "title,importance,effort_h,deadline,extra",
    ],
)
def test_parse_requires_the_exact_header(tmp_path, header):
    source = write_csv(tmp_path, f"{header}\nRead,3,1.5,2026-10-30\n")

    with pytest.raises(ValueError, match="line 1"):
        planner("parse").parse_csv(source)


@pytest.mark.parametrize("title", ["", "   "])
def test_parse_rejects_a_blank_title(tmp_path, title):
    source = write_csv(
        tmp_path,
        f"title,importance,effort_h,deadline\n{title},3,1.5,2026-10-30\n",
    )

    with pytest.raises(ValueError, match="line 2"):
        planner("parse").parse_csv(source)


def test_parse_rejects_a_blank_line(tmp_path):
    source = write_csv(tmp_path, "title,importance,effort_h,deadline\n\n")

    with pytest.raises(ValueError, match="line 2"):
        planner("parse").parse_csv(source)


@pytest.mark.parametrize("row", ["Read,3,1.5,2026-10-30,extra", "Read,3,1.5"])
def test_parse_rejects_wrong_field_counts(tmp_path, row):
    source = write_csv(tmp_path, f"title,importance,effort_h,deadline\n{row}\n")

    with pytest.raises(ValueError, match="line 2"):
        planner("parse").parse_csv(source)


@pytest.mark.parametrize("importance", ["0", "6"])
def test_parse_rejects_importance_outside_the_contract_range(tmp_path, importance):
    source = write_csv(
        tmp_path,
        f"title,importance,effort_h,deadline\nRead,{importance},1.5,2026-10-30\n",
    )

    with pytest.raises(ValueError, match="line 2"):
        planner("parse").parse_csv(source)


@pytest.mark.parametrize("effort", ["-1", "inf", "-inf"])
def test_parse_rejects_invalid_effort_values(tmp_path, effort):
    source = write_csv(
        tmp_path,
        f"title,importance,effort_h,deadline\nRead,3,{effort},2026-10-30\n",
    )

    with pytest.raises(ValueError, match="line 2"):
        planner("parse").parse_csv(source)


def test_parse_missing_file_propagates_oserror(tmp_path):
    with pytest.raises(FileNotFoundError):
        planner("parse").parse_csv(tmp_path / "missing.csv")
