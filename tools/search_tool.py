# tools/search_tool.py
from typing import List


class SearchTool:
    def __init__(self, enabled: bool = True):
        self.enabled = enabled

    def search(self, query: str) -> List[str]:
        if not self.enabled:
            return []
        # Placeholder: return mock results
        return [f"Result for '{query}' #1", f"Result for '{query}' #2"]
