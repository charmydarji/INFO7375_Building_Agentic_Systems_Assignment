# src/crewai_tasks.py
from crewai import Task
from src.crewai_agents import research_orchestrator

research_task = Task(
    description=(
        "The user's research question is: '{topic}'.\n"
        "You are working strictly in the domain of AI and generative AI for "
        "software testing and quality assurance (QA).\n\n"
        "You MUST call the tool 'Full Research Pipeline' exactly once, "
        "passing this question as the 'topic' argument.\n"
        "Return ONLY the Markdown research report string produced by the tool. "
        "Do not add any extra commentary around it."
    ),
    agent=research_orchestrator,
    expected_output=(
        "A well-structured Markdown research report with sections such as "
        "Executive Summary, Applications to software testing / QA, "
        "Benefits, Risks, Open Challenges, and References."
    ),
)
