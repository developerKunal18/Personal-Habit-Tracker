import json
import os


def load_data(filename):
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []

    except (json.JSONDecodeError, OSError):
        return []


def save_data(filename, data):
    os.makedirs("data", exist_ok=True)

    temporary_file = filename + ".tmp"

    with open(temporary_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    os.replace(temporary_file, filename)
