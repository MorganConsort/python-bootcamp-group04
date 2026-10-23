# W2-2
import csv
import json
from dataclasses import asdict
from datetime import date
from os import PathLike

from .models import Task


def load_tasks(path: str | PathLike[str]) -> list[Task]:
    """Read tasks, reporting malformed CSV records with their line number."""
    tasks: list[Task] = []
    fields = ["title", "importance", "effort_h", "deadline"]

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, strict=True)
        try:
            if reader.fieldnames != fields:
                raise ValueError("expected header: " + ",".join(fields))

            for row in reader:
                if None in row or any(
                    row[field] is None or not row[field].strip() for field in fields
                ):
                    raise ValueError("expected four non-empty fields")
                t = row["title"]
                i = int(row["importance"])
                e = float(row["effort_h"])
                d = date.fromisoformat(row["deadline"])

                task = Task(t, i, e, d)
                tasks.append(task)
        except (csv.Error, KeyError, TypeError, ValueError) as err:
            line = max(reader.line_num, reader.reader.line_num, 1)
            raise ValueError(f"Invalid CSV at line {line}: {err}") from err

    return tasks


def save_json(tasks: list[Task], path: str | PathLike[str]) -> None:
    """Save task fields as JSON, using ISO dates."""
    json_list = []

    for task in tasks:
        data = asdict(task)
        data["deadline"] = task.deadline.isoformat()
        json_list.append(data)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(json_list, file, indent=2, ensure_ascii=False)
