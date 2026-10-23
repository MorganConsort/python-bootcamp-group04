"""Parse task CSV files into the shared Task contract."""

import csv
from datetime import date
from pathlib import Path

from shared.contract import Task

FIELDS = ["title", "importance", "effort_h", "deadline"]


def _error(line: int, message: str) -> ValueError:
    """Build a ValueError that always identifies the physical CSV line."""
    return ValueError(f"line {line}: {message}")


def _row_to_task(row: list[str], line: int) -> Task:
    """Convert one CSV row to a Task, tagging any failure with its line."""
    if len(row) != len(FIELDS):
        raise _error(line, f"expected {len(FIELDS)} fields, got {len(row)}")

    title, importance_text, effort_text, deadline_text = row
    try:
        return Task(
            title=title,
            importance=int(importance_text),
            effort_h=float(effort_text),
            deadline=date.fromisoformat(deadline_text),
        )
    except (TypeError, ValueError) as exc:
        raise _error(line, str(exc)) from exc


def parse_csv(path: str | Path) -> list[Task]:
    """Read a UTF-8 task CSV and return Task objects in file order.

    The first line must be exactly ``title,importance,effort_h,deadline``.
    Malformed headers and records raise ``ValueError`` with a line number.
    """
    tasks: list[Task] = []
    with open(path, encoding="utf-8-sig", newline="") as source:
        reader = csv.reader(source, strict=True)
        try:
            if next(reader, None) != FIELDS:
                raise _error(1, "expected title,importance,effort_h,deadline header")

            for row in reader:
                line = reader.line_num
                if not row:
                    raise _error(line, "blank line is not a task")
                if not row[0].strip():
                    raise _error(line, "title must not be empty")
                tasks.append(_row_to_task(row, line))
        except csv.Error as exc:
            raise _error(reader.line_num, str(exc)) from exc

    return tasks
