The **default branch** is:

> 🔸 **`main`**

### Why?

* `main` (or sometimes called `master`) represents the **production-ready** codebase.
* It's the branch that new users see by default when they visit your GitHub repository.
* Your releases, deployments, and PyPI publishing should be tied to it.

---

### Branch Setup:

| Branch          | Purpose                                                                       |
| --------------- | ----------------------------------------------------------------------------- |
| `main`          | ✅ **Default branch** – always stable and ready for release.                   |
| `develop`       | Where all completed features are merged and tested before going to `main`.    |
| `feature/*`     | For new features. Merged into `develop`.                                      |
| `refactor/*`    | For code improvements or restructures. Merged into `develop`.                 |
| `test/*`        | For test-related work. Merged into `develop`.                                 |
| `release/x.y.z` | For prepping a release. Merges into both `main` and `develop`.                |
| `hotfix/*`      | For urgent bug fixes. Branches from `main`, merges into `main` and `develop`. |
| `docs`          | For documentation-only changes.                                               |
| `gh-actions`    | For GitHub Actions and CI/CD configuration.                                   |
