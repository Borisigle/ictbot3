"""Structured logging configuration for the ICT backend."""

from __future__ import annotations

import copy
import logging
import logging.config
from typing import Any, Dict

from ict_backend.core.settings import AppSettings

LOGGING_CONFIG: Dict[str, Any] = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        }
    },
    "loggers": {
        "": {"handlers": ["console"], "level": "INFO"},
        "uvicorn": {"handlers": ["console"], "level": "INFO"},
        "uvicorn.error": {"handlers": ["console"], "level": "INFO"},
        "uvicorn.access": {"handlers": ["console"], "level": "INFO"},
    },
}

_CONFIGURED = False


def configure_logging(settings: AppSettings) -> None:
    """Apply the logging configuration using the provided settings."""
    global _CONFIGURED

    if _CONFIGURED:
        return

    log_config = copy.deepcopy(LOGGING_CONFIG)
    root_logger_level = settings.log_level.upper()

    for logger_name in log_config["loggers"].keys():
        log_config["loggers"][logger_name]["level"] = root_logger_level

    logging.config.dictConfig(log_config)
    logging.getLogger(__name__).debug("Logging configured with level %s", root_logger_level)

    _CONFIGURED = True


__all__ = ["configure_logging"]
