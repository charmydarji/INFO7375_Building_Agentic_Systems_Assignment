# AI-Driven Research Assistant for Software Testing

This project is a **multi-agent, domain-specific research assistant** that helps engineers and QA teams explore:

> How AI and generative models can improve software testing, regression testing, and test automation.

It is built for the **INFO 7375 – Building Agentic Systems** assignment using:

- **CrewAI** (agent orchestration)
- A custom **Python Controller pipeline**
- Several internal “agents” (search, analysis, fact-checking, writing)
- A **custom domain metrics tool**
- A **feedback + charting** layer for evaluation

---

## 1. Features

- 🧠 **Domain-specific research**: Focused on AI + software testing / QA
- 🤝 **Multi-agent pipeline**: Search → Analyze → Fact-check → Write
- 🔧 **Custom tool**: Extracts testing-related signals (coverage, defects, time/cost savings)
- 📝 **Markdown reports**: Clean, structured research reports printed in the terminal
- ⭐ **Feedback loop**: CLI prompt stores ratings & comments in `memory.json`
- 📊 **Evaluation charts**: Python script generates rating and sentiment charts from real feedback
- ✅ **Pytest test suite**: Tests for system flow, memory, charts, CrewAI layer, and custom tool

---

## 2. Project Structure

```text
research-navigator/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── search_agent.py
│   │   ├── analysis_agent.py
│   │   ├── factcheck_agent.py
│   │   └── writer_agent.py
│   ├── memory/
│   │   ├── __init__.py
│   │   └── memory_manager.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── web_search.py
│   │   ├── content_fetch_tool.py
│   │   └── custom_metrics_tool.py
│   ├── crewai_agents.py
│   ├── crewai_tasks.py
│   ├── crewai_research_crew.py
│   ├── controller.py
│   └── main.py
├── scripts/
│   └── make_charts.py
├── tests/
│   ├── test_charts.py
│   ├── test_crew_layer.py
│   ├── test_custom_tool.py
│   ├── test_memory.py
│   └── test_system.py
├── docs/
│   └── charts/           # generated charts (PNG)
├── memory.json           # feedback store
├── requirements.txt
├── pytest.ini
└── README.md
```

# AI-Driven Research Assistant for Software Testing

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/research-navigator.git
cd research-navigator
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate    # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the System

```bash
python -m src.main "How can AI improve regression testing?"
```

### 5. Run Tests

```bash
pytest -s
```

### 6. Generate Charts

```bash
python scripts/make_charts.py
```
