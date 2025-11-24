# src/memory/memory_manager.py
import json
from pathlib import Path

MEMORY_FILE = Path("memory.json")


def load_memory():
    if not MEMORY_FILE.exists():
        return {}
    try:
        return json.load(MEMORY_FILE.open())
    except Exception:
        return {}


def save_memory(memory: dict):
    with MEMORY_FILE.open("w") as f:
        json.dump(memory, f, indent=2)


def append_feedback(query, rating, comments, file_path=MEMORY_FILE):
    with open(file_path, "r+") as f:
        data = json.load(f)
        data["feedback"].append({
            "query": query,
            "rating": rating,
            "comments": comments
        })
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

