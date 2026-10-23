from datetime import date
from pathlib import Path
import importlib

TODAY = date(2026, 10, 26)
ROOT = Path(__file__).resolve().parents[1]


def planner(name):
    return importlib.import_module(f"shared.study_planner.{name}")


def task(title="Exam", importance=5, effort=6, due=date(2026, 10, 30)):
    return importlib.import_module("shared.contract").Task(title, importance, effort, due)


def test_priority_due_overdue_and_stable_ties():
    tasks = [
        task("later"),
        task("due", 3, due=TODAY),
        task("overdue", 4, due=date(2026, 1, 1)),
        task("tie", 3, due=TODAY),
    ]
    result = planner("prioritise").prioritise(tasks, TODAY)
    assert [t.title for t in result] == ["overdue", "due", "tie", "later"]
    assert tasks[0].title == "later"
    assert planner("prioritise").prioritise([], TODAY) == []
