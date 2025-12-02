# tests/test_tools.py
from tools.utils import prioritize


def test_prioritize():
    items = [{"priority": 3}, {"priority": 1}, {"priority": 2}]
    out = prioritize(items)
    assert [i["priority"] for i in out] == [1, 2, 3]
