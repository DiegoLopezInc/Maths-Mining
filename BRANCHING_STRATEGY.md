# Git Branching Strategy for Maths-Mining

## Overview

This document defines the git branching structure for the Maths-Mining repository, enabling multiple agents to work in parallel efficiently and safely.

## Branch Structure

### Main Branches

```
main (production-ready code)
├── develop (integration branch for features)
├── feature/* (feature development branches)
├── agent/* (agent-specific working branches)
├── hotfix/* (urgent production fixes)
└── release/* (release preparation branches)
```

### Branch Types and Purposes

#### 1. `main`
- **Purpose**: Production-ready code only
- **Protection**: Protected branch, requires PR reviews
- **Merge from**: `release/*`, `hotfix/*`
- **Lifetime**: Permanent

#### 2. `develop`
- **Purpose**: Integration branch for ongoing development
- **Protection**: Protected, requires PR reviews
- **Merge from**: `feature/*`, `agent/*`
- **Merge to**: `release/*`
- **Lifetime**: Permanent

#### 3. `feature/*`
- **Naming**: `feature/<descriptive-name>`
- **Example**: `feature/matrix-operations`, `feature/prime-factorization`
- **Purpose**: New feature development
- **Branch from**: `develop`
- **Merge to**: `develop`
- **Lifetime**: Delete after merging

#### 4. `agent/*`
- **Naming**: `agent/<agent-id>/<task-name>`
- **Example**: `agent/001/implement-sorting`, `agent/002/add-documentation`
- **Purpose**: Agent-specific work isolation
- **Branch from**: `develop`
- **Merge to**: `develop`
- **Lifetime**: Delete after merging
- **Notes**: Each agent should work on its own branch to avoid conflicts

#### 5. `hotfix/*`
- **Naming**: `hotfix/<issue-description>`
- **Example**: `hotfix/critical-math-error`, `hotfix/security-patch`
- **Purpose**: Critical fixes for production
- **Branch from**: `main`
- **Merge to**: `main` AND `develop`
- **Lifetime**: Delete after merging

#### 6. `release/*`
- **Naming**: `release/<version>`
- **Example**: `release/1.0.0`, `release/2.1.0`
- **Purpose**: Release preparation and testing
- **Branch from**: `develop`
- **Merge to**: `main` (and back to `develop`)
- **Lifetime**: Delete after merging

## Workflow for Multiple Agents

### Agent Workflow

