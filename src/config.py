# src/config.py
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Models
INTERMEDIATE_MODEL = "gpt-5-nano"   # for summarization, analysis, fact-check
FINAL_MODEL = "gpt-5-mini"          # for final report writing

# Summarization settings
MAX_SUMMARY_TOKENS = 300

# Debug mode: if True, tools will fall back instead of crashing on errors
DEBUG_MODE = True
