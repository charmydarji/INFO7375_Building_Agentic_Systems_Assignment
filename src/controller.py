# src/controller.py
from src.agents.search_agent import SearchAgent
from src.agents.analysis_agent import AnalysisAgent
from src.agents.factcheck_agent import FactCheckAgent
from src.agents.writer_agent import WriterAgent
from src.memory.memory_manager import append_feedback

# ---- Domain configuration: AI for Software Testing & QA ----
DOMAIN = "AI for software testing and quality assurance"

# Keywords that count as “in-domain”
ALLOWED_KEYWORDS = [
    "software testing",
    "test automation",
    "unit test",
    "integration test",
    "system test",
    "qa",
    "quality assurance",
    "ci/cd",
    "cicd",
    "regression testing",
    "test coverage",
    "defect",
    "bug",
    "test case",
    "test script",
    "selenium",
    "playwright",
    "generative ai",
    "llm",
]


def normalize_topic(raw_query: str) -> str:
    """
    Normalize any incoming query into the software-testing/QA domain.

    If the query is clearly about testing/QA already, we keep it.
    Otherwise, we reinterpret it as:
      "How AI and generative AI relate to software testing and QA,
       given the question: <raw_query>"
    """
    text = raw_query.lower()
    if any(k in text for k in ALLOWED_KEYWORDS):
        return raw_query

    return (
        "How AI and generative AI relate to software testing and quality assurance (QA), "
        f"given the question: {raw_query}"
    )


class Controller:
    """
    Orchestrates the full research pipeline
    for the domain of AI in software testing & QA:

      Search -> Analysis -> Fact-check -> Writing -> Feedback
    """

    def __init__(self):
        self.search_agent = SearchAgent()
        self.analysis_agent = AnalysisAgent()
        self.factcheck_agent = FactCheckAgent()
        self.writer_agent = WriterAgent()

    def run_pipeline(self, user_query: str) -> str:
        # 0) Domain-normalize the topic
        topic = normalize_topic(user_query)

        # 1) Search
        search_results = self.search_agent.run(topic, num_results=3)
        if not search_results:
            return (
                "No search results found. Try a different query "
                "(ideally related to software testing / QA)."
            )

        # 2) Analyze
        summaries, all_metrics = self.analysis_agent.analyze_sources(
            search_results, topic
        )

        # 3) Extract simple claims from summaries (for fact-checking)
        key_claims = [
            s["summary"].split(".")[0] for s in summaries if s.get("summary")
        ][:5]

        # 4) Fact-check (LLM reasoning)
        fact_checks = self.factcheck_agent.fact_check(key_claims, topic)

        # 5) Write final report
        report = self.writer_agent.write_report(
            topic, summaries, all_metrics, fact_checks
        )
        return report

    def record_feedback(self, query: str, rating: int, comments: str = ""):
        """Wrapper around memory manager to record human rating."""
        append_feedback(query, rating, comments)
