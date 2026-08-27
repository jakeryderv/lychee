# Project Charter: Lychee

**Course:** SDI 4213/5213-980, DevOps CI/CD, Fall 2026
**Project type:** Semester-long group project
**Course project option:** Option 1, Inventory Tracker

---

## Project Name
Lychee

## Team Members
Fill in before submitting.

| Name | GitHub Handle | Role |
|---|---|---|
| [Name] | [@handle] | [Application lead / Pipeline lead / Platform lead] |
| [Name] | [@handle] | [Application lead / Pipeline lead / Platform lead] |
| [Name] | [@handle] | [Application lead / Pipeline lead / Platform lead] |

## Application Purpose
A multi-venue restaurant inventory tracker that lets rotating staff log stock counts in the informal units they already use, tracks bar, dry, and cold goods as distinct categories, and keeps two venues sharing one physical kitchen in sync in close to real time.

## Target Users
**Primary:** Rotating front of house and back of house staff recording counts during or between shifts.

**Secondary:** Shift leads, kitchen managers, and owners who review stock, transfer between venues, and reconcile costs.

## Primary Features
- Fast count entry in natural units, such as two thirds of a bottle or three heads of lettuce
- Three inventory categories, bar, dry, and cold, each with category-specific units and count cadence
- Shared-pool and per-venue stock tracking with transfers
- Waste logging with reason codes
- Low-stock reporting based on per-venue par levels
- Live updates pushed to every connected device

## Explicitly Out of Scope
- POS or supplier API integration
- Purchase order generation and vendor management
- Demand forecasting or par level suggestions
- Real user accounts, password reset, or role-based permissions beyond a staff PIN and a manager flag
- Barcode scanning, photo upload, offline-first sync
- Recipe costing and menu engineering

## Technology Stack
Python 3.12, FastAPI, SQLAlchemy, Alembic, PostgreSQL 16, a vanilla JS and HTML frontend, Pytest, Docker, Docker Compose, GitHub Actions, Trivy, Dependabot, CodeQL, Terraform or OpenTofu, Kubernetes (kind), Google Cloud Run and Artifact Registry, and a free serverless Postgres provider.

## Repository Link
[https://github.com/<org-or-user>/lychee]

---

## Open Items to Confirm With the Instructor
1. Confirm that Lychee, as a multi-venue extension of Option 1, does not require a separate proposal.
2. Confirm the team size and that shared testing and documentation responsibilities (rather than a dedicated owner for each) satisfy the course expectations.
3. Confirm the deployment plan, Google Cloud Run with a free serverless Postgres provider, and get written approval before attaching a billing account.
