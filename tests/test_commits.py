from unittest.mock import patch
from devtrack.commits import generate_commit


@patch("devtrack.commits.load_tasks")
@patch("devtrack.commits.get_git_diff")
@patch("devtrack.commits.load_config")
@patch("devtrack.commits.query_openai")
@patch("devtrack.commits.query_ollama")
@patch("devtrack.commits.sanitize_output")
@patch("devtrack.commits.subprocess.run")
def test_generate_commit_openai_success(
    mock_run,
    mock_sanitize,
    mock_ollama,
    mock_openai,
    mock_config,
    mock_diff,
    mock_tasks,
):
    # Mock task
    mock_tasks.return_value = [{"id": 1, "description": "Add login feature"}]
    mock_diff.return_value = "diff --git a/file.py b/file.py"
    mock_config.return_value = {
        "provider": "openai",
        "openai_api_key": "test-key",
        "ollama_model": "llama3",
    }
    mock_openai.return_value = "commit: add login feature"
    mock_sanitize.return_value = "add login feature"

    generate_commit(1)

    mock_openai.assert_called_once()
    mock_ollama.assert_not_called()
    mock_run.assert_called_once_with(
        ["git", "commit", "-m", "add login feature"], check=True
    )


@patch("devtrack.commits.load_tasks")
def test_generate_commit_task_not_found(mock_tasks, capsys):
    mock_tasks.return_value = [{"id": 2, "description": "Another task"}]

    generate_commit(1)

    captured = capsys.readouterr()
    assert "[!] Task with ID 1 not found." in captured.out


@patch("devtrack.commits.load_tasks")
@patch("devtrack.commits.get_git_diff")
def test_generate_commit_no_diff(mock_diff, mock_tasks, capsys):
    mock_tasks.return_value = [{"id": 1, "description": "Fix bug"}]
    mock_diff.return_value = ""

    generate_commit(1)

    captured = capsys.readouterr()
    assert "[!] No staged changes found." in captured.out


@patch("devtrack.commits.load_tasks")
@patch("devtrack.commits.get_git_diff")
@patch("devtrack.commits.load_config")
@patch("devtrack.commits.query_openai", side_effect=Exception("API key error"))
@patch("devtrack.commits.query_ollama")
@patch("devtrack.commits.sanitize_output")
@patch("devtrack.commits.subprocess.run")
def test_generate_commit_fallback_to_ollama(
    mock_run,
    mock_sanitize,
    mock_ollama,
    mock_openai,
    mock_config,
    mock_diff,
    mock_tasks,
):
    mock_tasks.return_value = [{"id": 1, "description": "Optimize search"}]
    mock_diff.return_value = "some git diff"
    mock_config.return_value = {
        "provider": "openai",
        "openai_api_key": "bad-key",
        "ollama_model": "llama3",
    }
    mock_ollama.return_value = "optimized search feature"
    mock_sanitize.return_value = "optimized search feature"

    generate_commit(1)

    mock_openai.assert_called_once()
    mock_ollama.assert_called_once()
    mock_run.assert_called_once_with(
        ["git", "commit", "-m", "optimized search feature"], check=True
    )
