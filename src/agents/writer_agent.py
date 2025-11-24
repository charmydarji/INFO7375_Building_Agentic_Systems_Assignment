# src/agents/writer_agent.py
from src.tools.summarizer_tool import summarize_text, format_final_report


class WriterAgent:
    def __init__(self, name: str = "Writer Agent"):
        self.name = name

    def write_report(self, topic: str, summaries: list, metrics_list: list, fact_checks: list):
        """
        Combine everything into a final Markdown report.
        """
        # Combine summaries to form a base executive summary
        combined = "\n\n".join([s["summary"] for s in summaries])
        executive_summary = summarize_text(combined, topic=topic, max_tokens=250)

        # Build clean key findings: first sentence per article
        key_points = []
        for s in summaries:
            first_sentence = s["summary"].split(".")[0].strip()
            if first_sentence:
                key_points.append(f"**{s['title']}** — {first_sentence}.")

        if not key_points:
            key_points = [f"No key findings extracted for topic '{topic}'"]

        # Build metrics table
        rows = ["| Metric | Value | Context |", "|---|---|---|"]
        for mset in metrics_list:
            for m in mset.get("key_metrics", []):
                rows.append(f"| {m.get('metric','')} | {m.get('value','')} | {m.get('context','')} |")
        metrics_table = "\n".join(rows) if len(rows) > 2 else "No numeric metrics extracted."

        # References from summaries
        references = [{"title": s["title"], "url": s["url"]} for s in summaries]

        # For now we don't show fact-check details in the report text,
        # but they can be logged or extended later.

        report = format_final_report(
            summary=executive_summary,
            key_points=key_points,
            metrics_table=metrics_table,
            references=references,
        )
        return report
