"""Rank tasks by importance divided by remaining days."""

from datetime import date

from shared.contract import Task


def prioritise(tasks: list[Task], today: date) -> list[Task]:
    """Return a stable descending ranking; due/overdue tasks use one day."""
    return sorted(
        tasks, key=lambda task: task.importance / max(1, (task.deadline - today).days), reverse=True
    )
