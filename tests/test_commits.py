import pytest
from devtrack import tasks as task_module
from devtrack.commits import generate_commit

def test_generate_commit_invalid_id(capsys):
    generate_commit(9999)
    captured = capsys.readouterr()
    assert "[!] Task not found" in captured.out

def test_generate_commit_valid(monkeypatch, capsys):
    # Mock task list
    monkeypatch.setattr(task_module, "load_tasks", lambda: [{"id": 1, "description": "Test task"}])

    # Force OpenAI to fail
    monkeypatch.setenv("OPENAI_API_KEY", "")
    # Use mock Ollama model
    monkeypatch.setenv("OLLAMA_MODEL", "llama3")

    # Mock ollama subprocess response
    def mock_ollama_request(task, diff):
        return "mock commit message"

    monkeypatch.setattr("devtrack.utils.get_ollama_commit_message", mock_ollama_request)

    generate_commit(1)
    captured = capsys.readouterr()
    assert "mock commit message" in captured.out


# import unittest
# from unittest.mock import patch, MagicMock
# from devtrack import commits
#
# class TestCommits(unittest.TestCase):
#
#     @patch("devtrack.commits.get_task_by_id", return_value="Refactor login component")
#     @patch("devtrack.commits.get_git_diff", return_value="diff --git a/app.py b/app.py")
#     @patch("devtrack.commits.generate_with_openai", return_value="Refactor: Simplify login logic")
#     def test_generate_commit_with_openai(self, mock_openai, mock_diff, mock_get_task):
#         commits.generate_commit(1)
#         mock_openai.assert_called_once_with("Refactor login component", "diff --git a/app.py b/app.py")
#
#     @patch("devtrack.commits.get_task_by_id", return_value="Add dark mode toggle")
#     @patch("devtrack.commits.get_git_diff", return_value="diff --git a/theme.js b/theme.js")
#     @patch("devtrack.commits.generate_with_openai", side_effect=Exception("openai_api_key"))
#     @patch("devtrack.commits.generate_with_ollama", return_value="feat(ui): add dark mode toggle")
#     def test_fallback_to_ollama(self, mock_ollama, mock_openai, mock_diff, mock_get_task):
#         commits.generate_commit(2)
#         mock_ollama.assert_called_once_with("Add dark mode toggle", "diff --git a/theme.js b/theme.js")
#
#     @patch("builtins.print")
#     @patch("devtrack.commits.get_task_by_id", return_value=None)
#     def test_commit_with_invalid_task(self, mock_get_task, mock_print):
#         commits.generate_commit(999)
#         mock_print.assert_any_call("[!] Task not found.")
#
#     @patch("subprocess.check_output", return_value=b"diff --git a/file.py b/file.py")
#     def test_get_git_diff(self, mock_subprocess):
#         result = commits.get_git_diff()
#         self.assertEqual(result, "diff --git a/file.py b/file.py")
#
#     @patch("devtrack.commits.config", {"ollama_model": "llama3"})
#     @patch("ollama.chat", return_value={"message": {"content": "Refactor: optimize logic"}})
#     def test_generate_with_ollama(self, mock_chat, _):
#         result = commits.generate_with_ollama("Refactor login", "code diff")
#         self.assertEqual(result, "Refactor: optimize logic")
#
#     @patch("devtrack.commits.config", {"openai_api_key": "sk-test", "openai_model": "gpt-4"})
#     @patch("openai.ChatCompletion.create", return_value=MagicMock(choices=[MagicMock(message={"content": "Fix: bug"})]))
#     def test_generate_with_openai(self, mock_openai):
#         result = commits.generate_with_openai("Fix bug", "diff")
#         self.assertEqual(result, "Fix: bug")
#
# if __name__ == "__main__":
#     unittest.main()
