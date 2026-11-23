from datetime import date, timedelta

from config import HABITS_FILE, PROGRESS_FILE
from storage import load_data
from utils import print_line


def calculate_streak(habit_id, progress):
    completed_dates = {
        date.fromisoformat(item["date"])
        for item in progress
        if item["habit_id"] == habit_id
    }

    if not completed_dates:
        return 0, 0

    today = date.today()

    current = 0
    check_date = today

    while check_date in completed_dates:
        current += 1
        check_date -= timedelta(days=1)

    if current == 0 and today - timedelta(days=1) in completed_dates:
        check_date = today - timedelta(days=1)

        while check_date in completed_dates:
            current += 1
            check_date -= timedelta(days=1)

    longest = 0
    streak = 0
    previous = None

    for completed_date in sorted(completed_dates):
        if previous is not None and (
            completed_date - previous
        ).days == 1:
            streak += 1
        else:
            streak = 1

        longest = max(longest, streak)
        previous = completed_date

    return current, longest


def habit_statistics():
    habits = load_data(HABITS_FILE)
    progress = load_data(PROGRESS_FILE)

    print_line()
    print("HABIT STATISTICS")
    print_line()

    if not habits:
        print("No habits found.")
        return

    for habit in habits:
        records = [
            item for item in progress
            if item["habit_id"] == habit["id"]
        ]

        current, longest = calculate_streak(
            habit["id"], progress
        )

        print(f"\nHabit: {habit['name']}")
        print(f"Frequency: {habit['frequency']}")
        print(f"Total completions: {len(records)}")
        print(f"Current streak: {current} days")
        print(f"Longest streak: {longest} days")


def weekly_report():
    habits = load_data(HABITS_FILE)
    progress = load_data(PROGRESS_FILE)

    today = date.today()
    start_date = today - timedelta(days=6)

    print_line()
    print("LAST 7 DAYS REPORT")
    print_line()

    for habit in habits:
        count = sum(
            1 for item in progress
            if item["habit_id"] == habit["id"]
            and start_date <= date.fromisoformat(item["date"]) <= today
        )

        print(
            f"{habit['name']}: "
            f"{count} completions in the last 7 days"
        )


def monthly_report():
    habits = load_data(HABITS_FILE)
    progress = load_data(PROGRESS_FILE)

    today = date.today()

    print_line()
    print(f"MONTHLY REPORT - {today.strftime('%B %Y')}")
    print_line()

    for habit in habits:
        count = sum(
            1 for item in progress
            if item["habit_id"] == habit["id"]
            and date.fromisoformat(item["date"]).year == today.year
            and date.fromisoformat(item["date"]).month == today.month
        )

        print(f"{habit['name']}: {count} completions this month")
