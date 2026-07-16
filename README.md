# Python Student Management System

A menu-driven command-line learning project for managing students, subject grades, individual results, and class summaries.

## Features

- Display all students and grades
- Search consistently without case-sensitive name matching
- Reject empty and duplicate student names
- Add or update subject grades from 0 to 100
- Handle students with no grades safely
- Calculate averages and pass/fail results
- Report class average, best/worst student, and pass/fail counts

## Run

Requires Python 3.10 or newer and no external packages.

```bash
python student_management_system.py
```

## Test

```bash
python -m unittest discover -s tests -v
```

## Example session

```text
1. Show all students
2. Search for a student
3. Add a student
4. Add or update a grade
5. Class summary
6. Exit
Choose an option: 2
Student name: ahmed
Student: Ahmed
Math: 80
English: 90
Python: 75
Average: 81.67
Status: Passed
```

## Concepts practiced

Functions, nested dictionaries, type hints, loops, conditions, input validation, calculations, docstrings, and unit tests.

## Project status

Completed learning project. The program uses sample data in memory and is not a production school-record system.
