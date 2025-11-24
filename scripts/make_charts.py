# scripts/make_charts.py

import json
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# ---------- Paths ----------

ROOT = Path(__file__).resolve().parents[1]   # project root
MEMORY_PATH = ROOT / "memory.json"
OUTPUT_DIR = ROOT / "docs" / "charts"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------- Helpers ----------

def load_feedback() -> pd.DataFrame:
    with open(MEMORY_PATH, "r") as f:
        data = json.load(f)
    df = pd.DataFrame(data["feedback"])
    # Add a simple “question id” label for nicer x-axis
    df["qid"] = [f"Q{i+1}" for i in range(len(df))]
    return df

def add_value_labels(ax):
    """Write the bar value on top of each bar."""
    for p in ax.patches:
        height = p.get_height()
        ax.annotate(
            f"{height:.1f}" if isinstance(height, float) else f"{height}",
            (p.get_x() + p.get_width() / 2, height),
            ha="center",
            va="bottom",
            fontsize=9,
        )

# ---------- Chart 1: Ratings per query ----------

def chart_ratings_by_query(df, output_dir=OUTPUT_DIR):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(df["qid"], df["rating"])
    ax.set_title("User Ratings per Query")
    ax.set_xlabel("Query (Q1, Q2, ...)")
    ax.set_ylabel("Rating (1–5)")
    ax.set_ylim(0, 5.5)
    add_value_labels(ax)
    plt.tight_layout()
    fig.savefig(output_dir / "ratings_per_query.png", dpi=200)
    plt.close(fig)

# ---------- Chart 2: Rating distribution ----------

def chart_rating_distribution(df, output_dir=OUTPUT_DIR):
    counts = df["rating"].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(counts.index.astype(str), counts.values)
    ax.set_title("Rating Distribution")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Number of Responses")
    add_value_labels(ax)
    plt.tight_layout()
    fig.savefig(output_dir / "ratings_distribution.png", dpi=200)
    plt.close(fig)

# ---------- Chart 3: Overall average score ----------

def chart_overall_score(df, output_dir=OUTPUT_DIR):
    avg = df["rating"].mean()
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.bar(["Average"], [avg], width=0.4)
    ax.set_title("Overall Average Rating")
    ax.set_ylabel("Rating (1–5)")
    ax.set_ylim(0, 5.5)
    add_value_labels(ax)
    plt.tight_layout()
    fig.savefig(output_dir / "overall_rating.png", dpi=200)
    plt.close(fig)

# ---------- Chart 4: Feedback sentiment buckets ----------

def classify_comment(row) -> str:
    # Very simple rule-based sentiment + rating combo
    txt = (row.get("comments") or "").lower()
    r = row.get("rating", 0)

    positive_words = ["good", "great", "amazing", "nice", "helpful", "love"]
    negative_words = ["bad", "poor", "confusing", "worst", "hate"]

    if any(w in txt for w in positive_words) or r >= 4:
        return "Positive"
    if any(w in txt for w in negative_words) or r <= 2:
        return "Negative"
    return "Neutral"

def chart_feedback_categories(df, output_dir=OUTPUT_DIR):
    df = df.copy()
    df["category"] = df.apply(classify_comment, axis=1)
    counts = df["category"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(counts.index, counts.values)
    ax.set_title("Feedback Sentiment Categories")
    ax.set_xlabel("Category")
    ax.set_ylabel("Number of Responses")
    add_value_labels(ax)
    plt.tight_layout()
    fig.savefig(output_dir / "feedback_categories.png", dpi=200)
    plt.close(fig)

# ---------- Main ----------

def main():
    print("Loaded feedback from:", MEMORY_PATH)
    df = load_feedback()
    print(df[["qid", "query", "rating", "comments"]])

    chart_ratings_by_query(df)
    chart_rating_distribution(df)
    chart_overall_score(df)
    chart_feedback_categories(df)

    print(f"\n✅ All charts saved to: {OUTPUT_DIR.resolve()}")
    print("Files:")
    for p in sorted(OUTPUT_DIR.glob("*.png")):
        print(" -", p.name)

if __name__ == "__main__":
    main()
