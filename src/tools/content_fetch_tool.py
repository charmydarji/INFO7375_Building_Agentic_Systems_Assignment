# src/tools/content_fetch_tool.py
import requests
from bs4 import BeautifulSoup

def fetch_page_content(url: str) -> str:
    """
    Fetch page HTML and extract main text.
    Handles http(s) URLs normally.
    Skips remote fetch for local:// URLs.
    """

    # NEW: Skip real HTTP requests for local mock URLs
    if url.startswith("local://"):
        return "[LOCAL CONTENT PROVIDED DIRECTLY — no fetch performed]"

    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
    except Exception:
        # Silently return empty text on error
        return ""

    soup = BeautifulSoup(resp.text, "html.parser")
    
    # Extract paragraph text
    texts = [p.get_text(strip=True) for p in soup.find_all("p")]

    # Return first 80 text segments (prevents massive dumps)
    return "\n".join(texts[:80])
