import os, json, tempfile
from unittest import mock

from devtrack.project import init_project


@mock.patch("builtins.input", return_value="openai")  # 👈 mock the user input
def test_init_project_creates_config_file(mock_input):
    with tempfile.TemporaryDirectory() as tmpdir:
        with mock.patch(
            "devtrack.project.CONFIG_FILE", os.path.join(tmpdir, "devtrack.json")
        ):
            init_project()

            config_path = os.path.join(tmpdir, "devtrack.json")
            assert os.path.exists(config_path), "Config file was not created"

            with open(config_path, "r") as f:
                data = json.load(f)
                assert "tasks" in data, "Missing 'tasks' key"
                assert (
                    data["tasks"] == []
                ), "'tasks' should be initialized as an empty list"
