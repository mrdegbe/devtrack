from devtrack.utils import load_tasks, save_tasks, extract_tag


def run(args):
    if not args:
        print("[!] Usage: devtrack add <task description> [--tag <tag>]")
        return

    tag, args = extract_tag(args)
    if tag is None and ("--tag" in args or "-t" in args):
        return  # Tag was expected but not provided

    description = " ".join(args)
    add_task(description, tag)


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
