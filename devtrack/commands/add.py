from devtrack.utils import load_tasks, save_tasks


def run(args):
    if not args:
        print("[!] Usage: devtrack add <task description> [--tag <tag>]")
        return

    tag = None
    if "--tag" in args:
        i = args.index("--tag")
        if i + 1 < len(args):
            tag = args[i + 1]
            args = args[:i] + args[i + 2 :]
        else:
            print("[!] Please provide a tag after --tag")
            return
    elif "-t" in args:
        i = args.index("-t")
        if i + 1 < len(args):
            tag = args[i + 1]
            args = args[:i] + args[i + 2 :]
        else:
            print("[!] Please provide a tag after -t")
            return

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
