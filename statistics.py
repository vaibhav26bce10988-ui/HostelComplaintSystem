from storage import load_complaints


def show_statistics():
    complaints = load_complaints()

    if not complaints:
        print("\nNo complaints available for statistics.")
        return

    total = len(complaints)
    pending = 0
    in_progress = 0
    resolved = 0
    type_counts = {}

    for complaint in complaints:

        # Count status
        if complaint["status"] == "Pending":
            pending += 1
        elif complaint["status"] == "In Progress":
            in_progress += 1
        elif complaint["status"] == "Resolved":
            resolved += 1

        # Count complaint types
        complaint_type = complaint["type"]

        if complaint_type in type_counts:
            type_counts[complaint_type] += 1
        else:
            type_counts[complaint_type] = 1

    # Calculate resolution percentage
    resolution_percentage = (resolved / total) * 100

    # Find most common complaint type
    most_common_type = ""
    highest_count = 0

    for complaint_type, count in type_counts.items():
        if count > highest_count:
            highest_count = count
            most_common_type = complaint_type

    print("\n" + "=" * 50)
    print("             COMPLAINT STATISTICS")
    print("=" * 50)

    print(f"Total Complaints    : {total}")
    print(f"Pending             : {pending}")
    print(f"In Progress         : {in_progress}")
    print(f"Resolved            : {resolved}")
    print(f"Resolution Rate     : {resolution_percentage:.1f}%")

    print("\nComplaints by Type:")

    for complaint_type, count in type_counts.items():
        print(f"{complaint_type:<20}: {count}")

    print(f"\nMost Common Type    : {most_common_type}")
    print(f"Number of Complaints: {highest_count}")
    print("=" * 50)