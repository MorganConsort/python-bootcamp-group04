"""Custom exceptions and validation for W2-3."""

from .models import Task


class InfeasiblePlan(Exception):
    """Exception raised when available hours are less than needed task effort."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Plan requires {needed_h} hours, but only {available_h} hours are available."
        )

    def __str__(self) -> str:
        return f"Plan requires {self.needed_h} hours, but only {self.available_h} hours are available."


def check_feasible(tasks: list[Task], available_h: float) -> None:
    """Check if tasks can be completed within available hours.

    Raises InfeasiblePlan if needed hours exceed available hours.
    """
    needed_h = sum(t.effort_h for t in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
