from complaint import generate_complaint_id
from storage import load_complaints, save_complaints
from validation import validate_complaint


def register_complaint():

    print("\n" + "=" * 50)
    print("             REGISTER COMPLAINT")
    print("=" * 50)

    student = input("Student Name: ").strip()
    room = input("Room Number: ").strip()

    print("\nComplaint Types:")
    print("1. Electrical")
    print("2. Plumbing")
    print("3. Cleaning")
    print("4. Furniture")
    print("5. Other")

    type_choice = input("Choose complaint type: ").strip()

    type_map = {
        "1": "Electrical",
        "2": "Plumbing",
        "3": "Cleaning",
        "4": "Furniture",
        "5": "Other"
    }

    if type_choice not in type_map:
        print("\nInvalid complaint type.")
        return

    complaint_type = type_map[type_choice]

    description = input("Description: ").strip()

    print("\nPriority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")

    priority_choice = input("Choose priority: ").strip()

    priority_map = {
        "1": "Low",
        "2": "Medium",
        "3": "High"
    }

    if priority_choice not in priority_map:
        print("\nInvalid priority.")
        return

    priority = priority_map[priority_choice]

    complaint = {
        "student": student,
        "room": room,
        "type": complaint_type,
        "description": description,
        "priority": priority,
        "status": "Pending"
    }

    # Validate complaint details
    if not validate_complaint(complaint):
        return

    # Load existing complaints
    complaints = load_complaints()

    # Generate a new complaint ID
    complaint["id"] = generate_complaint_id(complaints)

    # Add complaint to the list
    complaints.append(complaint)

    # Save updated complaints
    save_complaints(complaints)

    print("\n" + "=" * 50)
    print("Complaint registered successfully!")
    print("=" * 50)
    print(f"Complaint ID : {complaint['id']}")
    print(f"Type         : {complaint['type']}")
    print(f"Priority     : {complaint['priority']}")
    print(f"Status       : {complaint['status']}")
    print("=" * 50)