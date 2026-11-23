from habit_manager import (
    add_habit,
    view_habits,
    delete_habit
)

from progress_manager import (
    mark_completed,
    view_daily_progress,
    view_pending_habits
)

from report_manager import (
    habit_statistics,
    weekly_report,
    monthly_report
)


def main():
    while True:
        print("\n====================================")
        print("       PERSONAL HABIT TRACKER")
        print("====================================")

        print("1. Add New Habit")
        print("2. View All Habits")
        print("3. Mark Habit Completed")
        print("4. View Daily Progress")
        print("5. View Pending Habits")
        print("6. View Habit Statistics")
        print("7. Weekly Report")
        print("8. Monthly Report")
        print("9. Delete Habit")
        print("10. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_habit()

        elif choice == "2":
            view_habits()

        elif choice == "3":
            mark_completed()

        elif choice == "4":
            view_daily_progress()

        elif choice == "5":
            view_pending_habits()

        elif choice == "6":
            habit_statistics()

        elif choice == "7":
            weekly_report()

        elif choice == "8":
            monthly_report()

        elif choice == "9":
            delete_habit()

        elif choice == "10":
            print("Thank you for using Personal Habit Tracker!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
