"""Greedy allocation in the supplied task order."""

from math import isfinite

from shared.contract import Block, Task


def allocate(tasks: list[Task], hours: float) -> list[Block]:
    """Fill a finite nonnegative budget, allowing a partial final task."""
    if not isfinite(hours) or hours < 0:
        raise ValueError("hours must be finite and nonnegative")
    blocks = []
    remaining = hours
    for task in tasks:
        if remaining <= 0:
            break
        used = min(task.effort_h, remaining)
        if used > 0:
            blocks.append(Block(task, used))
            remaining -= used
    return blocks
