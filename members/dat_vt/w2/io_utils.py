"""W2-2: Load tasks from CSV and save them as JSON."""

import csv
import json
from datetime import date
from pathlib import Path

from members.dat_vt.w2.models import Task


def load_tasks(path: str | Path) -> list[Task]:
    """Read a CSV with header title,importance,effort_h,deadline.

    Invalid rows raise ValueError mentioning the 1-based line number.
    """
    tasks: list[Task] = []
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for lineno, row in enumerate(reader, start=2):  # header is line 1
            try:
                tasks.append(
                    Task(
                        title=row["title"],
                        importance=int(row["importance"]),
                        effort_h=float(row["effort_h"]),
                        deadline=date.fromisoformat(row["deadline"]),
                    )
                )
            except (KeyError, ValueError, TypeError) as exc:
                raise ValueError(f"line {lineno}: {exc}") from exc
    return tasks


def save_json(tasks: list[Task], path: str | Path) -> None:
    """Serialize a list of Tasks to a JSON file, converting dates to strings."""

    def _default(obj):
        if isinstance(obj, date):
            return obj.isoformat()
        raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

    with open(path, "w", encoding="utf-8") as fh:
        json.dump(
            [
                {
                    "title": t.title,
                    "importance": t.importance,
                    "effort_h": t.effort_h,
                    "deadline": t.deadline.isoformat(),
                }
                for t in tasks
            ],
            fh,
            indent=2,
            default=_default,
        )
