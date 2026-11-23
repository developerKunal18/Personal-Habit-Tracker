from config import HABITS_FILE, PROGRESS_FILE
from storage import load_data, save_data
from utils import get_next_id, print_line


def add_habit():
    habits = load_data(HABITS_FILE)

    name = input("Enter habit name: ").strip()

    if not name:
        print("Habit name cannot be empty.")
        return

    if any(
        habit["name"].lower() == name.lower()
        for habit in habits
    ):
        print("This habit already exists.")
        return

    print("\nSelect frequency:")
    print("1. Daily")
    print("2. Weekly")

    frequency_choice = input("Enter choice: ").strip()

    if frequency_choice == "1":
        frequency = "Daily"
    elif frequency_choice == "2":
        frequency = "Weekly"
    else:
        print("Invalid frequency.")
        return

    habit = {
        "id": get_next_id(habits),
        "name": name,
        "frequency": frequency,
        "created_at": __import__("datetime").date.today().isoformat()
    }

    habits.append(habit)
    save_data(HABITS_FILE, habits)

    print("Habit added successfully!")


def view_habits():
    habits = load_data(HABITS_FILE)

    print_line()
    print("MY HABITS")
    print_line()

    if not habits:
        print("No habits found.")
        return

    for habit in habits:
        print(
            f"ID: {habit['id']} | "
            f"Name: {habit['name']} | "
            f"Frequency: {habit['frequency']}"
        )


def delete_habit():
    habits = load_data(HABITS_FILE)
    progress = load_data(PROGRESS_FILE)

    try:
        habit_id = int(input("Enter habit ID to delete: "))
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

    confirm = input(
        f"Delete '{habit['name']}' and its progress history? (y/n): "
    ).strip().lower()

    if confirm != "y":
        print("Deletion cancelled.")
        return

    habits = [
        item for item in habits
        if item["id"] != habit_id
    ]

    progress = [
        item for item in progress
        if item["habit_id"] != habit_id
    ]

    save_data(HABITS_FILE, habits)
    save_data(PROGRESS_FILE, progress)

    print("Habit deleted successfully!")
