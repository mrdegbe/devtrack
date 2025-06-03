import json, os, subprocess
from devtrack.utils import load_config


def show_status():
    task_file = os.path.expanduser("~/.devtrack.json")

    # Load latest task safely
    if os.path.exists(task_file):
        try:
            with open(task_file, "r") as f:
                tasks = json.load(f)
        except json.JSONDecodeError:
            print("[!] Your task file is empty or corrupted. Resetting to empty list.")
            tasks = []
        current_task = tasks[-1] if tasks else None
    else:
        current_task = None

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
    provider_status = "✅" if is_online else "📴"

    print("\n📊 DevTrack Status\n" + "-" * 25)
    if current_task:
        print(f"🧠 Current Task: {current_task['description']} (#{current_task['id']})")
    else:
        print("🧠 Current Task: None")

    print(f"📂 Staged Changes: {staged_files} file(s)")
    print(f"🌐 AI Provider: {provider} {provider_status}\n")
