import unittest
from unittest.mock import patch

class TestLoginApp(unittest.TestCase):
    @patch('builtins.input', side_effect=["test_student", "test_password"])
    def test_successful_student_login(self, mock_input):
        # Ensure the login process works for a student
        login_app = LoginApp(tk.Tk())
        with self.assertLogs(level='INFO') as log:
            login_app.login()
        self.assertIn('Student login successful!', log.output)

    @patch('builtins.input', side_effect=["test_teacher", "test_password"])
    def test_successful_teacher_login(self, mock_input):
        # Ensure the login process works for a teacher
        login_app = LoginApp(tk.Tk())
        with self.assertLogs(level='INFO') as log:
            login_app.login()
        self.assertIn('Teacher login successful!', log.output)

if __name__ == '__main__':
    unittest.main()
