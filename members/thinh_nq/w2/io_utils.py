import csv
import json
from dataclasses import asdict
from datetime import date
from pathlib import Path

from .models import Task

FIELDS = ["title", "importance", "effort_h", "deadline"]


def load_tasks(path: str | Path) -> list[Task]:
    tasks = []
    with open(path, encoding="utf-8-sig", newline="") as source:
        reader = csv.reader(source, strict=True)
        try:
            header = next(reader, None)
            if header != FIELDS:
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


def save_json(tasks: list[Task], path: str | Path) -> None:
    data = [{**asdict(task), "deadline": task.deadline.isoformat()} for task in tasks]
    with open(path, "w", encoding="utf-8") as target:
        json.dump(data, target, ensure_ascii=False, indent=2, allow_nan=False)
        target.write("\n")
