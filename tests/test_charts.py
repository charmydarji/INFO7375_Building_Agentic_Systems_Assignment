# tests/test_charts.py
import json
from scripts.make_charts import (
    load_feedback,
    chart_overall_score,
    chart_rating_distribution,
)

def test_chart_generation(tmp_path, monkeypatch):
    # Create a temporary memory.json
    memory = tmp_path / "memory.json"
    memory.write_text('{"feedback":[{"query":"Test","rating":5,"comments":"good"}]}')

    # Patch MEMORY_PATH to use tmp_path memory file
    monkeypatch.setattr("scripts.make_charts.MEMORY_PATH", memory)

    # Load DF from patched memory.json
    df = load_feedback()

    # Create temp chart directory
    out = tmp_path / "charts"
    out.mkdir()

    # Generate charts into temp dir
    chart_overall_score(df, output_dir=out)
    chart_rating_distribution(df, output_dir=out)

    pngs = list(out.glob("*.png"))
    assert len(pngs) >= 1
