"""Centralized error and exception handling utilities."""

from __future__ import annotations

import logging
from typing import Any, Dict

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

logger = logging.getLogger(__name__)


class ApplicationError(Exception):
    """Base exception for domain-specific errors."""

    def __init__(self, message: str, *, status_code: int = 400, details: Dict[str, Any] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.details = details or {}


async def _handle_application_error(_: Request, exc: ApplicationError) -> JSONResponse:
    logger.warning("Application error raised", extra={"details": exc.details, "message": exc.message})
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.message, "details": exc.details},
    )


async def _handle_http_exception(_: Request, exc: StarletteHTTPException) -> JSONResponse:
    logger.info("HTTP exception encountered", extra={"status_code": exc.status_code})
    return JSONResponse(status_code=exc.status_code, content={"error": exc.detail})


async def _handle_validation_error(_: Request, exc: RequestValidationError) -> JSONResponse:
    logger.debug("Request validation error", extra={"errors": exc.errors()})
    return JSONResponse(status_code=422, content={"error": "Invalid request", "details": exc.errors()})


def register_exception_handlers(app: FastAPI) -> None:
    """Register custom exception handlers for the FastAPI app."""
    app.add_exception_handler(ApplicationError, _handle_application_error)
    app.add_exception_handler(StarletteHTTPException, _handle_http_exception)
    app.add_exception_handler(RequestValidationError, _handle_validation_error)


__all__ = ["ApplicationError", "register_exception_handlers"]
