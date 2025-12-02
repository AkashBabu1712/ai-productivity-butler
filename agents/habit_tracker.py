# agents/habit_tracker.py
from typing import Dict, Any
from memory.memory_bank import MemoryBank


class HabitTrackerAgent:
    def __init__(self, memory: MemoryBank):
        self.memory = memory

    def check_in(self, update: Dict[str, Any] | None = None) -> Dict[str, Any]:
        habits = self.memory.get("habits", {"reading": 0, "exercise": 0})
        if update:
            for k, v in update.items():
                habits[k] = habits.get(k, 0) + int(v)
        self.memory.set("habits", habits)
        return habits
