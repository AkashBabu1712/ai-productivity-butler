# tests/test_agents.py
from memory.memory_bank import MemoryBank
from tools.recipe_tool import RecipeTool
from tools.gmail_tool import GmailTool
from agents.task_planner import TaskPlannerAgent
from agents.meal_planner import MealPlannerAgent
from agents.email_summarizer import EmailSummarizerAgent


def test_task_planner():
    mem = MemoryBank()
    agent = TaskPlannerAgent(mem)
    out = agent.plan_day([{"title": "A", "priority": 2},
                         {"title": "B", "priority": 1}])
    assert out[0]["priority"] == 1


def test_meal_planner():
    mem = MemoryBank()
    recipes = RecipeTool()
    agent = MealPlannerAgent(recipes, mem)
    out = agent.plan_meals({})
    assert len(out) >= 1


def test_email_summarizer_mock():
    mem = MemoryBank()
    gmail = GmailTool(enabled=False)
    agent = EmailSummarizerAgent(gmail, mem)
    out = agent.summarize_inbox()
    assert isinstance(out, list) and len(out) >= 1
