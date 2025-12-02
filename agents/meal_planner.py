# agents/meal_planner.py
from typing import Dict, List
from tools.recipe_tool import RecipeTool
from memory.memory_bank import MemoryBank


class MealPlannerAgent:
    def __init__(self, recipes: RecipeTool, memory: MemoryBank):
        self.recipes = recipes
        self.memory = memory

    def plan_meals(self, preferences: Dict | None = None) -> List[Dict]:
        suggestions = self.recipes.suggest(
            preferences or self.memory.get("diet_prefs", {}))
        self.memory.set("last_meals", suggestions)
        return suggestions
