from datetime import date, timedelta

from config import HABITS_FILE, PROGRESS_FILE
from storage import load_data, save_data
from utils import get_today, get_valid_date, print_line


def mark_completed():
    habits = load_data(HABITS_FILE)
    progress = load_data(PROGRESS_FILE)

    if not habits:
        print("Add habits first.")
        return

    print("\nAVAILABLE HABITS")

    for habit in habits:
        print(
            f"{habit['id']}. {habit['name']} "
            f"({habit['frequency']})"
        )

    try:
        habit_id = int(input("\nEnter habit ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    habit = next(
        (item for item in habits if item["id"] == habit_id),
        None
    )

    if not habit:
        print("Habit not found.")
        return

    completion_date = get_valid_date(
        "Enter completion date (YYYY-MM-DD): "
    )

    selected_date = date.fromisoformat(completion_date)

    if selected_date > date.today():
        print("Future completion dates are not allowed.")
        return

    existing = next(
        (
            item for item in progress
            if item["habit_id"] == habit_id
            and item["date"] == completion_date
        ),
        None
    )

    if existing:
        print("This habit is already completed on this date.")
        return

    record = {
        "habit_id": habit_id,
        "date": completion_date,
        "status": "Completed"
    }

    progress.append(record)
    save_data(PROGRESS_FILE, progress)

    print(f"'{habit['name']}' marked as completed!")


def view_daily_progress():
    habits = load_data(HABITS_FILE)
    progress = load_data(PROGRESS_FILE)

    today = get_today()

    print_line()
    print(f"DAILY PROGRESS - {today}")
    print_line()

    if not habits:
        print("No habits available.")
        return

    completed_ids = {
        item["habit_id"]
        for item in progress
        if item["date"] == today
    }

    completed = 0

    for habit in habits:
        status = (
            "Completed"
            if habit["id"] in completed_ids
            else "Pending"
        )

        if status == "Completed":
            completed += 1

        print(f"{habit['name']} - {status}")

    percentage = (completed / len(habits)) * 100

    print_line()
    print(f"Completed: {completed}/{len(habits)}")
    print(f"Progress: {percentage:.1f}%")


def view_pending_habits():
    habits = load_data(HABITS_FILE)
    progress = load_data(PROGRESS_FILE)

    today = get_today()

    completed_ids = {
        item["habit_id"]
        for item in progress
        if item["date"] == today
    }

    pending = [
        habit for habit in habits
        if habit["id"] not in completed_ids
    ]

    print_line()
    print("PENDING HABITS")
    print_line()

    if not pending:
        print("All habits completed!")
        return

    for habit in pending:
        print(f"{habit['id']}. {habit['name']}")
