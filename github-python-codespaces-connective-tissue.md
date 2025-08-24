# 🧭 GitHub + Python + Codespaces: The Connective Tissue

A quick, practical intro to the *why* behind the terminal, GitHub, and Python in VS Code/Codespaces. Skimmable. Emoji-powered. Zero fluff.

---

## 🖥️ Why a Terminal Exists
- It is a precise control panel for your computer.
- Tools like Git and Python speak terminal first.
- Commands are fast and reproducible. That reduces confusion in class.

---

## 📂 Moving Around Folders
You run commands *in the folder that holds your files*. Know where you are.

- `pwd` → 📍 show current folder.
- `ls` → 📋 list files and folders.
- `cd foldername` → 🚪 enter a folder.
- `cd ..` → ⬆️ go up one level.

Tip: your *working directory* is where `python` and `git` look by default.

---

## 🐚 Terminal “Languages”
- **Bash** (Codespaces, Mac, Linux) → uses `ls`, `pwd`, `cd`.
- **PowerShell** (Windows) → similar idea, different syntax.
- **Python shell** → interactive Python mode. Start it with `python` then exit with `exit()`.

In VS Code you’ll usually be in **bash** unless you start Python on purpose.

---

## 🐍 Running Python
- Python files end with `.py`.
- Run a file from the folder that contains it:
  ```bash
  python hello.py
  ```
- If that fails, check:
  - Are you in the right folder? `pwd`
  - Does the file exist here? `ls`
  - Is your environment using the right Python? `python --version`

---

## 🗂️ Typical Project Shape
Example:
```
my-project/
├─ README.md
├─ .gitignore
├─ requirements.txt      # packages to install
├─ src/
│  ├─ main.py
│  └─ utils.py
└─ tests/
   └─ test_main.py
```
You run from the project folder or `src` depending on how imports are set up.

---

## 🌎 GitHub + Git: The Daily Cycle
GitHub is the cloud. Git is the tool that syncs your code with the cloud.

**Workflow**:
🔄 **pull** → 📋 **status** → ➕ **add** → 📝 **commit** → ☁️ **push** → ✅ **status**

![Git Workflow](git-workflow.png)

### Commands you’ll type
1) 🔄 **Pull the latest**
```bash
git pull
```
2) 📋 **See what changed**
```bash
git status
```
3) ➕ **Stage files for saving**
```bash
git add filename.py
# or stage everything (be intentional)
git add .
```
4) 📝 **Commit locally with a message**
```bash
git commit -m "Add solution for Lab 2: loops"
```
5) ☁️ **Push to GitHub**
```bash
git push
```
6) ✅ **Confirm state**
```bash
git status
```

### Why this order?
- Pull first to avoid conflicts.
- Status before and after to keep your mental model correct.
- Add → commit → push is a three-step save: stage → record → upload.

---

## 🧰 Quick Reference
- Where am I? `pwd`
- What’s here? `ls`
- Move: `cd <folder>`
- Go up: `cd ..`
- Run code: `python file.py`
- Git status: `git status`
- Save work: `git add` → `git commit -m "msg"` → `git push`

---

## 🚑 Common “Huh?” Moments
- “`python: can't open file`” → You are in the wrong folder or the filename is misspelled.
- “`command not found: git`” → You’re not in Codespaces or Git isn’t installed.
- “`error: failed to push refs`” → Pull first: `git pull`, resolve, then push.
- Stuck in Python shell (`>>>`)? Type `exit()` or press `Ctrl+D`.

---

## ✅ Minimal Daily Checklist
- 🔄 `git pull` before you start.
- 🧪 Run your code locally with `python ...`.
- 📝 Commit small, clear changes with messages that make sense.
- ☁️ `git push` when you’re done.
- 📋 `git status` to confirm you’re clean.

---

## 🎯 Mental Model
- Terminal = conversation with your computer.
- Folder = context. Commands act on *here*.
- Git = version history. GitHub = your remote copy.

Learn the muscle memory. The rest gets easier.
