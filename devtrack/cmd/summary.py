from devtrack.utils import load_tasks


def run(args=None):
    summary_tasks()


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
