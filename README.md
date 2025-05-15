## ✅ 1. ASCII Logo

[//]: # (We'll add this at the top of your `README.md`:)

```
 _____             _             _    
|  __ \           | |           | |   
| |  | | ___   ___| |_ __ _  ___| |_  
| |  | |/ _ \ / __| __/ _` |/ __| __| 
| |__| | (_) | (__| || (_| | (__| |_  
|_____/ \___/ \___|\__\__,_|\___|\__| 

            DevTrack CLI
```

---

## 🏷️ 2. Badges

[//]: # (Right under the logo, we'll place these badges:)

[//]: # ()

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/github/license/mrdegbe/devtrack)
![Stars](https://img.shields.io/github/stars/mrdegbe/devtrack?style=social)
![Last Commit](https://img.shields.io/github/last-commit/mrdegbe/devtrack)

---

# 🚀 DevTrack CLI

> 🛠️ A minimalist CLI tool that helps developers track micro-tasks and generate meaningful Git commits without leaving the terminal.

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

## 🧪 Demo

```bash
$ python devtrack.py add "Fix login bug"
✅ Task added: Fix login bug

$ python devtrack.py list
1. 🕓 Fix login bug

$ python devtrack.py done 1
✅ Task 1 marked as done.

$ python devtrack.py commit 1
✅ Commit created: Fix login bug
```

## 📦 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/devtrack.git
cd devtrack
```

### 2. Install Dependencies

```bash
pip install typer[all]
```

---

## 📌 Commands

### ➕ Add a Task

```bash
python devtrack.py add "Write unit tests"
```

With optional tag:

```bash
python devtrack.py add "Implement login page" --tag feature
```

---

### 📋 List Tasks

```bash
python devtrack.py list
```

---

### ✅ Mark a Task as Done

```bash
python devtrack.py done <task_id>
```

---

### 📦 Commit with Task

```bash
python devtrack.py commit <task_id>
```

Generates a Git commit with the task description.
Git must be initialized and have clean staging for this to work.

---

### 📊 View Summary

```bash
python devtrack.py summary
```

Shows completed task stats.

---

## 🧠 How It Works

* Tasks are stored locally in `.devtrack.json`
* Each task has an ID, description, tag, and completion status
* Git commits are generated using task data
* Keeps your Git history meaningful and linked to your actual progress

---

## 📂 Project Structure

```
devtrack/
│
├── devtrack.py        # CLI entry point
├── tasks.py           # Task management functions
├── commits.py         # Git commit logic
├── storage.py         # File read/write utilities
├── .devtrack.json     # Your personal task list (auto-generated)
└── README.md
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

## 👨‍💻 Contributing

Pull requests are welcome!

If you have suggestions for features, improvements, or bug fixes:

1. Fork the repo
2. Create a new branch (`feature/awesome-feature`)
3. Submit a PR 🚀

---

## 📜 License

MIT License © 2025 \[Raymond Degbe]

---

## 💬 Philosophy

> Great developers don’t just write code — they manage focus.
> DevTrack helps you turn microtasks into momentum.
