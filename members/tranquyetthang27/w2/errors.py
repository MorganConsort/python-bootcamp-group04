from typing import Iterable
from models import Task


class InfeasiblePlan(Exception):

    def __init__(self, needed_h: float, available_h: float):
        super().__init__()
        self.needed_h = needed_h
        self.available_h = available_h

    def __str__(self) -> str:
        return (
            f"Plan is infeasible: needed {self.needed_h:.1f} hours, "
            f"but only {self.available_h:.1f} hours are available."
        )


def check_feasible(tasks: Iterable[Task], available_h: float) -> None:

    total_needed_h = sum(task.effort_h for task in tasks)
    if total_needed_h > available_h:
        raise InfeasiblePlan(needed_h=total_needed_h, available_h=available_h)
