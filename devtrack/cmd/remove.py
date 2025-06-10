import json
from pathlib import Path
from devtrack.utils import TASKS_FILE, load_tasks, save_tasks


def run(args):
    if not args:
        print("[!] Usage: devtrack remove <task_id>")
        return
    try:
        task_id = int(args[0])
        remove_task(task_id)
    except ValueError:
        print("[!] Task ID must be an integer.")


def remove_task(task_id):
    tasks = load_tasks()
    updated = [t for t in tasks if t["id"] != task_id]
    if len(updated) == len(tasks):
        print(f"[!] Task with ID {task_id} not found.")
    else:
        save_tasks(updated)
        print(f"🗑️ Task {task_id} removed.")
