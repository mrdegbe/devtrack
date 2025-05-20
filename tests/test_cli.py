import sys
from unittest import mock
from devtrack import cli


# Mock the actual implementations so we can track if they're called
@mock.patch("devtrack.cli.generate_commit")
@mock.patch("builtins.print")
def test_commit_valid_id(mock_print, mock_generate_commit):
    test_args = ["devtrack", "commit", "2"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_generate_commit.assert_called_once_with(2)


@mock.patch("builtins.print")
def test_commit_missing_id(mock_print):
    test_args = ["devtrack", "commit"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_print.assert_any_call("[!] Usage: devtrack commit <task_id>")


@mock.patch("builtins.print")
def test_commit_invalid_id(mock_print):
    test_args = ["devtrack", "commit", "abc"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_print.assert_any_call("[!] Task ID must be an integer.")


@mock.patch("devtrack.cli.list_tasks")
@mock.patch("builtins.print")
def test_tasks(mock_print, mock_list_tasks):
    test_args = ["devtrack", "tasks"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_list_tasks.assert_called_once()


@mock.patch("devtrack.cli.add_task")
@mock.patch("builtins.print")
def test_add_valid_description(mock_print, mock_add_task):
    test_args = ["devtrack", "add", "Finish", "docs"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_add_task.assert_called_once_with("Finish docs")


@mock.patch("builtins.print")
def test_add_missing_description(mock_print):
    test_args = ["devtrack", "add"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_print.assert_any_call("[!] Usage: devtrack add <task description>")


@mock.patch("devtrack.cli.remove_task")
@mock.patch("builtins.print")
def test_remove_valid_id(mock_print, mock_remove_task):
    test_args = ["devtrack", "remove", "3"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_remove_task.assert_called_once_with(3)


@mock.patch("builtins.print")
def test_remove_missing_id(mock_print):
    test_args = ["devtrack", "remove"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_print.assert_any_call("[!] Usage: devtrack remove <task_id>")


@mock.patch("builtins.print")
def test_remove_invalid_id(mock_print):
    test_args = ["devtrack", "remove", "xyz"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_print.assert_any_call("[!] Task ID must be an integer.")


@mock.patch("builtins.print")
def test_help_command(mock_print):
    test_args = ["devtrack", "help"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_print.assert_any_call(
        """
Usage: devtrack <command> [options]

Available commands:
  init                 Configure DevTrack and set up your AI provider (runs once).
  commit <task_id>     Generate a Git commit message for the given task ID.
  tasks                List all tasks.
  add <description>    Add a new task with the provided description.
  remove <task_id>     Remove a task by its ID.
  help                 Show this help message.
"""
    )


@mock.patch("builtins.print")
def test_unknown_command(mock_print):
    test_args = ["devtrack", "launch"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_print.assert_any_call("[!] Unknown command: launch")
