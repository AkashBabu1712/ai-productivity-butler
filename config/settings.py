# config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # General
    APP_NAME: str = "AI Personal Productivity Butler"
    ENV: str = os.getenv("ENV", "dev")

    # Sessions & memory
    SESSION_MAX_TOKENS: int = 8192
    MEMORY_MAX_ITEMS: int = 1000

    # Tools
    SEARCH_ENABLED: bool = True
    GMAIL_ENABLED: bool = False  # set True when credentials available
    RECIPE_ENABLED: bool = True

    # Credentials (use environment variables)
    GMAIL_API_KEY: str | None = os.getenv("GMAIL_API_KEY")
    GMAIL_USER: str | None = os.getenv("GMAIL_USER")
    SEARCH_API_KEY: str | None = os.getenv("SEARCH_API_KEY")
    SEARCH_ENDPOINT: str | None = os.getenv("SEARCH_ENDPOINT")
    RECIPE_API_KEY: str | None = os.getenv("RECIPE_API_KEY")
    RECIPE_ENDPOINT: str | None = os.getenv("RECIPE_ENDPOINT")


settings = Settings()
