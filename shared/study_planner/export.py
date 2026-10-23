"""Export a study plan (list of Blocks) to a JSON file."""

import json
from pathlib import Path

from shared.contract import Block


def export_plan(blocks: list[Block], path: str | Path) -> None:
    """Write blocks to a JSON file with human-readable dates.

    Output format:
        [
          {"task": "title", "importance": 3, "deadline": "2026-10-30", "hours": 2.0},
          ...
        ]
    """
    data = [
        {
            "task": b.task.title,
            "importance": b.task.importance,
            "deadline": b.task.deadline.isoformat(),
            "hours": b.hours,
        }
        for b in blocks
    ]
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)


def import_plan_titles(path: str | Path) -> list[str]:
    """Read back a previously exported plan and return the task titles in order."""
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return [entry["task"] for entry in data]
