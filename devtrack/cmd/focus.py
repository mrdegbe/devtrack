from devtrack.utils import load_tasks, set_active_task


def run(args):
    if len(args) < 1:
        print("[!] Usage: devtrack focus <task_id>")
        return

    try:
        task_id = int(args[0])
    except ValueError:
        print("[!] Task ID must be an integer.")
        return

    tasks = load_tasks()
    if any(task["id"] == task_id for task in tasks):
        set_active_task(task_id)
        print(f"🎯 Now focusing on task #{task_id}")
    else:
        print(f"[!] No task found with ID {task_id}")
