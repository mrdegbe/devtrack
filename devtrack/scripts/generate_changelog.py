import subprocess
import re
from pathlib import Path

# Changelog file path
CHANGELOG_PATH = Path("CHANGELOG.md")

# Conventional commit pattern
commit_re = re.compile(r"^(feat|fix|docs|style|refactor|perf|test|chore)(\((.*?)\))?:\s(.+)$")

def get_commit_log():
    result = subprocess.run(
        ["git", "log", "--pretty=format:%s", "--no-merges"],
        capture_output=True, text=True, check=True
    )
    return result.stdout.strip().split("\n")

def parse_commits(commits):
    sections = {
        "feat": [],
        "fix": [],
        "docs": [],
        "style": [],
        "refactor": [],
        "perf": [],
        "test": [],
        "chore": []
    }

    for msg in commits:
        match = commit_re.match(msg)
        if match:
            type_, _, scope, description = match.groups()
            formatted = f"- {description}" if not scope else f"- **{scope}**: {description}"
            sections[type_].append(formatted)

    return sections

def generate_changelog():
    commits = get_commit_log()
    parsed = parse_commits(commits)

    lines = ["# 📝 Changelog\n"]

    for section, messages in parsed.items():
        if messages:
            section_title = {
                "feat": "✨ Features",
                "fix": "🐛 Bug Fixes",
                "docs": "📝 Documentation",
                "style": "💄 Style",
                "refactor": "🧹 Code Refactoring",
                "perf": "⚡ Performance",
                "test": "✅ Tests",
                "chore": "🔧 Chores"
            }[section]
            lines.append(f"## {section_title}")
            lines.extend(messages)
            lines.append("")  # add a newline

    CHANGELOG_PATH.write_text("\n".join(lines), encoding="utf-8")
    print("✅ CHANGELOG.md generated!")

if __name__ == "__main__":
    generate_changelog()
