"""Application settings powered by Pydantic BaseSettings."""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    """Service configuration loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    app_name: str = Field(default="ICT Backend API")
    environment: str = Field(default="local")
    debug: bool = Field(default=False)
    api_prefix: str = Field(default="/api")
    log_level: str = Field(default="INFO")


@lru_cache
def get_settings() -> AppSettings:
    """Return a cached instance of the application settings."""
    return AppSettings()


__all__ = ["AppSettings", "get_settings"]
