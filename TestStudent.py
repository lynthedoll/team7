import unittest
from unittest.mock import patch

class TestStudentApp(unittest.TestCase):
    @patch('builtins.input', return_value="test_student")
    def test_logout(self, mock_input):
        # Ensure the logout process works
        student_app = StudentApp(tk.Tk())
        with self.assertLogs(level='INFO') as log:
            student_app.logout()
        self.assertIn('Student app window closed', log.output)

if __name__ == '__main__':
    unittest.main()
