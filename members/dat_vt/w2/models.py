"""W2-1: Task model – a dataclass representing a study task."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    title: str
    importance: int          # 1-5
    effort_h: float
    deadline: date

    def __post_init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Return the number of days until the deadline, never below 0."""
        return max((self.deadline - today).days, 0)