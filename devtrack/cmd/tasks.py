from devtrack.utils import load_tasks


def run(args=None):
    list_tasks()


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks found.")
        return

    for task in tasks:
        tag = task.get("tag")
        tag_msg = f" (tag: {tag})" if tag else ""
        print(f"[{task['id']}] {task['description']}{tag_msg}")
