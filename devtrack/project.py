import os, json
from pathlib import Path

CONFIG_FILE = Path.home() / ".devtrack.json"
CONFIG_RC = Path.home() / ".devtrackrc"


def init_project():
    if os.path.exists(CONFIG_FILE):
        print("✅  DevTrack is already initialized in this project.")
    else:
        default_data = {
            "tasks": []
        }

        try:
            with open(CONFIG_FILE, "w") as f:
                json.dump(default_data, f, indent=2)

            print("📁 Created `devtrack.json` to track your tasks.")
        except Exception as e:
            print(f"[!] Failed to create project task file: {e}")
            return

    print("\n🛠️ Let's configure your AI provider for commit message generation.")

    provider = input("Choose your preferred AI provider [openai / ollama / openrouter]: ").strip().lower()

    config = {
        "provider": provider
    }

    if provider == "openai":
        api_key = input("🔑 Enter your OpenAI API key: ").strip()
        config["openai_api_key"] = api_key
    elif provider == "ollama":
        model = input("🤖 Enter your Ollama model name (e.g., codellama): ").strip()
        config["ollama_model"] = model
    elif provider == "openrouter":
        api_key = input("🔑 Enter your OpenRouter API key: ").strip()
        model = input("🤖 Enter your OpenRouter model (e.g., openrouter/openchat): ").strip()
        config["openrouter_api_key"] = api_key
        config["openrouter_model"] = model
    else:
        print("[!] Unknown provider. Skipping configuration.")
        return

    try:
        with open(CONFIG_RC, "w") as f:
            for key, value in config.items():
                f.write(f"{key}={value}\n")

        print(f"\n✅  Configuration saved to {CONFIG_RC}")
    except Exception as e:
        print(f"[!] Failed to write configuration: {e}")
