from unittest.mock import patch, mock_open, MagicMock
from devtrack.status import show_status


@patch("builtins.print")
@patch("devtrack.status.subprocess.run")
@patch("os.path.exists")
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"id": 1, "description": "Fix login bug"}]',
)
@patch("devtrack.status.load_config")
def test_show_status(
    mock_load_config, mock_open_file, mock_exists, mock_subprocess_run, mock_print
):
    # Mock task file exists
    mock_exists.return_value = True

    # Mock subprocess git diff return
    mock_subprocess_run.return_value = MagicMock(
        stdout="file1.py\nfile2.py\n", returncode=0
    )

    # Mock config
    mock_load_config.return_value = {"provider": "openrouter"}

    show_status()

    printed_lines = [args[0] for args, _ in mock_print.call_args_list]

    assert any("🧠 Current Task: Fix login bug (#1)" in line for line in printed_lines)
    assert any("📂 Staged Changes: 2 file(s)" in line for line in printed_lines)
    assert any("🌐 AI Provider: openrouter ✅" in line for line in printed_lines)
