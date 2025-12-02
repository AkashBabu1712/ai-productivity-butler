# tools/recipe_tool.py
from typing import Dict, List


class RecipeTool:
    def __init__(self, enabled: bool = True):
        self.enabled = enabled

    def suggest(self, preferences: Dict[str, List[str]] | None = None) -> List[Dict]:
        base = [
            {"title": "Veg Dal Khichdi", "ingredients": [
                "rice", "dal", "turmeric", "salt"], "time_min": 35},
            {"title": "Masala Poha", "ingredients": [
                "poha", "peanuts", "onion", "chilli"], "time_min": 20},
            {"title": "Paneer Bhurji", "ingredients": [
                "paneer", "tomato", "onion", "spices"], "time_min": 25},
        ]
        if not preferences:
            return base
        # Filter by preferences (dietary includes, excludes)
        include = set(preferences.get("include", []))
        exclude = set(preferences.get("exclude", []))
        filtered = []
        for r in base:
            if exclude and any(x in exclude for x in r["ingredients"]):
                continue
            if include and not any(x in include for x in r["ingredients"]):
                continue
            filtered.append(r)
        return filtered or base
