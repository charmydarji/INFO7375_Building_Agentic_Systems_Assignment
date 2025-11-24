# src/agents/search_agent.py
from src.tools.web_search_tool import web_search


class SearchAgent:
    def __init__(self, name: str = "Search Agent"):
        self.name = name

    def run(self, query: str, num_results: int = 3):
        """
        Return a list of search results.
        """
        return web_search(query, num_results=num_results)
