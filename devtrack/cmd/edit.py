import sys
from devtrack.utils import load_tasks, save_tasks, extract_tag


def run(args):
    if len(args) < 2:
        print("[!] Usage: devtrack edit <task_id> <new description> [--tag <new_tag>]")
        return

    try:
        task_id = int(args[0])
    except ValueError:
        print("[!] Task ID must be an integer.")
        return

    args = args[1:]
    tag, args = extract_tag(args)
    if tag is None and ("--tag" in args or "-t" in args):
        return  # Tag was expected but not provided

    new_description = " ".join(args)
    edit_task(task_id, new_description, tag)


def edit_task(task_id: int, new_description: str, new_tag: str = None):
    tasks = load_tasks()
    updated = False

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            if new_tag is not None:
                task["tag"] = new_tag
            updated = True
            break

    if updated:
        save_tasks(tasks)
        print(f"✏️ Task #{task_id} updated.")
    else:
        print(f"[!] No task found with ID {task_id}")
