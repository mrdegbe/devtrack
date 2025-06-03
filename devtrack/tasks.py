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
    completed = False
    tasks.append({"id": task_id, "description": description, "completed": completed})
    save_tasks(tasks)
    print(f"✅ Task added (ID {task_id}): {description}")


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


def mark_task_done(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"✅ Task [{task_id}] marked as completed.")
            return
    print(f"[!] Task with ID {task_id} not found.")


def summary_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📝 No tasks found.")
        return

    completed = [t for t in tasks if t.get("completed", False)]
    pending = [t for t in tasks if not t.get("completed", False)]

    print("✅  Completed Tasks:")
    for task in completed:
        print(f"  [{task['id']}] {task['description']}")

    print("\n🕐 Pending Tasks:")
    for task in pending:
        print(f"  [{task['id']}] {task['description']}")
