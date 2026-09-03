# Contributing Guidelines

This repository uses a branch-based workflow.

## Required Workflow

```text
Issue → Branch → Change → Commit → Push → Pull Request → Review → Merge → Update Board
```

## Branching Rules

Do not make routine changes directly on `main`.

Before starting work:

```bash
git checkout main
git pull
git checkout -b docs/example-branch
```

Use branch names such as:

- `docs/update-readme`
- `feature/add-home-page`
- `fix/readme-typo`
- `test/add-basic-tests`

## Pull Requests

Every change should be submitted through a pull request. Each pull request should:

- describe the change
- reference the related issue
- request at least one reviewer
- pass checks before merging, when checks are available

## Commit Messages

Use clear commit messages.

Good examples:

- `Add project charter`
- `Update README with team roles`
- `Create initial app folder`
- `Fix typo in setup instructions`

Weak examples:

- `update`
- `stuff`
- `fixed things`
