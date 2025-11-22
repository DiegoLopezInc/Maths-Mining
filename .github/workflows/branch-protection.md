# Branch Protection Configuration

This document describes the recommended branch protection rules for the Maths-Mining repository to enable safe parallel work by multiple agents.

## Configuration Guide

To set up branch protection rules, repository administrators should:

1. Go to repository **Settings**
2. Navigate to **Branches** in the left sidebar
3. Click **Add rule** for each protected branch

## Protection Rules for `main`

### Branch name pattern
```
main
```

### Rules to enable:
- ✅ **Require a pull request before merging**
  - Required number of approvals: `1`
  - Dismiss stale pull request approvals when new commits are pushed
  - Require review from Code Owners (if CODEOWNERS file exists)

- ✅ **Require status checks to pass before merging**
  - Require branches to be up to date before merging
  - Status checks to require: (configure based on CI/CD setup)
    - Tests
    - Linting
    - Build verification

- ✅ **Require conversation resolution before merging**
  - All review comments must be resolved

- ✅ **Require signed commits** (optional but recommended)

- ✅ **Require linear history** (optional)
  - Prevents merge commits, requires rebase or squash

- ✅ **Include administrators**
  - Apply rules to repository administrators too

- ✅ **Restrict pushes to matching branches**
  - Only allow specific people/teams to push (or none)

- ✅ **Restrict force pushes**
  - Prevents force pushes to main

- ✅ **Prevent deletion**
  - Prevents branch deletion

## Protection Rules for `develop`

### Branch name pattern
```
develop
```

### Rules to enable:
- ✅ **Require a pull request before merging**
  - Required number of approvals: `1`
  - Dismiss stale pull request approvals when new commits are pushed

- ✅ **Require status checks to pass before merging**
  - Require branches to be up to date before merging
  - Status checks to require:
    - Tests
    - Linting
    - Build verification

- ✅ **Require conversation resolution before merging**

- ✅ **Restrict force pushes**
  - Prevents force pushes to develop

- ✅ **Prevent deletion**
  - Prevents branch deletion

## Protection Rules for Agent Branches (Optional)

### Branch name pattern
```
agent/*
```

### Rules to enable:
- ✅ **Require status checks to pass before merging**
  - Basic CI checks (optional)

### Purpose:
- Provides basic safety net for agent branches
- Less restrictive than main/develop
- Allows agents to work freely while ensuring basic quality

## Wildcard Patterns for Feature Branches

You can also add rules for other branch patterns:

### Branch name pattern: `feature/*`
- ✅ Require status checks to pass before merging
- ✅ Require pull request before merging to develop

### Branch name pattern: `hotfix/*`
- ✅ Require pull request before merging
- ✅ Require status checks to pass
- ✅ Require approvals: 1+

### Branch name pattern: `release/*`
- ✅ Require pull request before merging
- ✅ Require status checks to pass
- ✅ Require approvals: 2+
- ✅ Require review from Code Owners

## Rulesets (GitHub's New Feature)

If your repository has access to Rulesets (newer feature), consider using them instead of classic branch protection rules. Rulesets provide:

- More flexible targeting
- Better organization
- Easier maintenance
- Additional rule types

### Recommended Rulesets

**Ruleset 1: Production Branches**
- **Target branches**: `main`, `release/*`
- **Rules**:
  - Require pull request
  - Require approvals (2)
  - Require status checks
  - Block force pushes
  - Block deletions

**Ruleset 2: Integration Branch**
- **Target branches**: `develop`
- **Rules**:
  - Require pull request
  - Require approvals (1)
  - Require status checks
  - Block force pushes
  - Block deletions

**Ruleset 3: Working Branches**
- **Target branches**: `agent/*`, `feature/*`
- **Rules**:
  - Require status checks
  - Allow force pushes (with lease)

## CODEOWNERS File

Create a `.github/CODEOWNERS` file to automatically request reviews from specific people:

```
# Default reviewers for everything
* @repo-owner @lead-developer

# Math algorithms
/src/algebra/ @math-expert
/src/geometry/ @geometry-specialist

# Documentation
*.md @docs-team
/docs/ @docs-team
```

## Status Checks Setup

For branch protection to require status checks, you need to set up CI/CD workflows. Example workflows to create:

### `.github/workflows/test.yml`
```yaml
name: Tests
on:
  pull_request:
    branches: [main, develop]
  push:
    branches: [main, develop]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: |
          # Add your test commands here
          echo "Tests passed"
```

### `.github/workflows/lint.yml`
```yaml
name: Lint
on:
  pull_request:
    branches: [main, develop]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run linters
        run: |
          # Add your linting commands here
          echo "Linting passed"
```

## Verification

After setting up branch protection:

1. Try to push directly to `main` - should be blocked
2. Try to push directly to `develop` - should be blocked
3. Create a test PR from agent branch to develop - should require review
4. Create a test PR from develop to main - should require review and checks

## Benefits for Multi-Agent Work

These protections ensure:
- ✅ No direct commits to protected branches
- ✅ All changes reviewed before merging
- ✅ Code quality maintained through CI checks
- ✅ History remains clean and auditable
- ✅ Agents can work independently without breaking main
- ✅ Integration branch (develop) acts as safety buffer

## Troubleshooting

### "Cannot push to protected branch"
- Expected behavior for `main` and `develop`
- Create a PR instead of pushing directly

### "Status checks are required but not configured"
- Set up CI/CD workflows first
- Or temporarily disable this requirement

### "Review required but no reviewers available"
- Ensure team members are added to repository
- Configure CODEOWNERS file
- Or reduce required reviewers to 0 for testing

## Maintenance

Review and update branch protection rules:
- When adding new branch patterns
- When CI/CD workflows change
- When team structure changes
- Every quarter for security best practices

---

**Note**: These are recommendations. Adjust based on your team size, workflow, and security requirements.
