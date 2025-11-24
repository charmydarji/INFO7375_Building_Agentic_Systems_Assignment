# tests/test_custom_tool.py

from src.tools.custom_metrics_tool import extract_research_metrics

def test_custom_metrics_basic():
    text = (
        "Generative AI improves test coverage and reduces flaky tests. "
        "It also provides time saving and cost saving benefits."
    )

    metrics = extract_research_metrics(text, topic="AI Testing")

    assert isinstance(metrics, dict)
    assert "raw_text_length" in metrics
    assert "testing_metrics_flags" in metrics

    flags = metrics["testing_metrics_flags"]
    assert flags["mentions_test_coverage"]
    assert flags["mentions_flakiness"]
    assert flags["mentions_time_savings"]
    assert flags["mentions_cost_savings"]
