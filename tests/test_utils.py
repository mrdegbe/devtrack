import os
import tempfile
import pytest
from devtrack.utils import (
    load_tasks, save_tasks, get_git_diff, get_openai_commit_message, get_ollama_commit_message
)

@pytest.fixture
def sample_tasks():
    return [
        {"id": 1, "description": "Task 1", "completed": False},
        {"id": 2, "description": "Task 2", "completed": True},
    ]

def test_save_and_load_tasks(sample_tasks):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        save_tasks(sample_tasks, tmp.name)
        loaded = load_tasks(tmp.name)
        assert loaded == sample_tasks
    os.remove(tmp.name)

def test_get_git_diff_returns_string():
    diff = get_git_diff()
    assert isinstance(diff, str)

def test_get_openai_commit_message_env_missing(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(KeyError):
        get_openai_commit_message("Test", "diff")

def test_get_ollama_commit_message_model_missing(monkeypatch):
    monkeypatch.delenv("OLLAMA_MODEL", raising=False)
    with pytest.raises(KeyError):
        get_ollama_commit_message("Test", "diff")


# import unittest
# from unittest.mock import mock_open, patch
# import os
# from devtrack import utils
#
# class TestUtils(unittest.TestCase):
#
#     @patch("os.getenv")
#     def test_get_api_key_env_var(self, mock_getenv):
#         mock_getenv.return_value = "env-key"
#         key = utils.get_api_key("openai_api_key")
#         self.assertEqual(key, "env-key")
#         mock_getenv.assert_called_with("OPENAI_API_KEY")
#
#     @patch("os.getenv", return_value=None)
#     @patch("builtins.open", new_callable=mock_open, read_data="[keys]\nopenai_api_key = file-key\n")
#     @patch("os.path.exists", return_value=True)
#     def test_get_api_key_from_file(self, mock_exists, mock_file, mock_getenv):
#         key = utils.get_api_key("openai_api_key")
#         self.assertEqual(key, "file-key")
#
#     @patch("os.getenv", return_value=None)
#     @patch("os.path.exists", return_value=False)
#     def test_get_api_key_not_found(self, mock_exists, mock_getenv):
#         key = utils.get_api_key("nonexistent_key")
#         self.assertIsNone(key)
#
#     @patch("subprocess.run")
#     def test_get_git_diff_success(self, mock_run):
#         mock_run.return_value.stdout = "diff --git ..."
#         diff = utils.get_git_diff()
#         self.assertEqual(diff, "diff --git ...")
#         mock_run.assert_called_once()
#
#     @patch("subprocess.run", side_effect=Exception("Git failed"))
#     def test_get_git_diff_failure(self, mock_run):
#         diff = utils.get_git_diff()
#         self.assertEqual(diff, "[!] Failed to get git diff.")
#
#     def test_log_error_writes_message(self):
#         test_message = "Something went wrong"
#         with patch("builtins.open", mock_open()) as mock_file:
#             utils.log_error(test_message)
#             mock_file().write.assert_any_call(test_message + "\n")
#
# if __name__ == "__main__":
#     unittest.main()
