# Week 2 Lab Requirements: Git, GitHub, Branches, and Team Workflow

**Core rule:** no routine changes directly on `main`. Every task follows:

`Issue -> Branch -> Change -> Commit -> Push -> Pull Request -> Review -> Merge -> Update Board`

## 1. Setup
- Clone the team repository.
- Confirm your local `git config` name and email are correct.

## 2. Team Workflow Document (branch + PR)
1. Create issue "Create team workflow document," move it to In Progress.
2. Branch from `main`: `docs/team-workflow`.
3. Add `docs/team-workflow.md` covering: branching strategy, PR process, code review expectations, commit message expectations, issue tracking, project board columns.
4. Commit, push, open a PR into `main` that references the issue (`Closes #<number>`).
5. A different teammate reviews and approves.
6. Merge, delete the branch, move the issue to Done.

## 3. Individual Documentation Task (every student)
1. Create or claim an issue for a small doc task (add name/role to README, add a project goal, add a setup note, etc), move to In Progress.
2. Start from updated `main`, create your own branch.
3. Make the edit, commit, push.
4. Open a PR referencing your issue, assign a reviewer.
5. If changes are requested, update the same branch and push again.
6. Merge after approval, delete the branch, move the issue to Done.

## 4. Update the Project Board
Once PRs are merged, make sure the board reflects reality: Done, In Progress, Review, Backlog/To Do.

## 5. Update README (branch + PR)
1. Issue: "Add team workflow link to README," move to In Progress.
2. Branch: `docs/add-workflow-link`.
3. Add a `## Team Workflow` section linking to `docs/team-workflow.md`.
4. Commit, push, open PR, get review, merge, delete branch, move issue to Done.

## Deliverables to Submit
1. Link to team GitHub repository: https://github.com/jakeryderv/lychee/tree/main
2. Link to GitHub Project board : https://github.com/jakeryderv/lychee/projects
3. Link to the merged PR for the team workflow document: https://github.com/jakeryderv/lychee/pulls?q=is%3Apr+is%3Aclosed
4. Links to each student's individual PR: https://github.com/jakeryderv/lychee/pulls?q=is%3Apr+is%3Aclosed
5. Screenshot or link showing at least one code review comment
6. Link to the PR that added the workflow section to the README: https://github.com/jakeryderv/lychee/pulls?q=is%3Apr+is%3Aclosed
7. Updated README containing the link to the team workflow document (done)
8. Short team reflection: 

## Grading (100 pts total)
| Category | Points |
|---|---|
| Repo cloned, Git configured | 10 |
| Branching workflow followed correctly | 15 |
| Team workflow document created via branch/PR | 15 |
| Issue created and linked to PR | 10 |
| PR opened, reviewed, merged | 15 |
| Each student completed individual branch/PR | 15 |
| Code review comments completed | 10 |
| Project board updated | 10 |

## Avoid
- Editing `main` directly
- Skipping `git pull` before branching
- Vague commit messages ("update," "stuff")
- PRs with no description
- Merging without review
- Vague issue titles
- Forgetting to move issues on the board
