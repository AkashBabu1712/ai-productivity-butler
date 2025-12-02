# observability/tracer.py
from dataclasses import dataclass, field
from typing import List


@dataclass
class TraceEvent:
    name: str
    detail: str


@dataclass
class Tracer:
    events: List[TraceEvent] = field(default_factory=list)

    def add(self, name: str, detail: str):
        self.events.append(TraceEvent(name=name, detail=detail))

    def timeline(self):
        return [f"{e.name}: {e.detail}" for e in self.events]
