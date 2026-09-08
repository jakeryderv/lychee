FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:0.12.5 /uv /bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project

COPY app ./app

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
