from datetime import date
from pathlib import Path
import importlib

TODAY = date(2026, 10, 26)
ROOT = Path(__file__).resolve().parents[1]


def planner(name):
    return importlib.import_module(f"shared.study_planner.{name}")


def task(title="Exam", importance=5, effort=6, due=date(2026, 10, 30)):
    return importlib.import_module("shared.contract").Task(title, importance, effort, due)


def test_render_and_pipeline():
    tasks = planner("parse").parse_csv(ROOT / "samples/tasks.csv")
    blocks = planner("allocate").allocate(planner("prioritise").prioritise(tasks, TODAY), 2)
    output = planner("render").render(blocks)
    assert output == "Plan (2 h):\n  1. Assignment: 1.5 h\n  2. DS exam: 0.5 h"
    assert planner("render").render([]) == "No tasks scheduled."
