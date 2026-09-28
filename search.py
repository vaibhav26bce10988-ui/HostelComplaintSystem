from storage import load_complaints


def display_complaint(complaint):
    print("\n" + "=" * 50)
    print(f"Complaint ID : {complaint['id']}")
    print(f"Student      : {complaint['student']}")
    print(f"Room         : {complaint['room']}")
    print(f"Type         : {complaint['type']}")
    print(f"Priority     : {complaint['priority']}")
    print(f"Status       : {complaint['status']}")
    print(f"Description  : {complaint['description']}")
    print("=" * 50)


def search_complaint():
    complaints = load_complaints()

    if not complaints:
        print("\nNo complaints found.")
        return

    print("\n--- Search Complaint ---")
    print("1. Complaint ID")
    print("2. Room Number")
    print("3. Complaint Type")
    print("4. Status")
    print("5. Priority")

    choice = input("Choose search type: ").strip()

    field_map = {
        "1": "id",
        "2": "room",
        "3": "type",
        "4": "status",
        "5": "priority"
    }

    if choice not in field_map:
        print("Invalid search option.")
        return

    value = input("Enter search value: ").strip().lower()

    field = field_map[choice]
    found = False

    for complaint in complaints:
        complaint_value = str(complaint[field]).lower()

        if value in complaint_value:
            display_complaint(complaint)
            found = True

    if not found:
        print("\nNo matching complaint found.")