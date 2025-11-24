def web_search(query: str, num_results: int = 5):
    """
    Domain-specific 'search' that returns local software-testing themed sources.
    We use `local://` URLs so the content_fetch_tool knows not to hit the network.
    """
    base_topic = f"AI and generative AI in software testing: {query}"

    return [
        {
            "title": "Overview of AI in Software Testing",
            "url": "local://source-1",
            "snippet": "High-level overview of how AI supports test case generation, regression testing, and CI/CD.",
        },
        {
            "title": "Benefits and Challenges of Generative AI for QA",
            "url": "local://source-2",
            "snippet": "Pros, cons, and risks of using generative models in testing pipelines.",
        },
        {
            "title": "Industrial Case Studies: AI-Driven Test Automation",
            "url": "local://source-3",
            "snippet": "Real-world stories from teams adopting AI-powered test tools.",
        },
    ][:num_results]
