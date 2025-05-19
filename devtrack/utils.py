# devtrack/utils.py

import os, subprocess, requests, logging
from pathlib import Path
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Logging setup
# logging.basicConfig(filename='devtrack.log', level=logging.ERROR)
log_path = os.path.join(os.path.expanduser("~"), "devtrack.log")
logging.basicConfig(filename=log_path, level=logging.ERROR)

CONFIG_PATH = Path.home() / ".devtrackrc"


def sanitize_output(text: str) -> str:
    return text.encode("utf-8", errors="ignore").decode("utf-8", errors="ignore")


def get_git_diff() -> str:
    try:
        result = subprocess.run(
            ["git", "diff", "--staged"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Git diff error: {e}")
        return ""


def load_config() -> dict:
    config = {}
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH) as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    config[key.strip()] = value.strip()
    return config


def query_openai(prompt: str, api_key: str) -> str:
    try:
        response = requests.post(
            "https://openai.com/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [
                    {"role": "system", "content": "Generate a short, clear Git commit message in present tense (max 12 words)."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            },
            timeout=15
        )
        data = response.json()

        if "choices" not in data:
            raise RuntimeError(f"Unexpected OpenAI response: {data}")

        return data["choices"][0]["message"]["content"].strip()

    except Exception as e:
        logging.error(f"OpenAI Error: {e}")
        raise RuntimeError(f"OpenAI Error: {e}")


def query_ollama(prompt: str, model: str) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", model, prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="ignore",
            timeout=60
        )
        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip())

        return result.stdout.strip()
    except Exception as e:
        logging.error(f"Ollama Error: {e}")
        raise RuntimeError(f"Ollama Error: {e}")


def query_openrouter(prompt: str, api_key: str, model: str) -> str:
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": "Generate a short, clear Git commit message in present tense (max 12 words)."},
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.3
            },
            timeout=15
        )
        data = response.json()

        if "choices" not in data:
            raise RuntimeError(f"Unexpected OpenRouter response: {data}")

        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        logging.error(f"OpenRouter Error: {e}")
        raise RuntimeError(f"OpenRouter Error: {e}")
