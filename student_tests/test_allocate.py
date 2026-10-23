from datetime import date
from pathlib import Path
import importlib
import pytest

TODAY = date(2026, 10, 26)
ROOT = Path(__file__).resolve().parents[1]


def planner(name):
    return importlib.import_module(f"shared.study_planner.{name}")


def task(title="Exam", importance=5, effort=6, due=date(2026, 10, 30)):
    return importlib.import_module("shared.contract").Task(title, importance, effort, due)


def test_allocate_fractional_budget_without_mutation():
    tasks = [task("HW", effort=1.5), task("Exam", effort=6)]
    blocks = planner("allocate").allocate(tasks, 2)
    assert [(b.task.title, b.hours) for b in blocks] == [("HW", 1.5), ("Exam", 0.5)]
    assert tasks[1].effort_h == 6
    assert blocks[0].task is tasks[0]
    assert planner("allocate").allocate(tasks, 0) == []
    assert planner("allocate").allocate([], 2) == []
    assert sum(b.hours for b in planner("allocate").allocate(tasks, 20)) == 7.5
    assert planner("allocate").allocate([task(effort=0)], 1) == []


@pytest.mark.parametrize("hours", [-1, float("nan"), float("inf")])
def test_allocate_rejects_bad_budget(hours):
    with pytest.raises(ValueError):
        planner("allocate").allocate([task()], hours)
