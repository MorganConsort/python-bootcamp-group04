# W2-2
import csv
import json
from dataclasses import asdict
from datetime import date

from .models import Task


def load_tasks(path) -> list[Task]:

    tasks : list[Task] = []

    with open(path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            
            try:
                t= row["title"]
                i = int(row["importance"])
                e = float(row["effort_h"])
                d = date.fromisoformat(row["deadline"])

                task = Task(t,i,e,d)
                tasks.append(task)
            except (KeyError, ValueError) as err:
                raise ValueError(
                    f"Invalid CSV at line {reader.line_num} : {err}"
                ) from err

    return tasks

def save_json(tasks: list[Task], path):
    json_list = []
    
    for task in tasks:
        data = asdict(task)
        data["deadline"] = task.deadline.isoformat()
        json_list.append(data)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(json_list, file, indent=2, ensure_ascii=False)
