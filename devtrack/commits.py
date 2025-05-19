# devtrack/commits.py

import subprocess, re
from devtrack.utils import (
    sanitize_output,
    get_git_diff,
    query_openai,
    query_ollama,
    load_config,
    query_openrouter
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
    config = load_config()
    provider = config.get("provider", "openai")

    commit_message = None

    try:
        if provider == "ollama":
            print("🧠 Using Ollama (local model)...")
            commit_message = query_ollama(prompt, config["ollama_model"])

        elif provider == "openrouter":
            print("🌐 Using OpenRouter...")
            try:
                commit_message = query_openrouter(prompt, config["openrouter_api_key"], config["openrouter_model"])
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

        # Sanitize and clean up response
        clean_commit_message = sanitize_output(commit_message).strip()

        # Try extracting content between quotes
        match = re.search(r'"([^"]+)"', clean_commit_message)
        if match:
            clean_commit_message = match.group(1)

        # Strip common prefixes
        prefixes = [
            "Here is a short, clear Git commit message in the present tense",
            "Commit message",
            "Suggested commit message"
        ]
        for prefix in prefixes:
            if clean_commit_message.lower().startswith(prefix.lower()):
                clean_commit_message = clean_commit_message[len(prefix):].strip(": \n\"")

        clean_commit_message = clean_commit_message.strip()

        subprocess.run(['git', 'commit', '-m', clean_commit_message], check=True)
        print("✅ Commit created: " + clean_commit_message)

    except Exception as e:
        print(f"[!] Failed to generate commit: {e}")

# def generate_commit(task_id: int):
#     tasks = load_tasks()
#     task = next((t for t in tasks if t["id"] == task_id), None)
#
#     if not task:
#         print(f"[!] Task with ID {task_id} not found.")
#         return
#
#     description = task["description"]
#     diff = get_git_diff()
#
#     if not diff:
#         print("[!] No staged changes found. Use `git add` first.")
#         return
#
#     prompt = f"Task: {description}\n\nGit Diff:\n{diff}"
#     config = load_config()
#     provider = config.get("provider", "openai")
#
#     def try_provider(p):
#         if p == "openai":
#             print("🌐 Using OpenAI...")
#             return query_openai(prompt, config["openai_api_key"])
#         elif p == "ollama":
#             print("🧠 Using Ollama (local model)...")
#             return query_ollama(prompt, config["ollama_model"])
#         elif p == "openrouter":
#             print("🌐 Using OpenRouter...")
#             return query_openrouter(prompt, config["openrouter_api_key"], config["openrouter_model"])
#         else:
#             raise ValueError(f"Unsupported provider: {p}")
#
#     try:
#         commit_message = try_provider(provider)
#     except Exception as e:
#         print(f"[!] {provider.title()} failed: {e}")
#         # Fallback sequence
#         fallbacks = ["openai", "openrouter", "ollama"]
#         for fallback in fallbacks:
#             if fallback == provider:
#                 continue
#             try:
#                 if (fallback == "openai" and "openai_api_key" in config) or \
#                    (fallback == "openrouter" and all(k in config for k in ["openrouter_api_key", "openrouter_model"])) or \
#                    (fallback == "ollama" and "ollama_model" in config):
#                     print(f"⚠️ Falling back to {fallback.title()}...")
#                     commit_message = try_provider(fallback)
#                     break
#             except Exception as fallback_error:
#                 print(f"[!] {fallback.title()} failed: {fallback_error}")
#         else:
#             print("[!] All providers failed. Cannot generate commit message.")
#             return
#
#     clean_commit_message = sanitize_output(commit_message).strip()
#
#     try:
#         subprocess.run(['git', 'commit', '-m', clean_commit_message], check=True)
#         print("✅ Commit created: " + clean_commit_message)
#     except subprocess.CalledProcessError as e:
#         print(f"[!] Git commit failed: {e}")

