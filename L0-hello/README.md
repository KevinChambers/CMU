Developer Notes:
Quick git workflow for this exercise:

1. Check repository status

```bash
git status
```

2. Stage changed files (example: `hello.py`)

```bash
git add L0-hello/hello.py
```

3. Create a commit with a short summary and longer description (opens editor):

```bash
git commit
```

Alternatively, commit in one command with a multi-line message:

```bash
git commit -m "Initial commit of exercise L0-hello" -m "Initial commit of \"Hello World\". Exercise L0-hello."
```

4. Push to the remote branch `main`:

```bash
git push origin main
```

Notes
- Adjust the branch name if you use a different branch.
- If this is the first push for a new branch, use `git push -u origin <branch>` to set upstream.