import sys, json, os
from unittest import mock
from devtrack import cli
from devtrack.session import get_active_task_id

ACTIVE_FILE = os.path.expanduser("~/.devtrack_active.json")


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
    # Updated to match new CLI usage with tag
    test_args = ["devtrack", "add", "Finish", "docs", "--tag", "writing"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    # Now add_task takes tag as second argument
    mock_add_task.assert_called_once_with("Finish docs", "writing")


@mock.patch("builtins.print")
def test_add_missing_description(mock_print):
    test_args = ["devtrack", "add"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_print.assert_any_call(
        "[!] Usage: devtrack add <task description> [--tag <tag>]"
    )


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

Available cmd:
  init                 Configure DevTrack and set up your AI provider (runs once).
  summary              List all tasks under Completed tasks and Pending tasks.
  status               Show current task, staged Git changes, and AI status.
  done <task_id>       Mark task as done by its ID.
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


@mock.patch("builtins.print")
@mock.patch("devtrack.tasks.load_tasks")
def test_focus_valid_task(mock_load_tasks, mock_print):
    # Set up a task list with ID 1 and 2
    mock_load_tasks.return_value = [
        {"id": 1, "description": "Task One", "completed": False},
        {"id": 2, "description": "Task Two", "completed": False},
    ]
    test_args = ["devtrack", "focus", "2"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()

    # Assert file was created with ID 2
    with open(ACTIVE_FILE) as f:
        data = json.load(f)
    assert data["active_task_id"] == 2
    mock_print.assert_any_call("🎯 Now focusing on task #2")


@mock.patch("builtins.print")
@mock.patch("devtrack.tasks.load_tasks")
def test_focus_nonexistent_task(mock_load_tasks, mock_print):
    mock_load_tasks.return_value = [{"id": 1, "description": "Only Task"}]
    test_args = ["devtrack", "focus", "5"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_print.assert_any_call("[!] No task found with ID 5")
    assert get_active_task_id() != 5


@mock.patch("builtins.print")
@mock.patch(
    "devtrack.status.set_active_task"
)  # or devtrack.tasks.set_active_task depending on location
@mock.patch("devtrack.tasks.load_tasks")
def test_focus_valid_task(mock_load_tasks, mock_set_active_task, mock_print):
    mock_load_tasks.return_value = [
        {"id": 1, "description": "Task One", "completed": False},
        {"id": 2, "description": "Task Two", "completed": False},
    ]
    test_args = ["devtrack", "focus", "2"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()

    # Ensure set_active_task was called with correct ID
    mock_set_active_task.assert_called_once_with(2)
    mock_print.assert_any_call("🎯 Now focusing on task #2")


@mock.patch("builtins.print")
def test_focus_missing_id(mock_print):
    test_args = ["devtrack", "focus"]
    with mock.patch.object(sys, "argv", test_args):
        cli.main()
    mock_print.assert_any_call("[!] Usage: devtrack focus <task_id>")


# def teardown_function():
#     if os.path.exists(ACTIVE_FILE):
#         os.remove(ACTIVE_FILE)
