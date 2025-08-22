# Purpose:
Quick Git workflow for the L0-hello exercise to demonstrate GitHub Repo usage.

# Developer Notes:
0. Pull the latest changes from the remote before you start

```bash
# Fast-forward only (safe when you don't expect local diverging commits)
# 📝 L0-hello — Quick Git Workflow

A tiny README with copyable commands for working with the `L0-hello` exercise.

## ⬇️ 0 — Pull latest changes
Before you start, pull the latest changes from the remote to avoid conflicts.

```bash
# Fast-forward only (safe when you don't expect local diverging commits)
git pull --ff-only

# Or explicitly pull from the remote branch if upstream isn't set
git pull origin main
```

## 🔎 1 — Check repository status

```bash
git status
```

## ➕ 2 — Stage changed files

Stage the files you want to commit. Example (this exercise):

```bash
git add L0-hello/hello.py L0-hello/hello.png L0-hello/README.md
```

## ✍️ 3 — Create a commit

Open your editor to write a multi-line commit message:

```bash
git commit
```

Or commit in one command with a short summary and longer body:

```bash
git commit -m "Initial commit of exercise L0-hello" -m "Initial commit of \"Hello World\". Exercise L0-hello."
```

## 🚀 4 — Push to remote

Push your changes to the remote branch (example: `main`):

```bash
git push origin main
```

If this is a new branch and you want to set the upstream in one command:

```bash
git push -u origin <branch>
```

## 💡 Notes

- Adjust the branch name if you use something other than `main`.
- If you encounter conflicts on pull, resolve them locally and re-commit before pushing.
