# Agent Quick Reference Guide

Quick command reference for agents working on Maths-Mining in parallel.

## 🚀 Starting a New Task

```bash
# 1. Update develop branch
git checkout develop
git pull origin develop

# 2. Create your agent branch
git checkout -b agent/<your-id>/<task-name>

# Example:
# git checkout -b agent/001/implement-matrix-ops
```

## 💾 Daily Workflow

```bash
# Morning: Sync with latest changes
git fetch origin develop
git rebase origin/develop

# During work: Commit frequently
git add .
git commit -m "feat(scope): what you did"

# Evening: Push your progress
git push origin agent/<your-id>/<task-name>
# If rebased: git push --force-with-lease
```

## 🔄 Keeping Branch Updated

```bash
# Option 1: Rebase (preferred - cleaner history)
git fetch origin develop
git rebase origin/develop

# Option 2: Merge (if rebase is problematic)
git fetch origin develop
git merge origin/develop
```

## ✅ Submitting Your Work

```bash
# 1. Final sync
git fetch origin develop
git rebase origin/develop

# 2. Push to remote
git push origin agent/<your-id>/<task-name>

# 3. Create Pull Request on GitHub
# - Base: develop
# - Compare: agent/<your-id>/<task-name>
# - Fill out PR template

# 4. After merge approval
git checkout develop
git pull origin develop
git branch -d agent/<your-id>/<task-name>
```

## 🔧 Common Scenarios

### Handling Merge Conflicts

```bash
# Conflicts appear during rebase
git status  # See conflicting files

# Fix conflicts in your editor, then:
git add <resolved-files>
git rebase --continue

# Push updated branch
git push --force-with-lease
```

### Switching Between Tasks

```bash
# Save current work
git add .
git commit -m "wip: save progress"
# or use: git stash

# Switch to other task
git checkout agent/<your-id>/<other-task>

# Return to first task
git checkout agent/<your-id>/<first-task>
```

### Undoing Mistakes

```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard all uncommitted changes
git checkout .

# Revert a specific file
git checkout -- <filename>

# Abandon branch and start fresh
git checkout develop
git branch -D agent/<your-id>/<task-name>
git checkout -b agent/<your-id>/<task-name>
```

## 📝 Commit Message Template

```
<type>(<scope>): <short summary>

<optional detailed description>

<optional footer>
```

**Types:** feat, fix, docs, style, refactor, test, chore

**Examples:**
```bash
git commit -m "feat(algebra): add quadratic solver"
git commit -m "fix(geometry): correct triangle area calculation"
git commit -m "docs(readme): update installation steps"
git commit -m "test(calculus): add derivative test cases"
```

## 🎯 Branch Naming

**Format:** `agent/<agent-id>/<task-description>`

**Good Examples:**
- `agent/001/matrix-multiplication`
- `agent/002/add-statistics-module`
- `agent/003/fix-division-error`
- `agent/004/update-docs`

**Bad Examples:**
- `agent1` (not descriptive)
- `temp-branch` (unclear purpose)
- `my_work` (no agent ID)

## 🔍 Checking Status

```bash
# See current branch and uncommitted changes
git status

# See commit history
git log --oneline -10

# See your changes
git diff

# See staged changes
git diff --cached

# See branches
git branch -a

# See what's on develop
git log develop..HEAD --oneline
```

## 🤝 Coordination with Other Agents

### Before Starting
1. Check GitHub issues for claimed tasks
2. Comment on issue to claim your task
3. Check for related open PRs

### During Work
1. Rebase from develop daily
2. Monitor other agents' merged PRs
3. Communicate blockers in PR comments

### Before Merging
1. Review your own PR first
2. Ensure all checks pass
3. Resolve all review comments
4. Squash commits if needed

## 🚨 Emergency Commands

### Stop Everything and Get Help
```bash
# Save your work first
git stash

# Check what's happening
git status
git log --oneline -5

# Get back to safe state
git checkout develop
```

### Recover from Bad State
```bash
# Abort ongoing rebase
git rebase --abort

# Abort ongoing merge
git merge --abort

# Hard reset to last known good state
git reset --hard origin/agent/<your-id>/<task-name>
```

## 📊 Visual Cheat Sheet

```
Your Workflow:
┌─────────────┐
│   develop   │ (main integration branch)
└──────┬──────┘
       │ git checkout -b agent/ID/task
       ↓
┌─────────────┐
│ agent/ID/   │ (your working branch)
│    task     │
└──────┬──────┘
       │ work, commit, push
       │ rebase from develop regularly
       │
       ↓
┌─────────────┐
│ Pull Request│ → Review → Merge
└─────────────┘
       │
       ↓
┌─────────────┐
│   develop   │ (updated with your work)
└─────────────┘
```

## 🎓 Best Practices

1. **Commit Often**: Small, focused commits are better
2. **Push Daily**: Don't lose work, push at least once per day
3. **Rebase Regularly**: Stay in sync with develop
4. **Test Before PR**: Run tests locally first
5. **Self-Review**: Check your own diff before requesting review
6. **Keep it Small**: Aim to merge within 1-3 days
7. **Clear Messages**: Write descriptive commit messages
8. **Ask Questions**: Better to ask than to guess

## 📚 Learn More

- [BRANCHING_STRATEGY.md](BRANCHING_STRATEGY.md) - Complete guide
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [README.md](README.md) - Project overview

## 🆘 Getting Unstuck

### "I have conflicts"
→ See "Handling Merge Conflicts" section above

### "My branch is way behind develop"
```bash
git fetch origin develop
git rebase origin/develop
# Resolve any conflicts
git push --force-with-lease
```

### "I committed to wrong branch"
```bash
# On wrong branch
git log -1  # Note the commit hash
git reset --hard HEAD~1  # Remove from wrong branch

# Switch to correct branch
git checkout correct-branch
git cherry-pick <commit-hash>
```

### "I need to change last commit message"
```bash
git commit --amend -m "new message"
git push --force-with-lease
```

### "Help! I broke something!"
1. Don't panic
2. `git status` to see what's happening
3. `git stash` to save your changes
4. `git checkout develop` to get to safe state
5. Ask for help with specific error message

---

**Remember:** Branches are cheap, conflicts are expensive. When in doubt, create a new branch!

**Need Help?** Check [BRANCHING_STRATEGY.md](BRANCHING_STRATEGY.md) for detailed information or ask in your PR/issue comments.
