"""T-W2 shared types; this contract requires review by all six members."""

from dataclasses import dataclass
from datetime import date
from math import isfinite


@dataclass
class Task:
    """A schedulable task; importance is 1-5 and effort is nonnegative."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")
        if not isfinite(self.effort_h) or self.effort_h < 0:
            raise ValueError("effort_h must be finite and nonnegative")


@dataclass
class Block:
    """Hours allocated to a particular task."""

    task: Task
    hours: float
