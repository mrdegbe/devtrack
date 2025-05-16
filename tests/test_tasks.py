import os
import tempfile
import pytest
from devtrack import tasks as task_module

@pytest.fixture
def temp_task_file():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        yield tmp.name
    os.remove(tmp.name)

@pytest.fixture
def mock_tasks():
    return [
        {"id": 1, "description": "First task"},
        {"id": 2, "description": "Second task"},
    ]

def test_add_task(monkeypatch, temp_task_file):
    monkeypatch.setattr(task_module, "TASKS_FILE", temp_task_file)
    monkeypatch.setattr(task_module, "load_tasks", lambda: [])
    added = []

    def mock_save(tasks, file):
        added.extend(tasks)

    monkeypatch.setattr(task_module, "save_tasks", mock_save)
    task_module.add_task("Write test cases")

    assert len(added) == 1
    assert added[0]["description"] == "Write test cases"
    assert added[0]["id"] == 1

def test_remove_task(monkeypatch, temp_task_file, mock_tasks):
    monkeypatch.setattr(task_module, "TASKS_FILE", temp_task_file)
    monkeypatch.setattr(task_module, "load_tasks", lambda: mock_tasks)
    removed = []

    def mock_save(tasks, file):
        removed.extend(tasks)

    monkeypatch.setattr(task_module, "save_tasks", mock_save)
    task_module.remove_task(1)

    assert len(removed) == 1
    assert removed[0]["id"] == 2

def test_list_tasks(monkeypatch, capsys, mock_tasks):
    monkeypatch.setattr(task_module, "load_tasks", lambda: mock_tasks)
    task_module.list_tasks()
    out = capsys.readouterr().out
    assert "1. First task" in out
    assert "2. Second task" in out


# import unittest
# from unittest.mock import mock_open, patch
# import json
# from devtrack import tasks
#
# mock_tasks_data = [
#     {"id": 1, "description": "Initial task"},
#     {"id": 2, "description": "Second task"}
# ]
#
# class TestTasks(unittest.TestCase):
#
#     @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_tasks_data))
#     def test_list_tasks(self, mock_file):
#         with patch("builtins.print") as mock_print:
#             tasks.list_tasks()
#             mock_print.assert_any_call("✅ 1: Initial task")
#             mock_print.assert_any_call("✅ 2: Second task")
#
#     @patch("builtins.open", new_callable=mock_open)
#     @patch("os.path.exists", return_value=True)
#     def test_add_task(self, mock_exists, mock_file):
#         with patch("json.load", return_value=mock_tasks_data.copy()), \
#              patch("json.dump") as mock_dump:
#             tasks.add_task("New task")
#             mock_dump.assert_called_once()
#             dumped_tasks = mock_dump.call_args[0][0]
#             self.assertEqual(dumped_tasks[-1]["description"], "New task")
#             self.assertEqual(dumped_tasks[-1]["id"], 3)
#
#     @patch("builtins.open", new_callable=mock_open)
#     @patch("os.path.exists", return_value=True)
#     def test_remove_task_valid_id(self, mock_exists, mock_file):
#         with patch("json.load", return_value=mock_tasks_data.copy()), \
#              patch("json.dump") as mock_dump, \
#              patch("builtins.print") as mock_print:
#             tasks.remove_task(1)
#             mock_dump.assert_called_once()
#             updated_tasks = mock_dump.call_args[0][0]
#             self.assertEqual(len(updated_tasks), 1)
#             self.assertEqual(updated_tasks[0]["id"], 2)
#             mock_print.assert_any_call("🗑️ Task 1 removed.")
#
#     @patch("builtins.open", new_callable=mock_open)
#     @patch("os.path.exists", return_value=True)
#     def test_remove_task_invalid_id(self, mock_exists, mock_file):
#         with patch("json.load", return_value=mock_tasks_data.copy()), \
#              patch("builtins.print") as mock_print:
#             tasks.remove_task(99)
#             mock_print.assert_any_call("[!] Task ID 99 not found.")
#
#     @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_tasks_data))
#     @patch("os.path.exists", return_value=True)
#     def test_get_task_by_id_found(self, mock_exists, mock_file):
#         task = tasks.get_task_by_id(2)
#         self.assertEqual(task, "Second task")
#
#     @patch("builtins.open", new_callable=mock_open, read_data=json.dumps(mock_tasks_data))
#     @patch("os.path.exists", return_value=True)
#     def test_get_task_by_id_not_found(self, mock_exists, mock_file):
#         task = tasks.get_task_by_id(99)
#         self.assertIsNone(task)
#
# if __name__ == "__main__":
#     unittest.main()
