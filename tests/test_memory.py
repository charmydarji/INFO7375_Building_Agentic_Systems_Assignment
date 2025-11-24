# tests/test_memory.py
import json
from src.memory.memory_manager import append_feedback

def test_feedback_saved(tmp_path):
    # temp memory file
    temp_memory = tmp_path / "memory.json"
    temp_memory.write_text(json.dumps({"feedback": []}))

    # write feedback into temporary file
    append_feedback("Test Query", 5, "Great", file_path=temp_memory)

    data = json.loads(temp_memory.read_text())
    assert len(data["feedback"]) >= 1
    assert data["feedback"][0]["query"] == "Test Query"
    assert data["feedback"][0]["rating"] == 5
