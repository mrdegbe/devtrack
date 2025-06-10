from devtrack.utils import load_tasks, save_tasks


def run(args):
    if not args:
        print("[!] Usage: devtrack done <task_id>")
        return
    try:
        task_id = int(args[0])
        mark_task_done(task_id)
    except ValueError:
        print("[!] Task ID must be an integer.")


def mark_task_done(task_id: int):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"✅ Task [{task_id}] marked as completed.")
            return
    print(f"[!] Task with ID {task_id} not found.")
