from .models import Task


class InfeasiblePlan(Exception):
    needed_h: float
    available_h: float

    def __init__(self, needed_h, available_h):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(needed_h, available_h)

    def __str__(self) -> str:
        return (f"Needed {self.needed_h}h but only {self.available_h}h available")

def check_feasible(tasks, available_h):
    needed_h = sum(task.effort_h for task in tasks)
    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)
   