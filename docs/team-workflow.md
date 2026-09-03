# Team Workflow

## Branching Strategy

Our team will not make routine project changes directly on the `main` branch. Each task will be completed on a separate branch.

Before creating a branch, each team member should switch to `main` and pull the latest changes.

```bash
git checkout main
git pull
git checkout -b docs/example-branch
```

Branch name examples:

- `feature/add-home-page`
- `docs/update-readme`
- `fix/readme-typo`
- `test/add-basic-tests`

## Pull Request Process

Each completed task should be submitted using a pull request.

Before opening a pull request, the team member should:

- confirm they are working on a branch, not `main`
- pull the latest version of `main` before starting the task
- complete the assigned work
- confirm the project still works
- commit changes with a clear message
- push the branch to GitHub
- open a pull request into `main`

## Code Review Expectations

At least one teammate should review each pull request before it is merged.

Reviewers should check:

- Does the change match the issue?
- Was the work completed on a branch?
- Is the code or documentation clear?
- Are unnecessary files included?
- Are there obvious errors?
- Are tests needed?

## Commit Message Expectations

Commit messages should be short and specific.

Good examples:

- `Add project charter`
- `Update README with team roles`
- `Create initial app folder`
- `Fix typo in setup instructions`

Weak examples:

- `update`
- `stuff`
- `final`
- `fixed things`

## Issue Tracking

The team will use GitHub Issues to track work. Each issue should have a clear title, description, and assignee when possible.

## Project Board

The team will use the project board to track work status.

Suggested columns:

- Backlog
- To Do
- In Progress
- Review
- Done
