import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "data" / "complaints.json"

def load_complaints():
    if not DATA_FILE.exists():
        return []

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []

def save_complaints(complaints):
    DATA_FILE.parent.mkdir(exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(complaints, file, indent=4)
