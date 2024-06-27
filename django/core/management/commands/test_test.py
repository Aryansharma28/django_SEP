from django.test import TestCase
from django.core.management import call_command
from io import StringIO
from unittest.mock import patch

class CommandHandleTestCase(TestCase):
    @patch("sys.exit")
    def test_handle_with_failures(self, mock_exit):
        out = StringIO()
        with patch("django.test.runner.TestRunner.run_tests") as mock_run_tests:
            mock_run_tests.return_value = 2  # Simulate test failures
            call_command("test", stdout=out)
        self.assertEqual(mock_exit.call_args[0][0], 1)
        self.assertIn("Total run", out.getvalue())

    @patch("sys.exit")
    def test_handle_without_failures(self, mock_exit):
        out = StringIO()
        with patch("django.test.runner.TestRunner.run_tests") as mock_run_tests:
            mock_run_tests.return_value = 0  # Simulate no test failures
            call_command("test", stdout=out)
        self.assertEqual(mock_exit.call_args[0][0], 0)
        self.assertIn("Total run", out.getvalue())