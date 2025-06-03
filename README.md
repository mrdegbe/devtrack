```
       _____             _______                 _    
      |  __ \           |__   __|               | |   
      | |  | |  ___ __   __| | _ __  __ _   ___ | | __
      | |  | | / _ \\ \ / /| || '__|/ _` | / __|| |/ /
      | |__| ||  __/ \ V / | || |  | (_| || (__ |   < 
      |_____/  \___|  \_/  |_||_|   \__,_| \___||_|\_\
 
 A developer task tracking and AI-powered Git commit CLI tool
                     — DevTrack —
```
---

## 🏷️ Badges

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Stars](https://img.shields.io/github/stars/mrdegbe/devtrack?style=social)
![Last Commit](https://img.shields.io/github/last-commit/mrdegbe/devtrack)

---

# 🚀 DevTrack CLI

> 🛠️ DevTrack is a lightweight developer productivity CLI tool for tracking tasks and generating meaningful Git commit messages (AI-powered) without leaving the terminal. It works both online (via OpenRouter) and offline (via Ollama).

---

## ✨ Why DevTrack?

Modern developers juggle dozens of tasks daily — but Git alone doesn’t track the **why** behind each change.

🔹 Project managers use Jira.  
🔹 Designers use Figma.  
🔹 Developers use… their memory?

**DevTrack** fills the gap by giving you a developer-first micro-task tracker that lives right in your terminal.

- 🧠 Track your current focus  
- 📝 Generate structured commit messages  
- 🐢 Avoid messy, vague Git history  
- 💻 Stay in flow — no switching tabs or opening heavy tools  

---

## ✨ Features

- ✅ Add, list, and remove tasks
- 🧠 Generate smart commit messages based on task description and git diff
- 🌐 Supports OpenRouter and Ollama for online/offline usage
- 📁 Stores tasks locally in `.devtrack.json`
- 🖥️ Runs from the terminal as `devtrack <command>`

---

## 🚀 Installation

Install globally from PyPI:

```bash
pip install devtrack
```

---

## 🧰 Usage

### ✅ Initialize DevTrack in a Project

```bash
devtrack init
```

This sets up `~/.devtrack.json` for task tracking and walks you through configuring an AI provider for commit message generation.

You'll be asked to choose a provider:

* `openai` → Requires your OpenAI API key.
* `ollama` → Requires a local model name (e.g., `codellama` or `llama3`).
* `openrouter` → Requires your OpenRouter API key and model name (e.g., `openrouter/openchat`).

Your settings are saved in `~/.devtrackrc`.

---

### ➕ Add a Task

```bash
devtrack add "Refactor user authentication flow"
```

### 📋 View All Tasks

```bash
devtrack tasks
```

### ❌ Remove a Task

```bash
devtrack remove <task_id>
```



### 💬 Generate a Commit Message (AI-Powered)

First, stage your changes with `git add`.

Then run:

```bash
devtrack commit <task_id>
```

DevTrack uses your configured AI provider to generate a short, clean Git commit message based on the task description and current Git diff.

---

## 🌐 AI Provider Configuration

To update your AI settings, simply run:

```bash
devtrack init
```

Or edit the `~/.devtrackrc` file directly:

```ini
provider=openrouter
openrouter_api_key=your_api_key
openrouter_model=openrouter/openchat
```
---

## 🧠 How It Works

* Tasks are stored locally in `~/.devtrack.json`
* Each task has an ID, description, tag, and completion status
* Git commits are generated using task data
* Keeps your Git history meaningful and linked to your actual progress

---

## 📂 Project Structure

```
devtrack/
├── devtrack/                  # Main package
│   ├── __init__.py
│   ├── cli.py                 # CLI entry point (Typer app)
│   ├── commits.py             # Commit generation logic
│   ├── tasks.py               # Task management logic
│   └── utils.py               # Utility functions (including config & AI query logic)
│
├── tests/                     # (optional) Unit tests for the CLI and modules
├── examples/                  # (optional) Sample commands and use cases
│
├── .devtrack.json             # Local task storage (generated at runtime)
├── .devtrackrc                # Optional runtime config (e.g., selected AI)
├── .env                       # API keys and environment config
├── pyproject.toml             # Packaging and dependencies
├── requirements.txt           # Pip installable requirements
├── README.md
├── .gitignore

```

---

## 🧰 Requirements

* Python 3.7+
* Git (for commit generation)
* Typer CLI: `python -m pip install typer[all]`

---

## 🌱 Roadmap & Features

See [devtrack\_roadmap.md](./devtrack_roadmap.md) for upcoming features and development phases.

---

## 🧪 Development

For development, make sure you install DevTrack in editable mode:

```bash
pip install -e .
```

Then run your tool from anywhere using:

```bash
devtrack <command>
```
---
## 👨‍💻 Contributing to DevTrack

Thanks for considering contributing! 💡

## How to Contribute

1. Fork the repo
2. Create a branch (`git checkout -b feature-idea`)
3. Make your changes
4. Commit and push
5. Open a Pull Request 🚀

We welcome bug fixes, feature ideas, and even documentation improvements!

<!-- ✅ NEW SECTION STARTS HERE -->

### 🔍 Code Style and Pre-commit Hooks

DevTrack uses [`pre-commit`](https://pre-commit.com/) with [`black`](https://github.com/psf/black) to automatically format Python code before every commit.

To set this up locally (only if you're contributing to DevTrack):

```bash
pip install pre-commit
pre-commit install
```

---
## 🛡 .gitignore

Make sure your `.gitignore` includes:

```
.env
.devtrack.json
.devtrackrc
__pycache__/
*.pyc
devtrack.log
```
---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Author

Created by [Raymond Degbe](https://github.com/mrdegbe) 💻

---

## 💬 Philosophy

> Great developers don’t just write code — they manage focus.
> DevTrack helps you turn microtasks into momentum.
