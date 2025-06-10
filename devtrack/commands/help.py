def run(args=None):
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
