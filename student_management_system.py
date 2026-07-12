# Project: Student Management System

students = {
    "Ahmed": {"Math": 80, "English": 90, "Python": 75},
    "Sara": {"Math": 95, "English": 88, "Python": 92},
    "Omar": {"Math": 90, "English": 95, "Python": 85},
}


while True:
    print()
    print("===== Student Management System =====")
    print("1. Show all students")
    print("2. Search for a student")
    print("3. Add a new student")
    print("4. Add/update a grade")
    print("5. Show class summary")
    print("6. Exit")

    try:
        option = int(input("Choose an option from the list: "))
        print()

        if option == 1:
            print("===== All Students =====")

            for student, subjects in students.items():
                print()
                print(f"Student: {student}")

                if len(subjects) == 0:
                    print("No grades yet.")
                    continue

                for subject, grade in subjects.items():
                    print(f"{subject}: {grade}")

                avg = sum(subjects.values()) / len(subjects)

                if avg >= 50:
                    status = "Passed"
                else:
                    status = "Failed"

                print(f"Average: {avg:.2f}")
                print(f"Status: {status}")

        elif option == 2:
            name = input("Enter student name: ").strip().capitalize()

            if name in students:
                print("=== Student Found ===")
                print()
                print(f"Student: {name}")

                if len(students[name]) == 0:
                    print("No grades yet.")
                    continue

                for subject, grade in students[name].items():
                    print(f"{subject}: {grade}")

                avg = sum(students[name].values()) / len(students[name])

                if avg >= 50:
                    status = "Passed"
                else:
                    status = "Failed"

                print(f"Average: {avg:.2f}")
                print(f"Status: {status}")
            else:
                print("Student not found.")

        elif option == 3:
            new_student = input("Enter new student: ").strip().capitalize()

            if new_student not in students:
                students[new_student] = {}
                print(f"Student {new_student} added successfully.")
            else:
                print("Student already exists.")

        elif option == 4:
            name = input("Enter student name: ").strip().capitalize()

            if name in students:
                subject = input("Enter subject name: ").strip().capitalize()
                new_grade = int(input("Enter grade: "))

                if new_grade < 0 or new_grade > 100:
                    print("Invalid grade. Grade must be from 0 to 100.")
                    continue

                if subject in students[name]:
                    students[name][subject] = new_grade
                    print("Subject updated.")
                else:
                    students[name][subject] = new_grade
                    print("Subject added.")
            else:
                print("Student not found.")

        elif option == 5:
            print("=== Class Summary ===")

            best_student = ""
            highest = None
            worst_student = ""
            lowest = None
            passed = 0
            failed = 0
            total = 0
            students_with_grades = 0

            for student, subjects in students.items():
                if len(subjects) == 0:
                    continue

                avg = sum(subjects.values()) / len(subjects)
                total += avg
                students_with_grades += 1

                if highest is None or avg > highest:
                    highest = avg
                    best_student = student

                if lowest is None or avg < lowest:
                    lowest = avg
                    worst_student = student

                if avg >= 50:
                    passed += 1
                else:
                    failed += 1

            if students_with_grades == 0:
                print("No grades available yet.")
            else:
                class_avg = total / students_with_grades
                print()
                print(f"Best student: {best_student} - {highest:.2f}")
                print(f"Worst student: {worst_student} - {lowest:.2f}")
                print(f"Passed students: {passed}")
                print(f"Failed students: {failed}")
                print(f"Class average: {class_avg:.2f}")

        elif option == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose from 1 to 6.")

    except ValueError:
        print("Please enter a valid number.")
