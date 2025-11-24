# src/agents/factcheck_agent.py
from src.tools.summarizer_tool import summarize_text


class FactCheckAgent:
    def __init__(self, name: str = "Fact-Check Agent"):
        self.name = name

    def fact_check(self, key_claims: list, topic: str):
        """
        Very lightweight 'fact-check':
        Use LLM reasoning over the claims themselves.
        (You could add more web_search calls here if needed.)
        """
        findings = []
        joined_claims = "\n".join(f"- {c}" for c in key_claims)

        explanation = summarize_text(
            f"Review the following claims about '{topic}' and discuss how plausible and well-balanced they are:\n{joined_claims}",
            topic=topic,
            max_tokens=250,
        )

        findings.append({
            "claims": key_claims,
            "analysis": explanation,
        })
        return findings
