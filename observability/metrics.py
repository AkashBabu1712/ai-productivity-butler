# observability/metrics.py
from dataclasses import dataclass


@dataclass
class Metrics:
    tasks_planned: int = 0
    recipes_generated: int = 0
    emails_summarized: int = 0
    habit_checkins: int = 0

    def as_dict(self): return self.__dict__
