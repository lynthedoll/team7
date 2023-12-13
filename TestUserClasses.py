import unittest

class TestUserClasses(unittest.TestCase):
    def test_student_creation(self):
        student = Student("test_student", "test_password")
        self.assertEqual(student.username, "test_student")
        self.assertEqual(student.password, "test_password")

    def test_teacher_creation(self):
        teacher = Teacher("test_teacher", "test_password")
        self.assertEqual(teacher.username, "test_teacher")
        self.assertEqual(teacher.password, "test_password")

if __name__ == '__main__':
    unittest.main()
