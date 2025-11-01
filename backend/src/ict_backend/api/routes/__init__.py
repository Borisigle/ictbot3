"""API router registration."""

from fastapi import FastAPI

from ict_backend.api.routes import health


def include_api_routes(app: FastAPI, api_prefix: str) -> None:
    """Attach all API routers to the FastAPI application."""
    app.include_router(health.router, prefix=api_prefix)


__all__ = ["include_api_routes"]
