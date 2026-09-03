# Operations Runbook

## System Overview

Describe the application and its major components.

## How to Run Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## How to Run with Docker

```bash
docker build -t sdi4213-app .
docker run -p 8000:8000 sdi4213-app
```

## How to Run with Docker Compose

```bash
docker compose up
```

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
