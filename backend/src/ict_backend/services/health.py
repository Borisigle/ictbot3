"""Business logic for the health endpoint."""

from ict_backend.core.settings import AppSettings
from ict_backend.repositories.health import HealthRecord, HealthRepository
from ict_backend.schemas.health import HealthStatus


class HealthService:
    """Service responsible for orchestrating health checks."""

    def __init__(self, repository: HealthRepository, settings: AppSettings) -> None:
        self._repository = repository
        self._settings = settings

    def get_health_status(self) -> HealthStatus:
        """Return the current health status of the application."""
        record: HealthRecord = self._repository.fetch_status()
        return HealthStatus(
            status=record.status,
            environment=self._settings.environment,
            timestamp=record.checked_at,
            application=self._settings.app_name,
        )
