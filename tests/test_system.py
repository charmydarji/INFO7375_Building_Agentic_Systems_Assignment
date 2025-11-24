# tests/test_system.py

from src.controller import Controller


def test_full_pipeline_runs():
    controller = Controller()

    topic = "How can generative AI improve regression testing?"
    report = controller.run_pipeline(topic)

    # Ensure the pipeline produces output
    assert isinstance(report, str)
    assert len(report) > 50  # not empty
    assert "AI" in report or "software testing" in report
    assert "Summary" in report or "Findings" in report
