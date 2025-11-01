"""Dependencies for health-related resources."""

from fastapi import Depends

from ict_backend.core.settings import AppSettings, get_settings
from ict_backend.repositories.health import HealthRepository
from ict_backend.services.health import HealthService


def get_health_repository() -> HealthRepository:
    """Return the repository responsible for health information."""
    return HealthRepository()


def get_health_service(
    repository: HealthRepository = Depends(get_health_repository),
    settings: AppSettings = Depends(get_settings),
) -> HealthService:
    """Return an instance of the health service."""
    return HealthService(repository=repository, settings=settings)
