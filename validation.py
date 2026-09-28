VALID_TYPES = ["Electrical", "Plumbing", "Cleaning", "Furniture", "Other"]
VALID_PRIORITIES = ["Low", "Medium", "High"]


def validate_complaint(complaint):

    # Check student name
    if not complaint["student"]:
        print("Student name cannot be empty.")
        return False

    # Check room number
    if not complaint["room"]:
        print("Room number cannot be empty.")
        return False

    # Check complaint type
    if complaint["type"] not in VALID_TYPES:
        print("Invalid complaint type.")
        print("Choose: Electrical, Plumbing, Cleaning, Furniture or Other.")
        return False

    # Check description
    if not complaint["description"]:
        print("Complaint description cannot be empty.")
        return False

    # Check priority
    if complaint["priority"] not in VALID_PRIORITIES:
        print("Invalid priority.")
        print("Choose: Low, Medium or High.")
        return False

    return True