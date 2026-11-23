from datetime import date


def get_next_id(records):
    if not records:
        return 1

    return max(record["id"] for record in records) + 1


def get_today():
    return date.today().isoformat()


def get_valid_date(message):
    while True:
        value = input(message).strip()

        try:
            return date.fromisoformat(value).isoformat()
        except ValueError:
            print("Enter date in YYYY-MM-DD format.")


def print_line():
    print("-" * 55)
