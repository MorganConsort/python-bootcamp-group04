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


def test_contract():
    contract = importlib.import_module("shared.contract")
    t = task()
    assert contract.Block(t, 0.5).task is t
    assert t.deadline == date(2026, 10, 30)
    with pytest.raises(ValueError):
        task(importance=0)
    with pytest.raises(ValueError):
        task(effort=-1)