1. **Start New Task**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b agent/<agent-id>/<task-name>
   ```

2. **Work on Task**
   ```bash
   # Make changes and commit regularly
   git add .
   git commit -m "Descriptive commit message"
   ```

3. **Sync with Latest Changes**
   ```bash
   git fetch origin develop
   git rebase origin/develop
   # Resolve any conflicts if they occur
   ```

4. **Push Work**
   ```bash
   git push origin agent/<agent-id>/<task-name>
   ```

5. **Create Pull Request**
   - Target: `develop` branch
   - Title: Clear description of changes
   - Description: Details of implementation
   - Request reviews if required

6. **After Merge**
   ```bash
   git checkout develop
   git pull origin develop
   git branch -d agent/<agent-id>/<task-name>
   ```

### Parallel Work Strategy

#### For Independent Tasks
- Each agent works on a separate `agent/*` branch
- Agents can work simultaneously without interference
- Regular rebasing from `develop` keeps branches up-to-date

#### For Dependent Tasks
- Agent 1 completes their work and merges to `develop`
- Agent 2 branches from updated `develop` or rebases onto it
- Communication via commit messages and PR comments

#### For Conflicting Changes
- First agent to merge wins (merges to `develop`)
- Subsequent agents must rebase and resolve conflicts
- Conflicts are resolved during rebase, not during PR review

## Branch Naming Conventions

### Format Rules
- Use lowercase letters
- Use hyphens (`-`) to separate words, not underscores
- Be descriptive but concise
- Include context (agent ID, feature name, issue number)

### Examples
✅ Good:
- `agent/001/matrix-multiplication`
- `feature/statistical-analysis`
- `hotfix/division-by-zero`
- `release/1.0.0`

❌ Bad:
- `agent1` (not descriptive)
- `my_branch` (uses underscores)
- `temp` (not descriptive)
- `fix` (too vague)

## Commit Message Guidelines

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Examples
```
feat(algebra): add quadratic equation solver

Implemented solver for quadratic equations with support for
real and complex solutions.

Closes #123
```

```
fix(geometry): correct area calculation for triangles

The previous implementation didn't handle negative coordinates.
Updated to use absolute values.
```

## Merge Strategies

### For Agent Branches
- **Squash and Merge**: Recommended for cleaner history
- Combines all commits into one before merging to `develop`
- Use meaningful squash commit message

### For Feature Branches
- **Merge Commit**: Preserves feature development history
- Creates explicit merge commit showing feature integration

### For Release Branches
- **Merge Commit**: Required to track releases
- Tags the merge commit with version number

## Conflict Resolution

### When Conflicts Occur
1. **Identify Conflict Source**
   ```bash
   git status
   ```

2. **View Conflicting Changes**
   ```bash
   git diff
   ```

3. **Resolve Manually**
   - Edit conflicting files
   - Remove conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`)
   - Keep the correct changes

4. **Mark as Resolved**
   ```bash
   git add <resolved-files>
   git rebase --continue
   # or for merge conflicts
   git commit
   ```

5. **Test Resolution**
   - Run tests to ensure functionality
   - Verify the merged code works correctly

## Best Practices

### For All Agents

1. **Pull Before You Push**
   ```bash
   git pull --rebase origin develop
   ```

2. **Commit Often, Push Daily**
   - Small, focused commits
   - Push at least once per day

3. **Keep Branches Short-Lived**
   - Aim to merge within 1-3 days
   - Smaller changes are easier to review

4. **Write Descriptive Commit Messages**
   - Explain what and why, not just what changed
   - Future maintainers will thank you

5. **Test Before Pushing**
   - Run local tests
   - Ensure code builds successfully

6. **Review Your Own Code First**
   - Use `git diff` to review changes
   - Catch obvious mistakes before PR

### For Parallel Work

1. **Communicate Intent**
   - Comment on issues before starting work
   - Avoid duplicate efforts

2. **Rebase Regularly**
   - Keep your branch updated with `develop`
   - Reduces merge conflicts

3. **Review Others' PRs**
   - Understand what's being merged
   - Learn from other agents' approaches

4. **Use Draft PRs**
   - Signal work in progress
   - Get early feedback

## Branch Protection Rules

### Recommended for `main`
- ✅ Require pull request reviews before merging (1+ reviewers)
- ✅ Require status checks to pass before merging
- ✅ Require branches to be up to date before merging
- ✅ Require conversation resolution before merging
- ✅ Prevent force pushes
- ✅ Prevent deletions

### Recommended for `develop`
- ✅ Require pull request reviews before merging (1 reviewer)
- ✅ Require status checks to pass before merging
- ✅ Require branches to be up to date before merging
- ✅ Prevent force pushes
- ✅ Prevent deletions

## Visual Branching Model

```
Time →

main:      ●─────────────●─────────────●──────→
           │             │             │
           │    ┌────────┘             │
           │    │                      │
develop:   ●────●─────●─────●─────────●───────→
           │    │     │     │         │
           │    │     │     │         │
feature/a: │    └─●───●─────┘         │
           │          │               │
agent/1/x: │          └──●──●─────────┘
           │                │
agent/2/y: └────────────────●──●───────┘

Legend:
● = Commit
─ = Branch timeline
└─┘ = Merge operation
```

## Troubleshooting

### "Your branch is behind origin/develop"
```bash
git pull --rebase origin develop
```

### "Merge conflict in file.txt"
```bash
# Edit file.txt to resolve conflicts
git add file.txt
git rebase --continue
```

### "I committed to the wrong branch"
```bash
# Save your changes
git stash

# Switch to correct branch
git checkout correct-branch

# Apply your changes
git stash pop
```

### "I need to undo my last commit"
```bash
# Undo commit but keep changes
git reset --soft HEAD~1

# Undo commit and discard changes
git reset --hard HEAD~1
```

## Agent Coordination

### Task Assignment
- Each agent should be assigned specific, non-overlapping tasks
- Document task assignments in issues or project board
- Use labels to indicate which agent is working on what

### Communication Channels
- Use PR comments for code-specific discussions
- Use issue comments for task-related discussions
- Commit messages for implementation details

### Daily Sync (Recommended)
- Review merged PRs from other agents
- Update your branch from `develop`
- Communicate blockers or dependencies

## Advanced Scenarios

### Working on Multiple Tasks
```bash
# Save current work
git stash

# Switch to other task
git checkout agent/<agent-id>/<other-task>

# Return to first task
git checkout agent/<agent-id>/<first-task>
git stash pop
```

### Cherry-picking Commits
```bash
# Apply specific commit from another branch
git cherry-pick <commit-hash>
```

### Splitting Large Work
```bash
# Create parent branch for large feature
git checkout -b feature/large-feature

# Create sub-branches for agents
git checkout -b agent/001/large-feature-part1
# Agent 1 works here

git checkout feature/large-feature
git checkout -b agent/002/large-feature-part2
# Agent 2 works here

# Merge to feature branch first, then to develop
```

## Conclusion

This branching strategy enables:
- ✅ Multiple agents working simultaneously
- ✅ Clear isolation of work
- ✅ Easy conflict resolution
- ✅ Maintainable history
- ✅ Safe production deployments

Remember: When in doubt, create a new branch. Branches are cheap, merge conflicts are expensive.
