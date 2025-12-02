# app/run_demo.py
from observability.logger import setup_logging, logger
from observability.tracer import Tracer
from observability.metrics import Metrics
from memory.memory_bank import MemoryBank
from config.settings import settings
from tools.gmail_tool import GmailTool
from tools.recipe_tool import RecipeTool
from agents.orchestrator import OrchestratorAgent


def seed_memory(memory: MemoryBank):
    memory.set("recurring_tasks", [
        {"title": "Morning yoga", "priority": 2, "duration_min": 20},
        {"title": "Email triage", "priority": 3, "duration_min": 30},
    ])
    memory.set("diet_prefs", {"include": [
               "paneer", "dal"], "exclude": ["egg"]})
    memory.set("habits", {"reading": 20, "exercise": 3})


def main():
    setup_logging()
    logger.info(f"Starting {settings.APP_NAME} in ENV={settings.ENV}")

    memory = MemoryBank(max_items=settings.MEMORY_MAX_ITEMS)
    seed_memory(memory)

    tracer = Tracer()
    metrics = Metrics()
    gmail = GmailTool(enabled=settings.GMAIL_ENABLED,
                      api_key=settings.GMAIL_API_KEY, user=settings.GMAIL_USER)
    recipes = RecipeTool(enabled=settings.RECIPE_ENABLED)

    orchestrator = OrchestratorAgent(memory, tracer, metrics, gmail, recipes)

    tasks = [
        {"title": "Standup meeting", "priority": 1, "duration_min": 15},
        {"title": "Student session: DSA", "priority": 2, "duration_min": 60},
        {"title": "Code review", "priority": 3, "duration_min": 45},
    ]

    result = orchestrator.run(tasks, prefs=None, habit_update={"reading": 10})
    logger.info("Run complete")
    print("\n=== Orchestrator Output ===")
    for k, v in result.items():
        if k in ("trace", "metrics"):
            print(f"{k}: {v}")
        else:
            print(f"{k}:")
            for item in v:
                print(" -", item)


if __name__ == "__main__":
    main()
