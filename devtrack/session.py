import os, json

ACTIVE_FILE = os.path.expanduser("~/.devtrack_active.json")


def set_active_task(task_id):
    """NEW: Save the currently active task ID to session state."""
    with open(ACTIVE_FILE, "w") as f:
        json.dump({"active_task_id": task_id}, f)


def get_active_task_id():
    """NEW: Retrieve the active task ID from session state."""
    if not os.path.exists(ACTIVE_FILE):
        return None
    with open(ACTIVE_FILE, "r") as f:
        try:
            data = json.load(f)
            return data.get("active_task_id")
        except json.JSONDecodeError:
            return None
