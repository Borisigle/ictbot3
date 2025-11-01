"""Repository responsible for retrieving health information."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class HealthRecord:
    """Data transfer object representing a health check result."""

    status: str
    checked_at: datetime


class HealthRepository:
    """Provide access to health data sources."""

    def fetch_status(self) -> HealthRecord:
        """Return the current health status of the service."""
        return HealthRecord(status="ok", checked_at=datetime.now(tz=timezone.utc))
