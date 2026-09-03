"""Starter FastAPI application for SDI 4213 DevOps - CI/CD."""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SDI 4213 DevOps Project")


class Item(BaseModel):
    """Simple item model for starter inventory/task examples."""

    id: int
    name: str
    status: str = "new"


sample_items = [
    Item(id=1, name="Example item", status="new"),
    Item(id=2, name="Second example item", status="in progress"),
]


@app.get("/")
def read_root():
    """Return a simple welcome message."""
    return {"message": "Welcome to the SDI 4213 DevOps project"}


@app.get("/health")
def health_check():
    """Return basic application health status."""
    return {"status": "ok"}


@app.get("/items")
def list_items():
    """Return a starter list of project items."""
    return sample_items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Return one item by ID or a not-found message."""
    for item in sample_items:
        if item.id == item_id:
            return item
    return {"error": "Item not found"}
