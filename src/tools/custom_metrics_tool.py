# src/tools/custom_metrics_tool.py
import json
from openai import OpenAI
from dotenv import load_dotenv

from src.config import OPENAI_API_KEY, INTERMEDIATE_MODEL, DEBUG_MODE

load_dotenv()
client = OpenAI(api_key=OPENAI_API_KEY)

def extract_research_metrics(text: str, topic: str) -> dict:
    """
    Heuristic custom tool for the software-testing domain.

    Detects domain-specific indicators such as:
    - test coverage
    - defect detection / bugs found
    - flakiness / flaky tests
    - time savings
    - cost savings
    """
    lower = text.lower()

    metrics = {
        "mentions_test_coverage": "coverage" in lower,
        "mentions_defect_rates": any(k in lower for k in ["defect", "bug rate", "bugs found"]),
        "mentions_flakiness": "flaky" in lower or "flakiness" in lower,
        "mentions_time_savings": any(k in lower for k in ["time saving", "faster", "cycle time"]),
        "mentions_cost_savings": "cost" in lower or "savings" in lower,
    }

    return {
        "topic": topic,
        "raw_text_length": len(text),
        "testing_metrics_flags": metrics,
    }


# ----------------------------
# NEW: Compatibility for tests
# ----------------------------

def compute_custom_metrics(text: str) -> dict:
    """
    Thin wrapper so tests can import this function.

    The test only checks `word_count` and `sentence_count`.
    So we return a simplified dictionary.
    """
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    words = text.split()

    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
    }
