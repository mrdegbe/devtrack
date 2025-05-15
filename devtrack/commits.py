# devtrack/commits.py

import subprocess
from devtrack.utils import (
    sanitize_output,
    get_git_diff,
    query_openai,
    query_ollama,
    load_config
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

    prompt = f"Task: {description}\n\nGit Diff:\n{diff}"

    try:
        config = load_config()
        provider = config.get("provider", "openai")

        if provider == "ollama":
            print("🧠 Using Ollama (local model)...")
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
        subprocess.run(['git', 'commit', '-m', clean_commit_message], check=True)
        print("✅ Commit created: " + clean_commit_message)

    except Exception as e:
        print(f"[!] Failed to generate commit: {e}")


# from tasks import load_tasks
# from utils import get_git_diff, sanitize_output
# from ai import generate_ai_commit_message
# import subprocess
#
# def generate_commit(task_id: int):
#     tasks = load_tasks()
#     task = next((t for t in tasks if t["id"] == task_id), None)
#
#     if not task:
#         print(f"[!] Task with ID {task_id} not found.")
#         return
#
#     diff = get_git_diff()
#     if not diff:
#         print("[!] No staged changes found. Use `git add` first.")
#         return
#
#     prompt = f"Task: {task['description']}\n\nGit Diff:\n{diff}"
#
#     try:
#         commit_message = generate_ai_commit_message(prompt)
#         clean_commit = sanitize_output(commit_message)
#
#         subprocess.run(
#             ['git', 'commit', '-m', clean_commit],
#             check=True,
#             encoding="utf-8",
#             errors="ignore"
#         )
#
#         print("✅ Commit created:", clean_commit)
#
#     except Exception as e:
#         print(f"[!] Failed to generate commit: {e}")
