# Operations Runbook

## System Overview

Describe the application and its major components.

## How to Run Locally

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run these commands from the repository root. uv manages Python 3.12 and the local virtual environment.

```bash
uv sync --locked
uv run uvicorn app.main:app --reload
```

Run the tests with `uv run python -m pytest`.

## How to Run with Docker

```bash
docker build -t sdi4213-app .
docker run -p 8000:8000 sdi4213-app
```

## How to Run with Docker Compose

```bash
docker compose up --build
```

The image installs the application dependencies from `uv.lock` with `uv sync --locked --no-dev --no-install-project`. Development dependencies are excluded. Rebuild the image after changing dependencies or application code.

## Health Check

Open:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

## Logs

Document how to view application logs.

## Deployment

Document the deployment process later in the semester.

## Rollback

Document the rollback process later in the semester.

## Known Issues

List known issues here.

## Security Considerations

Document secrets, dependencies, scans, and other security practices.
