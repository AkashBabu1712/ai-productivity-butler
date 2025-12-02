# agents/task_planner.py
from typing import List, Dict
from tools.utils import prioritize
from memory.memory_bank import MemoryBank


class TaskPlannerAgent:
    def __init__(self, memory: MemoryBank):
        self.memory = memory

    def plan_day(self, tasks: List[Dict]) -> List[Dict]:
        recurring = self.memory.get("recurring_tasks", [])
        all_tasks = recurring + tasks
        schedule = prioritize(all_tasks)
        self.memory.set("last_schedule", schedule)
        return schedule
