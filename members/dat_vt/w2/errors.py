"""W2-3: Custom exception for infeasible study plans."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from members.dat_vt.w2.models import Task


class InfeasiblePlan(Exception):
    """Raised when total effort exceeds the available hours."""

    def __init__(self, needed_h: float, available_h: float) -> None:
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self) -> str:
        return (
            f"Infeasible plan: {self.needed_h}h needed "
            f"but only {self.available_h}h available"
        )


def check_feasible(tasks: list["Task"], available_h: float) -> None:
    """Raise InfeasiblePlan if total effort exceeds available hours."""
    needed = sum(t.effort_h for t in tasks)
    if needed > available_h:
        raise InfeasiblePlan(needed_h=needed, available_h=available_h)
