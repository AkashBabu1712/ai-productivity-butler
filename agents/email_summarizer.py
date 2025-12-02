# agents/email_summarizer.py
from typing import List, Dict
from tools.gmail_tool import GmailTool
from memory.memory_bank import MemoryBank


class EmailSummarizerAgent:
    def __init__(self, gmail: GmailTool, memory: MemoryBank):
        self.gmail = gmail
        self.memory = memory

    def summarize_inbox(self) -> List[Dict]:
        summaries = self.gmail.important_summaries()
        self.memory.set("last_email_summaries", summaries)
        return summaries
