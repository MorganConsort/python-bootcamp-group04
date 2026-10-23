import csv
import json
from datetime import date
from dataclasses import asdict
from models import Task


def load_tasks(path: str) -> list[Task]:
    tasks = []
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)

        header = next(reader, None)

        for line_num, row in enumerate(reader, start=2):
            if not row:
                continue

            if len(row) != 4:
                raise ValueError(f"Line {line_num}: Expected 4 columns, got {len(row)}")

            title, importance_str, effort_h_str, deadline_str = row

            try:
                importance = int(importance_str.strip())
                effort_h = float(effort_h_str.strip())
                deadline = date.fromisoformat(deadline_str.strip())

                task = Task(
                    title=title.strip(),
                    importance=importance,
                    effort_h=effort_h,
                    deadline=deadline,
                )
                tasks.append(task)
            except Exception as e:
                raise ValueError(f"Line {line_num}: Invalid data ({e})") from e

    return tasks


def save_json(tasks: list[Task], path: str) -> None:
    data = []
    for task in tasks:
        task_dict = asdict(task)
        if isinstance(task_dict["deadline"], date):
            task_dict["deadline"] = task_dict["deadline"].isoformat()
        data.append(task_dict)

    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
