# Contributing to DevTrack

Thanks for your interest in contributing to DevTrack! 🎉  
We welcome contributions of all kinds — bug fixes, new features, documentation improvements, testing, and more.

## 🚀 Getting Started

1. **Fork the repo** and clone it:
```bash
   git clone https://github.com/YOUR-USERNAME/devtrack.git
   cd devtrack
```

2. **Set up your environment**:

```bash
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows
pip install -r requirements.txt
pip install -e .
  ```

3. **Run tests** to ensure everything works:

```bash
pytest
```

---

## 🛠 How to Contribute

### 📄 1. Pick or Create an Issue

* Browse [open issues](https://github.com/YOUR-USERNAME/devtrack/issues)
* Or open a new one if you're suggesting a new feature or bug fix

### 🧪 2. Create a New Branch

```bash
git checkout -b feature/your-feature-name
```

### 🧹 3. Follow Code Style

* Keep it **clean, minimal, and documented**
* Follow [PEP8](https://peps.python.org/pep-0008/)

### ✅ 4. Test Your Changes

* Write or update tests in the `tests/` folder
* Run `pytest` before committing

### 💬 5. Commit Message Guidelines

* Use clear commit messages in present tense

```
Add support for OpenRouter as backup provider
Fix fallback error message handling
```

### 📦 6. Push and Submit a Pull Request

```bash
git push origin feature/your-feature-name
```

Then open a PR with a clear description of your changes.

---

## ❤️ Community

Be kind, respectful, and collaborative. Let's build something amazing together!
