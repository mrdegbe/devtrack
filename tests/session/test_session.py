import os
import json
import pytest
from devtrack.session import set_active_task, get_active_task_id

ACTIVE_FILE = os.path.expanduser("~/.devtrack_active.json")


@pytest.fixture(autouse=True)
def clean_active_file():
    # Run before and after each test
    if os.path.exists(ACTIVE_FILE):
        os.remove(ACTIVE_FILE)
    yield
    if os.path.exists(ACTIVE_FILE):
        os.remove(ACTIVE_FILE)


def test_set_and_get_active_task_id():
    set_active_task(7)
    assert get_active_task_id() == 7


def test_get_active_task_id_returns_none_if_file_missing():
    if os.path.exists(ACTIVE_FILE):
        os.remove(ACTIVE_FILE)
    assert get_active_task_id() is None


def test_get_active_task_id_returns_none_if_corrupted():
    with open(ACTIVE_FILE, "w") as f:
        f.write("{{ broken json")
    assert get_active_task_id() is None


def test_set_active_task_creates_valid_json():
    set_active_task(42)
    with open(ACTIVE_FILE) as f:
        data = json.load(f)
    assert data["active_task_id"] == 42
