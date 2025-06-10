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
