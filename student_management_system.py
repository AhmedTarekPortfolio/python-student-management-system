"""A command-line student and grade manager for Python fundamentals practice."""

from __future__ import annotations

from copy import deepcopy
from typing import TypeAlias

Grades: TypeAlias = dict[str, int]
Students: TypeAlias = dict[str, Grades]

SAMPLE_STUDENTS: Students = {
    "Ahmed": {"Math": 80, "English": 90, "Python": 75},
    "Sara": {"Math": 95, "English": 88, "Python": 92},
    "Omar": {"Math": 90, "English": 95, "Python": 85},
}


def normalize_name(value: str) -> str:
    """Trim repeated spaces and capitalize each word."""
    return " ".join(value.split()).title()


def find_student(students: Students, name: str) -> str | None:
    """Find a student without requiring matching letter case."""
    target = normalize_name(name).casefold()
    return next((student for student in students if student.casefold() == target), None)


def add_student(students: Students, name: str) -> bool:
    """Add a non-empty, non-duplicate student."""
    normalized = normalize_name(name)
    if not normalized or find_student(students, normalized):
        return False
    students[normalized] = {}
    return True


def set_grade(students: Students, name: str, subject: str, grade: int) -> bool:
    """Add or update a subject grade between 0 and 100."""
    student = find_student(students, name)
    normalized_subject = normalize_name(subject)
    if student is None or not normalized_subject or not 0 <= grade <= 100:
        return False
    existing_subject = next((key for key in students[student] if key.casefold() == normalized_subject.casefold()), normalized_subject)
    students[student][existing_subject] = grade
    return True


def average(grades: Grades) -> float | None:
    """Return a student's average, or None when no grades exist."""
    return sum(grades.values()) / len(grades) if grades else None


def result(grades: Grades) -> str:
    """Return Passed, Failed, or No grades using a 50-point pass mark."""
    value = average(grades)
    if value is None:
        return "No grades"
    return "Passed" if value >= 50 else "Failed"


def class_summary(students: Students) -> dict[str, object] | None:
    """Calculate class totals while excluding students without grades."""
    ranked = [(name, average(grades)) for name, grades in students.items() if grades]
    if not ranked:
        return None
    typed_ranked = [(name, float(value)) for name, value in ranked if value is not None]
    best = max(typed_ranked, key=lambda item: item[1])
    worst = min(typed_ranked, key=lambda item: item[1])
    passed = sum(value >= 50 for _, value in typed_ranked)
    return {
        "best": best, "worst": worst, "passed": passed,
        "failed": len(typed_ranked) - passed,
        "class_average": sum(value for _, value in typed_ranked) / len(typed_ranked),
        "students_with_grades": len(typed_ranked),
    }


def show_student(name: str, grades: Grades) -> None:
    print(f"\nStudent: {name}")
    if not grades:
        print("No grades yet.")
        return
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    print(f"Average: {average(grades):.2f}")
    print(f"Status: {result(grades)}")


def read_grade() -> int:
    while True:
        try:
            value = int(input("Grade (0-100): "))
            if not 0 <= value <= 100:
                raise ValueError
            return value
        except ValueError:
            print("Enter a whole number from 0 to 100.")


def main() -> None:
    """Run the interactive student management menu."""
    students = deepcopy(SAMPLE_STUDENTS)
    menu = "\n1. Show all students\n2. Search for a student\n3. Add a student\n4. Add or update a grade\n5. Class summary\n6. Exit"
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            if not students:
                print("No students available.")
            for name, grades in students.items():
                show_student(name, grades)
        elif choice == "2":
            name = find_student(students, input("Student name: "))
            if name is None:
                print("Student not found.")
            else:
                show_student(name, students[name])
        elif choice == "3":
            print("Student added." if add_student(students, input("Student name: ")) else "Name is empty or already exists.")
        elif choice == "4":
            name = input("Student name: ")
            subject = input("Subject name: ")
            print("Grade saved." if set_grade(students, name, subject, read_grade()) else "Student or subject was not valid.")
        elif choice == "5":
            summary = class_summary(students)
            if summary is None:
                print("No grades available yet.")
            else:
                print(f"Best student: {summary['best'][0]} - {summary['best'][1]:.2f}")
                print(f"Worst student: {summary['worst'][0]} - {summary['worst'][1]:.2f}")
                print(f"Passed: {summary['passed']} | Failed: {summary['failed']}")
                print(f"Class average: {summary['class_average']:.2f}")
        elif choice == "6":
            print("Goodbye.")
            return
        else:
            print("Choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
