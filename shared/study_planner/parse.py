"""Parse task CSV files using the agreed shared contract."""

import csv
from datetime import date
from pathlib import Path

from shared.contract import Task

FIELDS = ["title", "importance", "effort_h", "deadline"]


def parse_csv(path: str | Path) -> list[Task]:
    """Read UTF-8 tasks, reporting malformed records with line numbers."""
    tasks = []
    with open(path, encoding="utf-8-sig", newline="") as source:
        reader = csv.reader(source, strict=True)
        try:
            if next(reader, None) != FIELDS:
                raise ValueError("line 1: expected title,importance,effort_h,deadline header")
            for row in reader:
                try:
                    if len(row) != 4 or not row[0].strip():
                        raise ValueError("expected a title and four fields")
                    title, importance, effort, deadline = row
                    tasks.append(
                        Task(title, int(importance), float(effort), date.fromisoformat(deadline))
                    )
                except (ValueError, TypeError) as exc:
                    raise ValueError(f"line {reader.line_num}: {exc}") from exc
        except csv.Error as exc:
            raise ValueError(f"line {reader.line_num}: {exc}") from exc
    return tasks
