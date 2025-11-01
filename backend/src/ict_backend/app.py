"""Application factory and ASGI entrypoint for the ICT backend."""

from fastapi import FastAPI

from ict_backend.api.routes import include_api_routes
from ict_backend.core.errors import register_exception_handlers
from ict_backend.core.logging import configure_logging
from ict_backend.core.settings import get_settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    settings = get_settings()
    configure_logging(settings)

    app = FastAPI(title=settings.app_name, debug=settings.debug)

    include_api_routes(app, settings.api_prefix)
    register_exception_handlers(app)

    return app


app = create_app()
