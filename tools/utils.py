# tools/utils.py
from typing import List, Dict


def prioritize(tasks: List[Dict]) -> List[Dict]:
    return sorted(tasks, key=lambda t: (t.get("priority", 5), t.get("duration_min", 30)))
