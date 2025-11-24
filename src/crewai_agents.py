# src/crewai_agents.py
from crewai import Agent
from src.crewai_tools_layer import full_research_pipeline_tool

# ✅ RENAME variable to 'research_orchestrator' to match the import in crewai_tasks.py
research_orchestrator = Agent(
    role="Research Orchestrator",
    goal=(
        "Given a user question about AI and software testing, "
        "run the full internal research pipeline and return a clear, "
        "well-structured Markdown report."
    ),
    backstory=(
        "You are a domain-specific research assistant focused on "
        "software testing and the use of AI/LLMs for QA, regression "
        "testing, and test automation."
    ),
    tools=[full_research_pipeline_tool],
    verbose=True,
)