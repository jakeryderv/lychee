# SDI 4213 DevOps Starter Project

## Project Description

This is the starter repository for the SDI 4213-980 DevOps - CI/CD semester project. Teams will use this repository to practice Git, GitHub, branching, pull requests, automated testing, CI/CD, containerization, deployment, Infrastructure as Code, Kubernetes, and operations documentation.

## Team Members

- [@Jake](https://github.com/jakeryderv) - Head Developer
- [@Mei](https://github.com/mei-morrow) - Backend Developer
- [@Sumner](https://github.com/sumnerkirby) - Front End Developer


## Planned Technology Stack

- Programming language: Python
- Framework: FastAPI
- Testing framework: Pytest
- CI/CD platform: GitHub Actions
- Containerization: Docker
- Multi-service environment: Docker Compose
- Infrastructure as Code: OpenTofu or Terraform
- Orchestration: Kubernetes
- Deployment target: To be selected by the team

## Project Goals

- Build a small working web application or API.
- Use GitHub Issues, branches, pull requests, and code reviews.
- Add automated testing and continuous integration.
- Containerize and deploy the application.
- Document the complete DevOps workflow.

## Team Workflow

Our team workflow will be documented in [docs/team-workflow.md](docs/team-workflow.md).

## Current Status

Week 1-2: Project setup, documentation, GitHub workflow, and branching practice.

## Running the Application Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open the app in your browser:

```text
http://127.0.0.1:8000
```

View the automatic API docs:

```text
http://127.0.0.1:8000/docs
```

## Running Tests

```bash
pytest
```

## Basic Git Workflow

For this course, do not make routine changes directly on `main`.

Use this workflow:

```text
Issue → Branch → Change → Commit → Push → Pull Request → Review → Merge → Update Board
```
