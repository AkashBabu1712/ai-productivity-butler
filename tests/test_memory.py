# tests/test_memory.py
from memory.memory_bank import MemoryBank


def test_memory_set_get():
    m = MemoryBank()
    m.set("foo", "bar")
    assert m.get("foo") == "bar"
s