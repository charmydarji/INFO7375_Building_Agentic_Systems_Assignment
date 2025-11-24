# src/main.py
import sys
from src.crewai_research_crew import run_research_crew
from src.memory.memory_manager import append_feedback


def main():
    if len(sys.argv) < 2:
        print('Usage: python -m src.main "your research question here"')
        sys.exit(1)

    user_query = sys.argv[1]
    report = run_research_crew(user_query)

    print(report)

    try:
        rating_str = input(
            "\nOn a scale of 1–5, how would you rate the clarity and usefulness of this report? "
        )
        rating = int(rating_str.strip())
        comments = input(
            "Any comments or suggestions to improve future reports? "
        )
        append_feedback(user_query, rating, comments)
        print("Thanks! Your feedback was recorded.")
    except Exception:
        print("Feedback not recorded (invalid input).")


if __name__ == "__main__":
    main()
