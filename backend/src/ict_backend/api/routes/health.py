"""Health check endpoint."""

from fastapi import APIRouter, Depends

from ict_backend.dependencies.health import get_health_service
from ict_backend.schemas.health import HealthStatus
from ict_backend.services.health import HealthService

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("", response_model=HealthStatus, summary="Readiness probe")
def health_check(service: HealthService = Depends(get_health_service)) -> HealthStatus:
    """Return basic service health information."""
    return service.get_health_status()
