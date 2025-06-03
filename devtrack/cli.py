import sys
from devtrack.commits import generate_commit
from devtrack.tasks import (
    list_tasks,
    add_task,
    remove_task,
    summary_tasks,
    mark_task_done,
)
from devtrack.project import init_project
from devtrack.status import show_status


def print_help():
    print(
        """
Usage: devtrack <command> [options]

Available commands:
  init                 Configure DevTrack and set up your AI provider (runs once).
  summary              List all tasks under Completed tasks and Pending tasks.
  status               Show current task, staged Git changes, and AI status.
  done <task_id>       Mark task as done by its ID.
  commit <task_id>     Generate a Git commit message for the given task ID.
  tasks                List all tasks.
  add <description>    Add a new task with the provided description.
  remove <task_id>     Remove a task by its ID.
  help                 Show this help message.
"""
    )


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    command = sys.argv[1]

    if command == "commit":
        if len(sys.argv) < 3:
            print("[!] Usage: devtrack commit <task_id>")
            return
        try:
            task_id = int(sys.argv[2])
            generate_commit(task_id)
        except ValueError:
            print("[!] Task ID must be an integer.")

    elif command == "tasks":
        list_tasks()

    elif command == "add":
        if len(sys.argv) < 3:
            print("[!] Usage: devtrack add <task description>")
            return
        description = " ".join(sys.argv[2:])
        add_task(description)

    elif command == "remove":
        if len(sys.argv) < 3:
            print("[!] Usage: devtrack remove <task_id>")
            return
        try:
            task_id = int(sys.argv[2])
            remove_task(task_id)
        except ValueError:
            print("[!] Task ID must be an integer.")

    elif command == "init":
        init_project()

    elif command == "help":
        print_help()

    elif command == "done":
        if len(sys.argv) < 3:
            print("[!] Usage: devtrack done <task_id>")
            return
        try:
            task_id = int(sys.argv[2])
            mark_task_done(task_id)
        except ValueError:
            print("[!] Task ID must be an integer.")

    elif command == "summary":
        summary_tasks()

    elif command == "status":
        show_status()

    else:
        print(f"[!] Unknown command: {command}")
        print_help()
