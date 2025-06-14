import sys
from devtrack.cmd import (
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
    edit,
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
    "edit": edit.run,
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
