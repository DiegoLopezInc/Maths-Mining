# Maths-Mining
Mining Mathematics to solve problems.

## About

Maths-Mining is a collaborative project for developing mathematical algorithms and tools. This repository supports multiple agents working in parallel on various mathematical problems and implementations.

## For Contributors

### Quick Start for Agents

If you're an agent assigned to work on a task:

1. **Read the Quick Reference**: See [AGENT_QUICK_REFERENCE.md](AGENT_QUICK_REFERENCE.md) for essential commands
2. **Understand the Workflow**: Read [BRANCHING_STRATEGY.md](BRANCHING_STRATEGY.md) for the complete branching model
3. **Follow Guidelines**: Check [CONTRIBUTING.md](CONTRIBUTING.md) for contribution standards

### Documentation

- **[AGENT_QUICK_REFERENCE.md](AGENT_QUICK_REFERENCE.md)** - Quick command reference for daily agent workflow
- **[BRANCHING_STRATEGY.md](BRANCHING_STRATEGY.md)** - Complete git branching strategy for parallel work
- **[BRANCHING_TREE_VISUAL.md](BRANCHING_TREE_VISUAL.md)** - Visual diagrams of the branching structure
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines and code standards

## Repository Structure

```
main          - Production-ready code
develop       - Integration branch for ongoing development
agent/*       - Agent-specific working branches
feature/*     - Feature development branches
hotfix/*      - Critical production fixes
release/*     - Release preparation branches
```

## Getting Started

```bash
# Clone the repository
git clone https://github.com/DiegoLopezInc/Maths-Mining.git
cd Maths-Mining

# Start working on a task (for agents)
git checkout develop
git pull origin develop
git checkout -b agent/<your-id>/<task-name>

# Make changes, then commit and push
git add .
git commit -m "feat(scope): description"
git push origin agent/<your-id>/<task-name>
```

## Parallel Development

This repository is designed for multiple agents to work simultaneously:

- Each agent works on isolated branches
- Regular syncing with `develop` branch prevents conflicts
- Pull requests are reviewed before merging
- Clear branching structure ensures organized collaboration

See [BRANCHING_STRATEGY.md](BRANCHING_STRATEGY.md) for details on how multiple agents can work together efficiently.

## License

This project is open source and available for collaborative mathematical development.
