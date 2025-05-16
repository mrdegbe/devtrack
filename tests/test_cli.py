import unittest
from unittest.mock import patch
from devtrack import cli


class TestCLI(unittest.TestCase):

    @patch("builtins.print")
    def test_help_command(self, mock_print):
        with patch("sys.argv", ["devtrack", "help"]):
            cli.main()
        mock_print.assert_any_call("""
Usage: devtrack <command> [options]

Available commands:
  commit <task_id>     Generate a Git commit message for the given task ID.
  tasks                List all tasks.
  add <description>    Add a new task with the provided description.
  remove <task_id>     Remove a task by its ID.
  help                 Show this help message.
""")

    @patch("devtrack.tasks.add_task")
    def test_add_command(self, mock_add_task):
        with patch("sys.argv", ["devtrack", "add", "Fix", "login", "bug"]):
            cli.main()
        mock_add_task.assert_called_once_with("Fix login bug")

    @patch("builtins.print")
    def test_add_missing_description(self, mock_print):
        with patch("sys.argv", ["devtrack", "add"]):
            cli.main()
        mock_print.assert_called_with("[!] Usage: devtrack add <task description>")

    @patch("devtrack.tasks.list_tasks")
    def test_tasks_command(self, mock_list_tasks):
        with patch("sys.argv", ["devtrack", "tasks"]):
            cli.main()
        mock_list_tasks.assert_called_once()

    @patch("devtrack.tasks.remove_task")
    def test_remove_command(self, mock_remove_task):
        with patch("sys.argv", ["devtrack", "remove", "2"]):
            cli.main()
        mock_remove_task.assert_called_once_with(2)

    @patch("builtins.print")
    def test_remove_missing_id(self, mock_print):
        with patch("sys.argv", ["devtrack", "remove"]):
            cli.main()
        mock_print.assert_called_with("[!] Usage: devtrack remove <task_id>")

    @patch("builtins.print")
    def test_remove_invalid_id(self, mock_print):
        with patch("sys.argv", ["devtrack", "remove", "abc"]):
            cli.main()
        mock_print.assert_called_with("[!] Task ID must be an integer.")

    @patch("devtrack.commits.generate_commit")
    def test_commit_command(self, mock_generate_commit):
        with patch("sys.argv", ["devtrack", "commit", "1"]):
            cli.main()
        mock_generate_commit.assert_called_once_with(1)

    @patch("builtins.print")
    def test_commit_missing_id(self, mock_print):
        with patch("sys.argv", ["devtrack", "commit"]):
            cli.main()
        mock_print.assert_called_with("[!] Usage: devtrack commit <task_id>")

    @patch("builtins.print")
    def test_commit_invalid_id(self, mock_print):
        with patch("sys.argv", ["devtrack", "commit", "xyz"]):
            cli.main()
        mock_print.assert_called_with("[!] Task ID must be an integer.")

    @patch("builtins.print")
    def test_unknown_command(self, mock_print):
        with patch("sys.argv", ["devtrack", "unknown"]):
            cli.main()
        mock_print.assert_any_call("[!] Unknown command: unknown")


if __name__ == "__main__":
    unittest.main()


# import unittest
# from unittest.mock import patch
# from devtrack import cli
#
# class TestCLI(unittest.TestCase):
#
#     @patch("builtins.print")
#     def test_help_command(self, mock_print):
#         with patch("sys.argv", ["devtrack", "help"]):
#             cli.main()
#         mock_print.assert_any_call("""
# Usage: devtrack <command> [options]
#
# Available commands:
#   commit <task_id>     Generate a Git commit message for the given task ID.
#   tasks                List all tasks.
#   add <description>    Add a new task with the provided description.
#   remove <task_id>     Remove a task by its ID.
#   help                 Show this help message.
# """)
#
#     @patch("devtrack.tasks.add_task")
#     def test_add_command(self, mock_add_task):
#         with patch("sys.argv", ["devtrack", "add", "Fix", "login", "bug"]):
#             cli.main()
#         mock_add_task.assert_called_once_with("Fix login bug")
#
#     @patch("devtrack.tasks.list_tasks")
#     def test_tasks_command(self, mock_list_tasks):
#         with patch("sys.argv", ["devtrack", "tasks"]):
#             cli.main()
#         mock_list_tasks.assert_called_once()
#
#     @patch("devtrack.tasks.remove_task")
#     def test_remove_command(self, mock_remove_task):
#         with patch("sys.argv", ["devtrack", "remove", "2"]):
#             cli.main()
#         mock_remove_task.assert_called_once_with(2)
#
#     @patch("devtrack.commits.generate_commit")
#     def test_commit_command(self, mock_generate_commit):
#         with patch("sys.argv", ["devtrack", "commit", "1"]):
#             cli.main()
#         mock_generate_commit.assert_called_once_with(1)
#
#     @patch("builtins.print")
#     def test_unknown_command(self, mock_print):
#         with patch("sys.argv", ["devtrack", "unknown"]):
#             cli.main()
#         mock_print.assert_any_call("[!] Unknown command: unknown")
#
# if __name__ == "__main__":
#     unittest.main()
