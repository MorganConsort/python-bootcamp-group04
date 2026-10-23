"""Load and save utilities for tasks (W2-2)."""

import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task

EXPECTED_HEADER = ["title", "importance", "effort_h", "deadline"]


def load_tasks(path: str | Path) -> list[Task]:
    """Load tasks from a CSV file with header title,importance,effort_h,deadline.

    Raises ValueError with the line number if any row is invalid.
    """
    tasks: list[Task] = []
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        try:
            header = next(reader, None)
            if header != EXPECTED_HEADER:
                raise ValueError("line 1: invalid CSV header")
            for row in reader:
                line_no = reader.line_num
                try:
                    if len(row) != 4:
                        raise ValueError(f"expected 4 fields, got {len(row)}")
                    title, importance_str, effort_str, deadline_str = row
                    task = Task(
                        title=title,
                        importance=int(importance_str),
                        effort_h=float(effort_str),
                        deadline=date.fromisoformat(deadline_str),
                    )
                    tasks.append(task)
                except Exception as exc:
                    raise ValueError(f"line {line_no}: {exc}") from exc
        except csv.Error as exc:
            raise ValueError(f"line {reader.line_num}: {exc}") from exc
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Save tasks to a JSON file."""
    data = [{**asdict(t), "deadline": t.deadline.isoformat()} for t in tasks]
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
