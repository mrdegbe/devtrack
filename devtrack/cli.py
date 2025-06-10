import sys
from devtrack.commands import (
    add,
    commit,
    done,
    focus,
    help,
    init,
    remove,
    status,
    summary,
    tasks,
)

COMMANDS = {
    "add": add.run,
    "commit": commit.run,
    "done": done.run,
    "focus": focus.run,
    "help": help.run,
    "init": init.run,
    "remove": remove.run,
    "status": status.run,
    "summary": summary.run,
    "tasks": tasks.run,
}


def main():
    if len(sys.argv) < 2:
        help.run([])
        return

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd in COMMANDS:
        COMMANDS[cmd](args)
    else:
        print(f"[!] Unknown command: {cmd}")
        help.run([])


# import sys
# from devtrack.commits import generate_commit
# from devtrack.tasks import (
#     list_tasks,
#     add_task,
#     remove_task,
#     summary_tasks,
#     mark_task_done,
#     load_tasks,
# )
# from devtrack.project import init_project
# from devtrack.status import show_status
# from devtrack.session import set_active_task
#
#
# def print_help():
#     print(
#         """
# Usage: devtrack <command> [options]
#
# Available commands:
#   init                 Configure DevTrack and set up your AI provider (runs once).
#   summary              List all tasks under Completed tasks and Pending tasks.
#   status               Show current task, staged Git changes, and AI status.
#   done <task_id>       Mark task as done by its ID.
#   commit <task_id>     Generate a Git commit message for the given task ID.
#   tasks                List all tasks.
#   add <description>    Add a new task with the provided description.
#   remove <task_id>     Remove a task by its ID.
#   help                 Show this help message.
# """
#     )
#
#
# def main():
#     if len(sys.argv) < 2:
#         print_help()
#         return
#
#     command = sys.argv[1]
#
#     if command == "commit":
#         if len(sys.argv) < 3:
#             print("[!] Usage: devtrack commit <task_id>")
#             return
#         try:
#             task_id = int(sys.argv[2])
#             generate_commit(task_id)
#         except ValueError:
#             print("[!] Task ID must be an integer.")
#
#     elif command == "tasks":
#         list_tasks()
#
#     elif command == "add":
#         if len(sys.argv) < 3:
#             print("[!] Usage: devtrack add <task description> [--tag <tag>]")
#             return
#
#         # Simple parsing: look for --tag or -t flags
#         args = sys.argv[2:]
#         tag = None
#         if "--tag" in args:
#             tag_index = args.index("--tag")
#             if tag_index + 1 < len(args):
#                 tag = args[tag_index + 1]
#                 # Remove tag flag and value from args
#                 args = args[:tag_index] + args[tag_index + 2 :]
#             else:
#                 print("[!] Please provide a tag after --tag")
#                 return
#         elif "-t" in args:
#             tag_index = args.index("-t")
#             if tag_index + 1 < len(args):
#                 tag = args[tag_index + 1]
#                 args = args[:tag_index] + args[tag_index + 2 :]
#             else:
#                 print("[!] Please provide a tag after -t")
#                 return
#
#         description = " ".join(args)
#         add_task(description, tag)
#
#     elif command == "focus":
#         if len(sys.argv) < 3:
#             print("[!] Usage: devtrack focus <task_id>")
#             return
#         try:
#             task_id = int(sys.argv[2])
#         except ValueError:
#             print("[!] Task ID must be an integer.")
#             return
#
#         tasks = load_tasks()
#         if any(task["id"] == task_id for task in tasks):
#             set_active_task(task_id)
#             print(f"🎯 Now focusing on task #{task_id}")
#         else:
#             print(f"[!] No task found with ID {task_id}")
#
#     elif command == "remove":
#         if len(sys.argv) < 3:
#             print("[!] Usage: devtrack remove <task_id>")
#             return
#         try:
#             task_id = int(sys.argv[2])
#             remove_task(task_id)
#         except ValueError:
#             print("[!] Task ID must be an integer.")
#
#     elif command == "init":
#         init_project()
#
#     elif command == "help":
#         print_help()
#
#     elif command == "done":
#         if len(sys.argv) < 3:
#             print("[!] Usage: devtrack done <task_id>")
#             return
#         try:
#             task_id = int(sys.argv[2])
#             mark_task_done(task_id)
#         except ValueError:
#             print("[!] Task ID must be an integer.")
#
#     elif command == "summary":
#         summary_tasks()
#
#     elif command == "status":
#         show_status()
#
#     else:
#         print(f"[!] Unknown command: {command}")
#         print_help()
