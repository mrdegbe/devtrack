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


def add_task(description, tag=None):
    tasks = load_tasks()
    task_id = 1 if not tasks else tasks[-1]["id"] + 1
    completed = False

    task = {"id": task_id, "description": description, "completed": completed}
    if tag:
        task["tag"] = tag

    tasks.append(task)
    save_tasks(tasks)

    tag_msg = f" [tag: {tag}]" if tag else ""
    print(f"✅ Task added (ID {task_id}): {description}{tag_msg}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return

    for task in tasks:
        tag = task.get("tag")
        tag_msg = f" (tag: {tag})" if tag else ""
        print(f"[{task['id']}] {task['description']}{tag_msg}")


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
        tag = task.get("tag")
        tag_msg = f" (tag: {tag})" if tag else ""
        print(f"  [{task['id']}] {task['description']}{tag_msg}")

    print("\n🕐 Pending Tasks:")
    for task in pending:
        tag = task.get("tag")
        tag_msg = f" (tag: {tag})" if tag else ""
        print(f"  [{task['id']}] {task['description']}{tag_msg}")
