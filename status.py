from storage import load_complaints, save_complaints


def update_status():
    complaints = load_complaints()

    if not complaints:
        print("\nNo complaints found.")
        return

    complaint_id = input("\nEnter Complaint ID: ").strip().upper()

    for complaint in complaints:

        if complaint["id"] == complaint_id:

            print("\nComplaint Found")
            print(f"Student : {complaint['student']}")
            print(f"Room    : {complaint['room']}")
            print(f"Current Status : {complaint['status']}")

            print("\nChoose New Status:")
            print("1. Pending")
            print("2. In Progress")
            print("3. Resolved")

            choice = input("Enter your choice: ").strip()

            status_map = {
                "1": "Pending",
                "2": "In Progress",
                "3": "Resolved"
            }

            if choice not in status_map:
                print("\nInvalid status option.")
                return

            new_status = status_map[choice]

            # Prevent unnecessary update
            if complaint["status"] == new_status:
                print("\nComplaint is already in this status.")
                return

            complaint["status"] = new_status

            save_complaints(complaints)

            print("\nComplaint status updated successfully!")
            print(f"Complaint ID : {complaint_id}")
            print(f"New Status   : {new_status}")

            return

    print("\nComplaint ID not found.")