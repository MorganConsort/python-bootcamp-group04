# Addition checks for W2-2 file conversion and malformed records
# Not required, but useful for file errors and debugging

import json
from datetime import date

import pytest

from .io_utils import load_tasks, save_json

HEADER = "title,importance,effort_h,deadline\n"


def test_csv_json_round_trip(tmp_path):
    source = tmp_path / "tasks.csv"
    source.write_text(HEADER + '"Study, Python",5,1.5,2026-10-30\n', encoding="utf-8")
    tasks = load_tasks(source)
    assert tasks[0].deadline == date(2026, 10, 30)
    output = tmp_path / "tasks.json"
    save_json(tasks, output)
    assert json.loads(output.read_text(encoding="utf-8")) == [
        {
            "title": "Study, Python",
            "importance": 5,
            "effort_h": 1.5,
            "deadline": "2026-10-30",
        }
    ]


@pytest.mark.parametrize(
    "bad_row",
    [
        "Bad,3",
        "Bad,3,1,2026-10-30,extra",
        ",3,1,2026-10-30",
        "Bad,9,1,2026-10-30",
        "Bad,3,nope,2026-10-30",
        "Bad,3,1,not-a-date",
        '"Unclosed,3,1,2026-10-30',
    ],
)
def test_invalid_row_reports_line_three(tmp_path, bad_row):
    source = tmp_path / "bad.csv"
    source.write_text(
        HEADER + "Good,3,1,2026-10-30\n" + bad_row + "\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="line 3"):
        load_tasks(source)


def test_missing_header_reports_line_one(tmp_path):
    source = tmp_path / "bad.csv"
    source.write_text("title,importance\nBad,3\n", encoding="utf-8")
    with pytest.raises(ValueError, match="line 1"):
        load_tasks(source)
