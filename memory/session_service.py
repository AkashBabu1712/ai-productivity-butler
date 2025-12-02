# memory/session_service.py
from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Session:
    session_id: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    context: Dict[str, Any] = field(default_factory=dict)


class InMemorySessionService:
    def __init__(self):
        self.sessions: Dict[str, Session] = {}

    def get_or_create(self, session_id: str) -> Session:
        if session_id not in self.sessions:
            self.sessions[session_id] = Session(session_id=session_id)
        return self.sessions[session_id]

    def update_context(self, session_id: str, key: str, value: Any):
        session = self.get_or_create(session_id)
        session.context[key] = value
        return session.context
