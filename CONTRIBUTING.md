# Contributing to Maths-Mining

Thank you for your interest in contributing to Maths-Mining! This document provides guidelines for contributing to the project, especially for agents working in parallel.

## Quick Start for Agents

### 1. Get Set Up
```bash
# Clone the repository (if not already done)
git clone https://github.com/DiegoLopezInc/Maths-Mining.git
cd Maths-Mining

# Create your working branch
git checkout develop
git pull origin develop
git checkout -b agent/<your-agent-id>/<task-name>
```

### 2. Make Your Changes
- Write clean, well-documented code
- Follow existing code style and conventions
- Keep changes focused and atomic

### 3. Test Your Changes
- Run all existing tests
- Add new tests for new functionality
- Verify your changes work as expected

### 4. Commit Your Work
```bash
git add .
git commit -m "feat(scope): description of your changes"
```

### 5. Push and Create PR
```bash
git push origin agent/<your-agent-id>/<task-name>
```
Then create a Pull Request targeting the `develop` branch.

## Branching Strategy

Please read our [Branching Strategy](BRANCHING_STRATEGY.md) document for detailed information on:
- Branch types and naming conventions
- Workflow for parallel agent work
- Conflict resolution strategies
- Best practices

### Quick Reference

**Branch Types:**
- `main` - Production-ready code
- `develop` - Integration branch
- `agent/<id>/<task>` - Agent working branches
- `feature/<name>` - Feature development
- `hotfix/<issue>` - Critical fixes
- `release/<version>` - Release preparation

**Create agent branch:**
```bash
git checkout develop
git pull origin develop
git checkout -b agent/<agent-id>/<task-name>
```

**Keep branch updated:**
```bash
git fetch origin develop
git rebase origin/develop
```

## Code Style Guidelines

### General Principles
- Write clear, self-documenting code
- Use meaningful variable and function names
- Keep functions small and focused
- Avoid code duplication
- Comment complex logic

### Python (if applicable)
- Follow PEP 8 style guide
- Use type hints where appropriate
- Write docstrings for all public functions
- Maximum line length: 88 characters (Black formatter)

### JavaScript (if applicable)
- Follow ESLint configuration
- Use const/let, not var
- Use modern ES6+ syntax
- Write JSDoc comments for functions

### Documentation
- Use clear, concise language
- Include examples where helpful
- Keep documentation up to date with code changes
- Use proper Markdown formatting

## Commit Message Format

We follow the Conventional Commits specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only changes
- `style`: Code style changes (formatting, missing semicolons, etc)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvement
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to build process or auxiliary tools

### Examples
```
feat(algebra): add polynomial factorization

Implemented algorithm for factoring polynomials up to degree 4.
Includes support for complex coefficients.

Closes #42
```

```
fix(geometry): correct circle area calculation

Fixed floating point precision issue in area calculation.
```

```
docs(readme): update installation instructions

Added Python 3.9+ requirement and clarified setup steps.
```

## Pull Request Process

1. **Create PR**: Open a pull request from your agent branch to `develop`
2. **Fill Template**: Complete the PR template with all required information
3. **Self-Review**: Review your own changes before requesting review
4. **Automated Checks**: Ensure all CI/CD checks pass
5. **Address Feedback**: Respond to review comments promptly
6. **Merge**: Once approved, squash and merge into `develop`
7. **Cleanup**: Delete your branch after merging

### PR Checklist
- [ ] Branch is up to date with `develop`
- [ ] All tests pass locally
- [ ] Code follows style guidelines
- [ ] Documentation is updated
- [ ] PR template is filled out
- [ ] Self-review completed

## Working with Multiple Agents

### Coordination
- Check existing issues and PRs before starting work
- Comment on issues to claim tasks
- Use draft PRs to signal work in progress
- Communicate dependencies in PR descriptions

### Avoiding Conflicts
- Keep branches short-lived (merge within 1-3 days)
- Rebase frequently from `develop`
- Work on isolated, independent tasks when possible
- Coordinate with other agents on shared files

### Handling Conflicts
1. Pull latest changes: `git fetch origin develop`
2. Rebase your branch: `git rebase origin/develop`
3. Resolve conflicts in your editor
4. Mark resolved: `git add <files>`
5. Continue: `git rebase --continue`
6. Force push: `git push --force-with-lease`

## Testing

### Running Tests
```bash
# Add appropriate test commands for your project
# Examples:
python -m pytest tests/
npm test
go test ./...
```

### Writing Tests
- Write tests for all new functionality
- Follow existing test patterns
- Use descriptive test names
- Include edge cases and error conditions
- Aim for high code coverage

## Documentation

### What to Document
- Public APIs and functions
- Complex algorithms or logic
- Setup and installation instructions
- Usage examples
- Configuration options

### Where to Document
- **Code Comments**: For implementation details
- **Docstrings/JSDoc**: For function documentation
- **README.md**: For project overview and setup
- **Separate Docs**: For extensive guides

## Getting Help

### Resources
- [Branching Strategy](BRANCHING_STRATEGY.md) - Detailed git workflow
- [README.md](README.md) - Project overview
- GitHub Issues - Known issues and feature requests

### Questions?
- Open a discussion issue
- Comment on relevant PRs
- Review existing documentation

## Code Review Guidelines

### For Authors
- Keep PRs small and focused
- Provide context in PR description
- Respond to feedback constructively
- Make requested changes promptly

### For Reviewers
- Be constructive and respectful
- Focus on code quality and correctness
- Suggest improvements, don't demand perfection
- Approve when requirements are met

## Recognition

All contributors are valued! Your contributions will be:
- Acknowledged in release notes
- Tracked in git history
- Appreciated by the community

## License

By contributing to Maths-Mining, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to Maths-Mining! Your work helps make this project better for everyone.
