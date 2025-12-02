# tools/gmail_tool.py
from typing import List, Dict


class GmailTool:
    def __init__(self, enabled: bool = False, api_key: str | None = None, user: str | None = None):
        self.enabled = enabled and api_key and user

    def important_summaries(self) -> List[Dict]:
        if not self.enabled:
            return [{"subject": "Mock Update", "action_items": ["Review docs", "Confirm meeting time"]}]
        # Integrate real Gmail API here
        return []
