"""Dependency injection helpers for the ICT backend."""

from .health import get_health_repository, get_health_service

__all__ = ["get_health_repository", "get_health_service"]
