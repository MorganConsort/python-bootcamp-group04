from dataclasses import dataclass 
from datetime import date
from datetime import timedelta
    

class Task:
    title: str
    importance: int
    effort_h: float  
    deadline: date 
    
    def __post__init__(self):
        if not 1 <= self.importance <= 5:
            raise ValueError("Importance must be 1-5")
    
    def days_left(self, today=None):
        if today is None:
            today = date.today()
        return (self.deadline - today).days