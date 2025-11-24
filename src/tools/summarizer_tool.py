# src/tools/summarizer_tool.py
import os
from dotenv import load_dotenv
from openai import OpenAI

from src.config import (
    OPENAI_API_KEY,
    INTERMEDIATE_MODEL,
    FINAL_MODEL,
    MAX_SUMMARY_TOKENS,
    DEBUG_MODE,
)

load_dotenv()

client = OpenAI(api_key=OPENAI_API_KEY)


def _fallback_summary(text: str, topic: str = "") -> str:
    """
    Simple Python-only summary used when LLM fails or no API key.
    Takes the first few non-empty lines / sentences.
    """
    if not text:
        return ""

    # Take first ~5 non-empty lines as a "summary"
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    short = " ".join(lines[:5])
    if topic:
        return f"(Heuristic summary for topic '{topic}') {short}"
    return short


def summarize_text(text: str, topic: str = "", max_tokens: int = MAX_SUMMARY_TOKENS) -> str:
    """
    Summarize a block of text focusing on the given topic.

    Logic:
    - If no API key or DEBUG_MODE: use fallback summary only.
    - Else: try OpenAI Responses API; if anything fails, fallback to heuristic summary.
    """
    text = (text or "").strip()
    if len(text) < 30:
        return text

    # If no key or we want to avoid API: just do heuristic
    if not OPENAI_API_KEY or DEBUG_MODE:
        return _fallback_summary(text, topic)

    prompt = f"""
You are a concise research assistant.

Summarize the following text. Focus on key points relevant to:
'{topic}'.

Write in 3–6 bullet sentences, clear and neutral.

Text:
{text}
"""

    try:
        completion = client.responses.create(
            model=INTERMEDIATE_MODEL,
            input=prompt,
            max_output_tokens=max_tokens,
        )
        # Try to parse the Responses output safely
        out = completion.output
        if out and len(out) > 0 and out[0].content and len(out[0].content) > 0:
            return out[0].content[0].text
        # If structure is weird, fallback
        return _fallback_summary(text, topic)
    except Exception:
        # Any error -> heuristic summary instead of ugly [LLM ERROR]
        return _fallback_summary(text, topic)


def format_final_report(summary: str, key_points: list, metrics_table: str, references: list) -> str:
    """
    Combine components into a Markdown research report.

    - Tries to "polish" the summary with the LLM when possible.
    - Falls back to the raw summary if LLM fails.
    """
    # If no API or debug mode, skip polishing
    if not OPENAI_API_KEY or DEBUG_MODE:
        polished_summary = summary
    else:
        polish_prompt = f"Polish the following executive summary in clear academic style:\n\n{summary}"
        try:
            completion = client.responses.create(
                model=FINAL_MODEL,
                input=polish_prompt,
                max_output_tokens=300,
            )
            out = completion.output
            if out and len(out) > 0 and out[0].content and len(out[0].content) > 0:
                polished_summary = out[0].content[0].text
            else:
                polished_summary = summary
        except Exception:
            polished_summary = summary

    refs_md = "\n".join([f"- [{r.get('title','')}]({r.get('url','')})" for r in references])

    return f"""# Research Report

## 1. Executive Summary
{polished_summary}

## 2. Key Findings
{chr(10).join(['- ' + p for p in key_points])}

## 3. Key Metrics
{metrics_table}

## 4. References
{refs_md}
"""
