# 🧪 Research Navigator – Test Suite Overview

This document explains the structure, purpose, and execution instructions for all automated tests included in the **Research Navigator** agentic system.  
These tests help validate correctness, reliability, and end-to-end execution of the entire system — including agents, tools, memory, and the custom research pipeline.

---

## 📁 Test Files Overview

The project contains the following test modules:

tests/
│── test_custom_tool.py
│── test_system.py
│── test_memory.py
│── test_crew_layer.py
│── test_charts.py
└── test_basic_flow.md

Each file tests a different layer of the multi-agent pipeline.

### **1. `test_custom_tool.py`**

**Purpose:**  
Validates the **custom metrics tool** used by the analysis agent.

**What it checks:**

- The function `compute_custom_metrics(text)` returns a dictionary
- Output contains the expected keys
- Metrics are correctly computed with predictable dummy input
- Ensures the custom tool behaves consistently and reliably

---

### **2. `test_memory.py`**

**Purpose:**  
Ensures that the memory system properly stores and retrieves user feedback.

**What it checks:**

- Adding feedback entries using `append_feedback()`
- Memory file (`memory.json`) updates correctly
- Schema integrity (each entry contains query, rating, comments)

---

### **3. `test_system.py`**

**Purpose:**  
End-to-end validation of the research system without CrewAI.

**What it checks:**

- The **Controller** executes the entire pipeline:
  - Search Agent
  - Analysis Agent
  - Fact Check Agent
  - Writer Agent
- Output is a non-empty Markdown research report
- No crash during sequential execution

This is your **core evaluation test** for system reliability.

---

### **4. `test_crew_layer.py`**

**Purpose:**  
Validates the **CrewAI orchestration layer** (for the assignment requirements).

**What it checks:**

- CrewAI agent successfully initializes
- Custom tool (`FullResearchPipelineTool`) is available
- Calling `run_research_crew(topic)` returns a valid string result
- Ensures multi-agent orchestration runs without exceptions

---

### **5. `test_charts.py`**

**Purpose:**  
Tests the plotting system used to generate evaluation charts.

**What it checks:**

- `load_feedback()` loads memory.json correctly
- Chart functions run without errors:
  - Ratings per query
  - Rating distribution
  - Overall score
  - Feedback categories
- PNG files generated and saved to `docs/charts/`

**Expected output after running tests:**

docs/charts/
│── ratings_per_query.png
│── ratings_distribution.png
│── overall_rating.png
└── feedback_categories.png

These charts are required for your **Evaluation Report**.

---

# ▶️ How to Run All Tests

Ensure your venv is active:

```bash
source venv/bin/activate
```

```bash
pytest -s
```

## 🛠 Required Configurations

### 1. Ensure `pytest.ini` exists at project root:

```ini
[pytest]
pythonpath = .
```

src/
**init**.py
scripts/
**init**.py

Expected Test Output Summary
After setup, running pytest should produce:

collected 5 items

tests/test_custom_tool.py .... PASSED
tests/test_memory.py .... PASSED
tests/test_system.py .... PASSED
tests/test_crew_layer.py .... PASSED
tests/test_charts.py .... PASSED

=================== 5 passed in X.XXs ===================
