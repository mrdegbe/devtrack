
# 🛣️ DevTrack Roadmap

**Vision**: Make DevTrack the go-to CLI companion for developers, combining productivity, AI-powered assistance, and streamlined git workflows into one cohesive tool.

---

## ✅ MVP (Completed)
- [x] Add task (`devtrack add`)
- [x] List tasks (`devtrack tasks`)
- [x] Remove task (`devtrack remove`)
- [x] Generate commit message from task + `git diff` using:
  - OpenAI (primary)
  - Ollama (fallback/local)
- [x] Config file support (`~/.devtrackrc`)
- [x] Unit tests
- [x] PyPI packaging

---

## 🔜 Phase 1: Core Usability & Daily Workflow
- [ ] **Task categories/labels** (e.g. `bug`, `feature`, `chore`)
- [ ] **Edit task descriptions**
- [ ] **Mark tasks as completed**
- [ ] **List tasks with filters** (e.g. only completed, only pending)
- [ ] **Enhanced AI prompt context**: Include file names, changes summary, or branch name
- [ ] **Undo last task operation**
- [ ] **Dry run mode** for commit (see what would happen without committing)

---

## 🚀 Phase 2: Developer Experience & AI Boost
- [ ] **Interactive mode** (`devtrack --interactive`) with prompts & suggestions
- [ ] **Inline task suggestions** based on staged diff
- [ ] **AI-assisted changelog generation**
- [ ] **Alias support** for faster commands
- [ ] **Configurable commit style templates** (Angular, Conventional Commits, etc.)
- [ ] **Automatic task linking to GitHub issues (optional)**

---

## 🌐 Phase 3: Collaboration & Integration
- [ ] **GitHub integration** (sync tasks/issues)
- [ ] **Team mode** with shared `.devtrack.json`
- [ ] **Cloud sync / backup** support
- [ ] **VS Code extension** (bonus goal)

---

## 🧪 Experimental Ideas (Explore after core is solid)
- [ ] AI-powered code review CLI companion
- [ ] Timeline-based task view
- [ ] Voice-to-task input (integrate whisper)
- [ ] `devtrack journal` – keep a daily log of progress/tasks

---

## 🧰 Developer Contribution Friendly
- [ ] CONTRIBUTING.md guide
- [ ] Good first issues labeled
- [ ] Modular plugin-like architecture (optional)
