from devtrack.tasks import (
    load_tasks,
    save_tasks,
    add_task,
    list_tasks,
    remove_task,
    get_task_description,
    TASKS_FILE,
)
from pathlib import Path
from unittest.mock import mock_open, patch, call
import json, pytest
from devtrack import tasks


@patch.object(Path, "exists", return_value=False)
def test_load_tasks_file_not_exists(mock_exists):
    assert load_tasks() == []


@patch.object(Path, "exists", return_value=True)
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"id": 1, "description": "Test"}]',
)
def test_load_tasks_valid(mock_open_file, mock_exists):
    tasks = load_tasks()
    assert tasks == [{"id": 1, "description": "Test"}]


@patch.object(Path, "exists", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="{ bad json }")
def test_load_tasks_invalid_json(mock_open_file, mock_exists, capsys):
    tasks = load_tasks()
    captured = capsys.readouterr()
    assert tasks == []
    assert "corrupted" in captured.out


@patch("builtins.open", new_callable=mock_open)
def test_save_tasks(mock_open_file):
    tasks = [{"id": 1, "description": "Test task"}]

    # Call the function
    save_tasks(tasks)

    # ✅ Match the actual TASKS_FILE object (Path)
    mock_open_file.assert_called_once_with(TASKS_FILE, "w", encoding="utf-8")

    handle = mock_open_file()
    written = "".join(call.args[0] for call in handle.write.call_args_list)

    expected = json.dumps(tasks, indent=2)
    assert written == expected


@patch("devtrack.tasks.save_tasks")
@patch("devtrack.tasks.load_tasks", return_value=[])
def test_add_task(mock_load, mock_save, capsys):
    add_task("New Task")
    mock_save.assert_called_once()
    captured = capsys.readouterr()
    assert "Task added" in captured.out


@patch("devtrack.tasks.load_tasks", return_value=[])
def test_list_tasks_empty(mock_load_tasks, capsys):
    list_tasks()
    captured = capsys.readouterr()
    assert "No tasks" in captured.out


@patch(
    "devtrack.tasks.load_tasks",
    return_value=[{"id": 1, "description": "Do A"}, {"id": 2, "description": "Do B"}],
)
def test_list_tasks_multiple(mock_load_tasks, capsys):
    list_tasks()
    captured = capsys.readouterr()
    assert "Do A" in captured.out
    assert "Do B" in captured.out


@patch("devtrack.tasks.save_tasks")
@patch(
    "devtrack.tasks.load_tasks",
    return_value=[{"id": 1, "description": "Keep"}, {"id": 2, "description": "Delete"}],
)
def test_remove_task_found(mock_load, mock_save, capsys):
    remove_task(2)
    mock_save.assert_called_once()
    captured = capsys.readouterr()
    assert "removed" in captured.out


@patch("devtrack.tasks.save_tasks")
@patch(
    "devtrack.tasks.load_tasks", return_value=[{"id": 1, "description": "Only Task"}]
)
def test_remove_task_not_found(mock_load, mock_save, capsys):
    remove_task(5)
    mock_save.assert_not_called()
    captured = capsys.readouterr()
    assert "not found" in captured.out


@patch(
    "devtrack.tasks.load_tasks",
    return_value=[
        {"id": 1, "description": "Fix bug"},
        {"id": 2, "description": "Add feature"},
    ],
)
def test_get_task_description_found(mock_load):
    desc = get_task_description(2)
    assert desc == "Add feature"


@patch("devtrack.tasks.load_tasks", return_value=[])
def test_get_task_description_not_found(mock_load):
    assert get_task_description(99) is None


MOCK_TASKS = [
    {"id": 1, "description": "First Task", "completed": False},
    {"id": 2, "description": "Second Task", "completed": False},
]


@pytest.fixture
def mock_load_save():
    with patch("devtrack.tasks.load_tasks", return_value=MOCK_TASKS.copy()), patch(
        "devtrack.tasks.save_tasks"
    ) as mock_save:
        yield mock_save


def test_mark_task_done_success(mock_load_save, capsys):
    tasks.mark_task_done(1)
    captured = capsys.readouterr()
    assert "marked as completed" in captured.out
    mock_load_save.assert_called_once()
    assert MOCK_TASKS[0]["completed"] is True


def test_mark_task_done_not_found(mock_load_save, capsys):
    tasks.mark_task_done(99)
    captured = capsys.readouterr()
    assert "not found" in captured.out


def test_summary_tasks_output(capsys):
    with patch(
        "devtrack.tasks.load_tasks",
        return_value=[
            {"id": 1, "description": "Done Task", "completed": True},
            {"id": 2, "description": "Pending Task", "completed": False},
        ],
    ):
        tasks.summary_tasks()
        captured = capsys.readouterr()
        assert "✅  Completed Tasks:" in captured.out
        assert "[1] Done Task" in captured.out
        assert "🕐 Pending Tasks:" in captured.out
        assert "[2] Pending Task" in captured.out


def test_summary_tasks_no_tasks(capsys):
    with patch("devtrack.tasks.load_tasks", return_value=[]):
        tasks.summary_tasks()
        captured = capsys.readouterr()
        assert "No tasks found" in captured.out
