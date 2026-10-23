"""Task model for W2-1."""

from dataclasses import dataclass
from datetime import date


@dataclass
class Task:
    """A task with importance 1-5, effort in hours, and a deadline."""

    title: str
    importance: int
    effort_h: float
    deadline: date

    def __post_init__(self) -> None:
        if not 1 <= self.importance <= 5:
            raise ValueError("importance must be 1-5")

    def days_left(self, today: date) -> int:
        """Calculate days remaining until deadline (never below 0)."""
        return max(0, (self.deadline - today).days)
