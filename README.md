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

## 🔧 Installation

### Clone and install locally (editable mode)

```bash
git clone https://github.com/mrdegbe/devtrack.git
cd devtrack
pip install -e .
````
---
## 📌 Usage

### ➕ Add a Task

```bash
devtrack add "Write unit tests"
```



### 📋 List Tasks

```bash
devtrack tasks
```


### 🗑️ Remove a task

```bash
devtrack remove <task_id>
```

### 📦 Commit with Task

```bash
devtrack commit <task_id>
```
Commits with AI-generated commit message.
Git must be initialized and have clean staging for this to work.

### 📊 View Summary

```bash
devtrack summary
```

Shows completed task stats.

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

* [x] Add/complete/list tasks
* [x] Git commit integration
* [ ] Task filtering by tag
* [ ] Task priority levels
* [ ] GitHub issue linking
* [ ] Daily journal export
* [ ] Zsh/Bash shell completion

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
