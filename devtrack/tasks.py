# devtrack/tasks.py

import json
from pathlib import Path

TASKS_FILE = Path.home() / ".devtrack.json"


def load_tasks():
    if not TASKS_FILE.exists():
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("[!] Warning: Task file is corrupted. Starting fresh.")
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(description):
    tasks = load_tasks()
    task_id = 1 if not tasks else tasks[-1]["id"] + 1
    tasks.append({"id": task_id, "description": description})
    save_tasks(tasks)
    print(f"✅  Task added (ID {task_id}): {description}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return
    print("📋 Tasks:")
    for task in tasks:
        print(f"  [{task['id']}] {task['description']}")


def remove_task(task_id):
    tasks = load_tasks()
    updated = [t for t in tasks if t["id"] != task_id]
    if len(updated) == len(tasks):
        print(f"[!] Task with ID {task_id} not found.")
    else:
        save_tasks(updated)
        print(f"🗑️ Task {task_id} removed.")


def get_task_description(task_id):
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)
    return task["description"] if task else None
