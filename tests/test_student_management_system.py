import unittest

from student_management_system import add_student, average, class_summary, find_student, result, set_grade


class StudentTests(unittest.TestCase):
    def setUp(self):
        self.students = {"Ahmed Ali": {"Math": 80}, "No Grades": {}}

    def test_duplicate_and_empty_students_are_rejected(self):
        self.assertFalse(add_student(self.students, " ahmed   ali "))
        self.assertFalse(add_student(self.students, "  "))
        self.assertTrue(add_student(self.students, "Sara"))

    def test_search_is_case_insensitive(self):
        self.assertEqual(find_student(self.students, "AHMED ALI"), "Ahmed Ali")

    def test_grade_validation_and_update(self):
        self.assertFalse(set_grade(self.students, "Ahmed Ali", "Math", 101))
        self.assertTrue(set_grade(self.students, "ahmed ali", "math", 90))
        self.assertEqual(self.students["Ahmed Ali"]["Math"], 90)

    def test_empty_grade_handling(self):
        self.assertIsNone(average({}))
        self.assertEqual(result({}), "No grades")

    def test_summary_excludes_students_without_grades(self):
        self.students["Sara"] = {"Math": 40, "English": 60}
        summary = class_summary(self.students)
        self.assertEqual(summary["students_with_grades"], 2)
        self.assertEqual(summary["best"][0], "Ahmed Ali")
        self.assertEqual(summary["class_average"], 65.0)


if __name__ == "__main__":
    unittest.main()
