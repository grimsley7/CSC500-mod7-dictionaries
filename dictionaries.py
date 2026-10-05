# Course Information System
# This program uses multiple dictionaries to look up course details.

# Dictionary for room numbers
room_numbers = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

# Dictionary for instructors
instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

# Dictionary for meeting times
meeting_times = {
    "CSC101": "Monday at 9:15 AM",
    "CSC102": "Tuesday at 10:00 AM",
    "CSC103": "Thursday at 1:30 PM",
    "NET110": "Wednesday at 8:00 AM",
    "COM241": "Monday at 9:00 AM"
}


def show_course(course_number):
    """Display one course."""
    print("\nCourse Information")
    print("Course Number:", course_number)
    print("Room Number:", room_numbers[course_number])
    print("Instructor:", instructors[course_number])
    print("Meeting Time:", meeting_times[course_number])


def search_by_instructor(instructor_name):
    """Display all courses taught by an instructor using full or partial name search."""
    found = False
    search_name = instructor_name.lower()

    print(f"\nCourses matching instructor search '{instructor_name}':")

    for course in instructors:
        if search_name in instructors[course].lower():
            print(f"{course} | Room: {room_numbers[course]} | Time: {meeting_times[course]}")
            found = True

    if not found:
        print("No courses found for that instructor.")


def get_time_block(time_text):
    """
    Return the hour block from a time string.
    Example: 'Monday at 9:15 AM' becomes '9 AM'
    Example: '9:00 AM' becomes '9 AM'
    """
    if "at" in time_text:
        time_text = time_text.split("at")[1].strip()

    parts = time_text.upper().split()
    hour = parts[0].split(":")[0]
    period = parts[1]
    return f"{hour} {period}"


def search_by_time(search_time):
    """Display all courses that meet during the requested hour block."""
    found = False
    search_block = get_time_block(search_time)

    print(f"\nCourses in the {search_block} time block:")

    for course in meeting_times:
        if get_time_block(meeting_times[course]) == search_block:
            print(f"{course} | Instructor: {instructors[course]} | Room: {room_numbers[course]} | Time: {meeting_times[course]}")
            found = True

    if not found:
        print("No courses found in that time block.")


def display_menu():
    """Display the menu options."""
    print("\nCourse Information System")
    print("1. Search by course number")
    print("2. Search by instructor")
    print("3. Search by time block")
    print("4. Quit")


def main():
    """Run the course information system."""
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            course_number = input("Enter a course number: ").strip().upper()

            if course_number in room_numbers:
                show_course(course_number)
            else:
                print("\nSorry, that course number was not found.")

        elif choice == "2":
            instructor_name = input("Enter an instructor name: ").strip()
            search_by_instructor(instructor_name)

        elif choice == "3":
            search_time = input("Enter a time block (example: 9:00 AM): ").strip()
            search_by_time(search_time)

        elif choice == "4":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
