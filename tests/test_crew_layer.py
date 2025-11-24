# tests/test_crewai_layer.py

from src.crewai_research_crew import run_research_crew
from src.memory.memory_manager import append_feedback


def test_crewai_layer():
    topic = "Role of AI in test automation"
    result = run_research_crew(topic)

    assert isinstance(result, str)
    assert len(result) > 50
    assert "test" in result.lower()
