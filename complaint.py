from storage import load_complaints


def generate_complaint_id(complaints):
    """Generate a unique complaint ID."""
    if not complaints:
        return "C001"

    highest_number = 0

    for complaint in complaints:
        complaint_id = complaint.get("id", "")

        if complaint_id.startswith("C"):
            try:
                number = int(complaint_id[1:])

                if number > highest_number:
                    highest_number = number

            except ValueError:
                pass

    return f"C{highest_number + 1:03d}"


def view_all_complaints():
    complaints = load_complaints()

    if not complaints:
        print("\nNo complaints found.")
        return

    print("\n" + "=" * 50)
    print("             ALL COMPLAINTS")
    print("=" * 50)

    for complaint in complaints:
        print(f"Complaint ID : {complaint['id']}")
        print(f"Student      : {complaint['student']}")
        print(f"Room         : {complaint['room']}")
        print(f"Type         : {complaint['type']}")
        print(f"Priority     : {complaint['priority']}")
        print(f"Status       : {complaint['status']}")
        print(f"Description  : {complaint['description']}")
        print("-" * 50)