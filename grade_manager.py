"""Student Grade Manager"""

# Storage choice: a list of dictionaries.
# Each student is a separate record, so duplicate names are allowed.
# Example entry: {"name": "Priya", "mark": 92, "grade": "A"}


def get_grade(mark):
    """Return the letter grade for a mark between 0 and 100."""
    if 90 <= mark <= 100:
        return "A"
    if 80 <= mark <= 89:
        return "B"
    if 70 <= mark <= 79:
        return "C"
    if 60 <= mark <= 69:
        return "D"
    return "E"


def validate_mark(raw_value):
    """Validate that the raw input is an integer between 0 and 100."""
    try:
        mark = int(raw_value)
    except ValueError:
        raise ValueError("Mark must be a number.") from None

    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")

    return mark


def add_student(students):
    """Prompt the user to add one student and validate mark input."""
    while True:
        name = input("Enter student name (or 'cancel' to go back): ").strip()
        if name.lower() == "cancel":
            print("Cancelled student entry.")
            return
        if not name:
            print("Name cannot be empty. Please try again.")
            continue
        break

    while True:
        raw_value = input(f"Enter mark for {name}: ").strip()
        if raw_value.lower() == "cancel":
            print("Cancelled student entry.")
            return

        try:
            mark = validate_mark(raw_value)
        except ValueError as exc:
            print(f"Invalid input: {exc} Please enter a whole number from 0 to 100.")
            continue

        student = {"name": name, "mark": mark, "grade": get_grade(mark)}
        students.append(student)
        print(f"Added {name} with mark {mark} ({student['grade']}).")
        return


def show_results(students):
    """Display grades in a table and summary statistics."""
    if not students:
        print("No students added yet.")
        return

    print(f"{'Name':<12}{'Mark':>6}{'Grade':>8}")
    for student in students:
        print(f"{student['name']:<12}{student['mark']:>6}{student['grade']:>8}")

    average = sum(student["mark"] for student in students) / len(students)
    highest = max(student["mark"] for student in students)
    lowest = min(student["mark"] for student in students)

    print(f"Average: {average:.1f}    Highest: {highest}    Lowest: {lowest}")


def main():
    """Run the menu loop for the Student Grade Manager."""
    students = []

    while True:
        print("\nStudent Grade Manager")
        print("1. Add student")
        print("2. Show results")
        print("3. Quit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_results(students)
        elif choice in {"3", "q", "quit", "exit"}:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
