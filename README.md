

Readme · MD
Lychee
Logo: app/static/lychee-logo.svg

A multi-venue restaurant inventory tracker that lets rotating staff log stock counts in the natural units they already use (a bottle, a case, a head of lettuce), keeps bar, dry, and cold goods as distinct categories, and keeps two venues sharing one physical kitchen in sync in close to real time.

Team Members
[Name] ([@GitHub handle])
[Name] ([@GitHub handle])
[Name] ([@GitHub handle])
Who This Is For
Primary users: Rotating front of house and back of house staff recording counts during or between shifts.

Secondary users: Shift leads, kitchen managers, and owners who review stock, transfer between venues, and reconcile costs.

Planned Technology Stack
Backend: Python 3.12, FastAPI, SQLAlchemy, Alembic
Database: PostgreSQL 16
Frontend: Server-rendered HTML with a small amount of vanilla JS
Testing: Pytest
Containers: Docker, Docker Compose
CI/CD: GitHub Actions
Security: Trivy, Dependabot, CodeQL
Infrastructure as code: Terraform or OpenTofu
Orchestration: Kubernetes (kind)
Deployment: Google Cloud Run and Artifact Registry, with a free serverless Postgres provider
What Lychee Does Not Do
This is a course project, scoped deliberately. The following are out of scope:

POS or supplier API integration
Purchase order generation and vendor management
Demand forecasting or par level suggestions
Real user accounts, password reset, or role-based permissions beyond a staff PIN and a manager flag
Barcode scanning, photo upload, offline-first sync
Recipe costing and menu engineering
Project Status
Week 1: project charter and repository setup. See docs/charter.md for the full charter.

Getting Started
Setup and local run instructions will be added once the application skeleton exists (Week 3).

License
[MIT or similar license, to be added]



