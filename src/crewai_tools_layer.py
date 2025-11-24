# src/crewai_tools_layer.py

from crewai.tools import BaseTool

class FullResearchPipelineTool(BaseTool):
    """
    Custom CrewAI tool that runs our full software-testing research pipeline.
    This wraps the Python Controller so CrewAI can call it as a tool.
    """

    name: str = "Full Research Pipeline"
    description: str = (
        "Run the full domain-specific research pipeline for AI + software testing. "
        "Input: a user question about AI/LLMs in software testing. "
        "Output: a well-structured Markdown research report."
    )

    def _run(self, topic: str) -> str:
        from src.controller import Controller
        
        controller = Controller()
        return controller.run_pipeline(topic)


# This is what we import in crewai_agents.py
full_research_pipeline_tool = FullResearchPipelineTool()