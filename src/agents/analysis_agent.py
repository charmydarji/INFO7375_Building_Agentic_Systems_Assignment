# src/agents/analysis_agent.py
from src.tools.content_fetch_tool import fetch_page_content
from src.tools.summarizer_tool import summarize_text
from src.tools.custom_metrics_tool import extract_research_metrics


class AnalysisAgent:
    def __init__(self, name: str = "Analysis Agent"):
        self.name = name

    def analyze_sources(self, search_results: list, topic: str):
        """
        For each search result:
        - Prefer local 'content' if present (from web_search_tool ARTICLES)
        - Otherwise fetch from the URL (HTTP)
        - Summarize the text
        - Extract structured metrics via the custom tool
        """
        summaries = []
        all_metrics = []

        for res in search_results:
            url = res.get("url", "")
            title = res.get("title", "Untitled Source")

            # ✅ 1. Prefer local content (stable, deterministic)
            if "content" in res and res["content"]:
                raw_text = res["content"]
            else:
                # ✅ 2. Fallback: fetch from the web (may return an error string)
                raw_text = fetch_page_content(url)

            # ✅ 3. Summarize the content
            summary = summarize_text(raw_text, topic=topic)

            # ✅ 4. Extract metrics (custom tool)
            metrics = extract_research_metrics(raw_text, topic=topic)

            summaries.append({
                "title": title,
                "url": url,
                "summary": summary,
                "metrics": metrics,
            })
            all_metrics.append(metrics)

        return summaries, all_metrics
