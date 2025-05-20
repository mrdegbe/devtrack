import pytest, subprocess
from unittest.mock import patch, mock_open, MagicMock
from devtrack import utils


# ─────────────────────────────
# sanitize_output
# ─────────────────────────────
def test_sanitize_output_removes_invalid_utf8():
    input_text = "Hello 👋 \udce2\udce2"
    sanitized = utils.sanitize_output(input_text)
    assert "�" not in sanitized
    assert "Hello" in sanitized


# ─────────────────────────────
# get_git_diff
# ─────────────────────────────
@patch("subprocess.run")
def test_get_git_diff_success(mock_run):
    mock_run.return_value = MagicMock(stdout="diff output\n", returncode=0)
    diff = utils.get_git_diff()
    assert diff == "diff output"


@patch("subprocess.run", side_effect=subprocess.CalledProcessError(1, "git"))
def test_get_git_diff_error(mock_run):
    diff = utils.get_git_diff()
    assert diff == ""


# ─────────────────────────────
# load_config
# ─────────────────────────────
@patch("pathlib.Path.exists", return_value=True)
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="provider=openai\nopenai_api_key=test123\n",
)
def test_load_config(mock_file, mock_exists):
    config = utils.load_config()
    assert config["provider"] == "openai"
    assert config["openai_api_key"] == "test123"


@patch("pathlib.Path.exists", return_value=False)
def test_load_config_no_file(mock_exists):
    config = utils.load_config()
    assert config == {}


# ─────────────────────────────
# query_openai
# ─────────────────────────────
@patch("requests.post")
def test_query_openai_success(mock_post):
    mock_post.return_value.json.return_value = {
        "choices": [{"message": {"content": "Test commit message"}}]
    }

    result = utils.query_openai("Test prompt", "fake_api_key")
    assert result == "Test commit message"


@patch("requests.post")
def test_query_openai_failure(mock_post):
    mock_post.return_value.json.return_value = {"error": "Bad request"}

    with pytest.raises(RuntimeError):
        utils.query_openai("Test prompt", "fake_api_key")


# ─────────────────────────────
# query_ollama
# ─────────────────────────────
@patch("subprocess.run")
def test_query_ollama_success(mock_run):
    mock_run.return_value = MagicMock(returncode=0, stdout="Local AI message\n")
    result = utils.query_ollama("Prompt", "model")
    assert result == "Local AI message"


@patch("subprocess.run", side_effect=Exception("Ollama error"))
def test_query_ollama_error(mock_run):
    with pytest.raises(RuntimeError):
        utils.query_ollama("Prompt", "model")
