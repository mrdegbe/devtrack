import json, os, subprocess
from devtrack.utils import load_config, get_active_task_id, TASKS_FILE


def run(args=None):
    show_status()


def show_status():

    # Load all tasks safely
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                tasks = json.load(f)
        except json.JSONDecodeError:
            print("[!] Your task file is empty or corrupted. Resetting to empty list.")
            tasks = []
    else:
        tasks = []

    active_id = get_active_task_id()  # NEW: Get the task ID that's marked as active
    current_task = next(
        (t for t in tasks if t["id"] == active_id), None
    )  # NEW: Lookup active task

    # Get staged changes
    try:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only"],
            capture_output=True,
            text=True,
            check=True,
        )
        staged_files = len(result.stdout.strip().splitlines())
    except subprocess.CalledProcessError:
        staged_files = 0

    # Load AI config
    config = load_config()
    provider = config.get("provider", "None")
    is_online = provider in ["openai", "openrouter"]
    provider_status = "🟢" if is_online else "🔴"

    print("\n📊 DevTrack Status\n" + "-" * 25)
    if current_task:
        print(
            f" Current Task: {current_task['description']} (#{current_task['id']})"
        )  # MODIFIED: Clarified label
    else:
        print("🎯 Current Task: None")  # MODIFIED: Clarified label

    print(f"📂 Staged Changes: {staged_files} file(s)")
    print(f"🌐 AI Provider: {provider} {provider_status}\n")
