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

🛠️ DevTrack is a lightweight developer productivity CLI tool for tracking microtasks and generating smart Git commit messages using AI. It works both online (OpenRouter/OpenAI) and offline (Ollama).

## ✨ Why DevTrack?

Most devs juggle dozens of thoughts and changes. Git doesn’t capture the *why* — DevTrack does.

🔹 Project managers have Jira.
🔹 Designers have Figma.
🔹 Developers? Now we have DevTrack.

* 🧠 Track your focus per task
* 🧾 Avoid vague Git commit messages
* 💻 Stay in flow, never leave the terminal
* 🧠 Smart commit messages powered by AI

---

## 🔥 Features

* ✅ Add, list, tag, remove, and complete tasks
* 🧠 Mark any task as your current focus
* 💬 Generate smart, AI-assisted Git commit messages
* 📂 Works with OpenRouter, OpenAI, or Ollama
* 📁 Stores tasks locally in `.devtrack.json`
* 🧠 Stores current focus in `.devtrack_active.json`

---

## 🚀 Installation

```bash
pip install devtrack
```

---

## 🧰 Usage

### ✅ Initialize DevTrack

```bash
devtrack init
```

This creates `~/.devtrack.json` for tasks and lets you configure your AI provider in `~/.devtrackrc`.

---

### ➕ Add a Task (with optional tag)

```bash
devtrack add "Implement login screen" --tag feature
```

---

### 🎯 Set a Task as Your Focus

```bash
devtrack focus 2
```

This marks task ID `2` as your current working task.

---

### 📊 View Dev Status

```bash
devtrack status
```


📋 **Output:**

```
📊 DevTrack Status
-------------------------
🧠 Current Task: Fix login bug (#2)
📂 Staged Changes: 2 file(s)
🌐 AI Provider: openai ✅
```


---

### 📋 List Tasks

```bash
devtrack tasks
```

Lists all tasks with IDs, descriptions, and tags.

---

### ✅ Mark Task as Done

```bash
devtrack done 2
```

---

### ❌ Remove a Task

```bash
devtrack remove 3
```

---

### 💬 Generate an AI Commit Message

Stage your changes first:

```bash
git add .
devtrack commit 2
```

Generates a commit message based on the task and your `git diff`.

---

## 🌐 AI Configuration

To reconfigure AI provider:

```bash
devtrack init
```

Or edit `~/.devtrackrc`:

```ini
provider=openrouter
openrouter_api_key=your_api_key
openrouter_model=openrouter/openchat
```

---

## 🧠 How It Works

* Tasks saved in `~/.devtrack.json`
* Current focus saved in `~/.devtrack_focus.json`
* Tasks include: ID, description, tag, completed flag
* Git commit messages generated from task + diff

---
## 🌱 Roadmap

See [devtrack\_roadmap.md](./devtrack_roadmap.md)

---

## 🧪 Development

```bash
pip install -e .
```

Then run from anywhere:

```bash
devtrack <command>
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch
3. Commit + Push
4. Open a Pull Request

---

## 🧼 Pre-commit

DevTrack uses `black` for formatting:

```bash
pip install pre-commit
pre-commit install
```

---

## 🛡 .gitignore

Ensure `.gitignore` contains:

```
.env
.devtrack.json
.devtrack_focus.json
.devtrackrc
__pycache__/
*.pyc
```

---

## 📜 License

MIT License

---

## 💡 Author

Created by [Raymond Degbe](https://github.com/mrdegbe)

---

## 💬 Dev Philosophy

> Great devs don’t just write code — they manage focus.
> DevTrack turns microtasks into momentum.

---