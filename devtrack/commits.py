# devtrack/commits.py

import subprocess, re
from devtrack.utils import (
    sanitize_output,
    get_git_diff,
    query_openai,
    query_ollama,
    load_config,
    query_openrouter,
)
from devtrack.tasks import load_tasks


def generate_commit(task_id: int):
    tasks = load_tasks()
    task = next((t for t in tasks if t["id"] == task_id), None)

    if not task:
        print(f"[!] Task with ID {task_id} not found.")
        return

    description = task["description"]
    diff = get_git_diff()

    if not diff:
        print("[!] No staged changes found. Use `git add` first.")
        return

    # 🧠 Conventional Commit prompt
    prompt = (
        "Write a Git commit message in the Conventional Commits format based on the task and git diff below.\n\n"
        f"Task: {description}\n\nGit Diff:\n{diff}\n\n"
        "Format: <type>(<scope>): <description>\n"
        "Types: feat, fix, chore, docs, refactor, test, style, perf\n"
        "Respond with ONLY the commit message — no explanations or quotes."
    )

    config = load_config()
    provider = config.get("provider", "openai")

    try:
        if provider == "ollama":
            print("🧠 Using Ollama (local model)...")
            commit_message = query_ollama(prompt, config["ollama_model"])
        elif provider == "openrouter":
            print("🌐 Using OpenRouter...")
            try:
                commit_message = query_openrouter(
                    prompt, config["openrouter_api_key"], config["openrouter_model"]
                )
            except Exception as e:
                print(f"[!] Openrouter failed: {e}")
                print("⚠️ Falling back to Ollama...")
                commit_message = query_ollama(prompt, config["ollama_model"])
        else:
            print("🌐 Using OpenAI...")
            try:
                commit_message = query_openai(prompt, config["openai_api_key"])
            except Exception as e:
                print(f"[!] OpenAI failed: {e}")
                print("⚠️ Falling back to Ollama...")
                commit_message = query_ollama(prompt, config["ollama_model"])

        clean_commit_message = sanitize_output(commit_message)

        # 🔍 Ensure message follows Conventional Commit format
        if not clean_commit_message.startswith(
            ("feat", "fix", "chore", "docs", "refactor", "test", "style", "perf")
        ):
            clean_commit_message = f"chore(core): {clean_commit_message}"
        elif "(" not in clean_commit_message:
            # If missing scope, inject default "core"
            split_type = clean_commit_message.split(":", 1)
            if len(split_type) == 2:
                clean_commit_message = f"{split_type[0]}(core):{split_type[1]}"

        subprocess.run(["git", "commit", "-m", clean_commit_message], check=True)
        print("✅ Commit created: " + clean_commit_message)

    except Exception as e:
        print(f"[!] Failed to generate commit: {e}")
