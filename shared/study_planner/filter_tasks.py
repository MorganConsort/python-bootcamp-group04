"""Filter tasks by deadline range or minimum importance."""

import json
from pathlib import Path
from shared.contract import Task


def filter_by_deadline(
    tasks: list[Task], start: date, end: date
) -> list[Task]:
    """Return tasks whose deadline falls within [start, end] inclusive.

    Raises ValueError if start > end.
    """
    if start > end:
        raise ValueError(f"start ({start}) must not be after end ({end})")
    return [t for t in tasks if start <= t.deadline <= end]


def filter_by_importance(
    tasks: list[Task], min_importance: int
) -> list[Task]:
    """Return tasks with importance >= min_importance."""
    return [t for t in tasks if t.importance >= min_importance]
