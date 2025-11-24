# src/crewai_research_crew.py
from crewai import Crew, Process

from src.crewai_agents import research_orchestrator
from src.crewai_tasks import research_task


def run_research_crew(topic: str) -> str:
    """
    Runs the CrewAI wrapper around the internal multi-agent research pipeline.
    Returns the final Markdown report as a string.
    """
    crew = Crew(
        agents=[research_orchestrator],
        tasks=[research_task],
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff(inputs={"topic": topic})
    return str(result)