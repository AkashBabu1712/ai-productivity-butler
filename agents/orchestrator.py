# agents/orchestrator.py
from typing import Dict, List, Any
from observability.tracer import Tracer
from observability.metrics import Metrics
from memory.memory_bank import MemoryBank
from agents.task_planner import TaskPlannerAgent
from agents.meal_planner import MealPlannerAgent
from agents.email_summarizer import EmailSummarizerAgent
from agents.habit_tracker import HabitTrackerAgent
from tools.recipe_tool import RecipeTool
from tools.gmail_tool import GmailTool


class OrchestratorAgent:
    def __init__(self, memory: MemoryBank, tracer: Tracer, metrics: Metrics, gmail: GmailTool, recipes: RecipeTool):
        self.memory = memory
        self.tracer = tracer
        self.metrics = metrics
        self.task_planner = TaskPlannerAgent(memory)
        self.meal_planner = MealPlannerAgent(recipes, memory)
        self.email_summarizer = EmailSummarizerAgent(gmail, memory)
        self.habit_tracker = HabitTrackerAgent(memory)

    def run(self, tasks: List[Dict[str, Any]], prefs: Dict[str, Any] | None = None, habit_update: Dict[str, int] | None = None):
        self.tracer.add("orchestrator:start", f"tasks={len(tasks)}")
        schedule = self.task_planner.plan_day(tasks)
        self.metrics.tasks_planned += len(schedule)

        meals = self.meal_planner.plan_meals(preferences=prefs)
        self.metrics.recipes_generated += len(meals)

        emails = self.email_summarizer.summarize_inbox()
        self.metrics.emails_summarized += len(emails)

        habits = self.habit_tracker.check_in(update=habit_update)
        self.metrics.habit_checkins += 1

        self.tracer.add("orchestrator:end", "completed")
        return {
            "schedule": schedule,
            "meals": meals,
            "emails": emails,
            "habits": habits,
            "metrics": self.metrics.as_dict(),
            "trace": self.tracer.timeline(),
        }
