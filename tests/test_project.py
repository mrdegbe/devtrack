from pathlib import Path
import tempfile, json
from unittest import mock
from devtrack.project import init_project

@mock.patch("builtins.input", side_effect=["openai", "test-key"])  # Mock both provider + API key
def test_init_project_creates_config_file(mock_input):
    with tempfile.TemporaryDirectory() as tmpdir:
        # Patch both the task config and the RC config paths
        with mock.patch("devtrack.project.CONFIG_FILE", Path(tmpdir) / "devtrack.json"), \
             mock.patch("devtrack.project.CONFIG_RC", Path(tmpdir) / ".devtrackrc"):  # 👈 PATCH THIS

            init_project()

            # Validate JSON task file
            config_path = Path(tmpdir) / "devtrack.json"
            assert config_path.exists(), "Config file was not created"

            with open(config_path, "r") as f:
                data = json.load(f)
                assert "tasks" in data, "Missing 'tasks' key"
                assert data["tasks"] == [], "'tasks' should be initialized as an empty list"

            # Validate .devtrackrc content
            rc_path = Path(tmpdir) / ".devtrackrc"
            assert rc_path.exists(), ".devtrackrc was not created"
            content = rc_path.read_text()
            assert "provider=openai" in content
            assert "openai_api_key=test-key" in content
