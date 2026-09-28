from registration import register_complaint
from complaint import view_all_complaints
from search import search_complaint
from status import update_status
from statistics import show_statistics


def display_menu():
    print("\n" + "=" * 50)
    print("       HOSTEL COMPLAINT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Register Complaint")
    print("2. View All Complaints")
    print("3. Search Complaint")
    print("4. Update Complaint Status")
    print("5. Complaint Statistics")
    print("6. Exit")
    print("=" * 50)


def main():

    print("\nWelcome to Hostel Complaint Management System!")

    while True:

        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_complaint()

        elif choice == "2":
            view_all_complaints()

        elif choice == "3":
            search_complaint()

        elif choice == "4":
            update_status()

        elif choice == "5":
            show_statistics()

        elif choice == "6":
            print("\nThank you for using the system.")
            print("Program closed successfully.")
            break

        else:
            print("\nInvalid choice.")
            print("Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()