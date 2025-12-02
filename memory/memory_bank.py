# memory/memory_bank.py
from collections import deque
from typing import Any


class MemoryBank:
    def __init__(self, max_items: int = 1000):
        self.store: dict[str, Any] = {}
        self.timeline: deque[tuple[str, Any]] = deque(maxlen=max_items)

    def get(self, key: str, default=None):
        return self.store.get(key, default)

    def set(self, key: str, value: Any):
        self.store[key] = value
        self.timeline.append((key, value))

    def append_list(self, key: str, item: Any):
        lst = self.store.get(key, [])
        lst.append(item)
        self.store[key] = lst
        self.timeline.append((key, item))

    def snapshot(self) -> dict[str, Any]:
        return dict(self.store)
