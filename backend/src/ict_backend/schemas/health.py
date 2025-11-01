"""Pydantic models for health resources."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class HealthStatus(BaseModel):
    """Response model for the health endpoint."""

    model_config = ConfigDict(populate_by_name=True)

    status: Literal["ok", "degraded"] = Field(default="ok", examples=["ok"])
    environment: str = Field(..., examples=["local"])
    timestamp: datetime = Field(..., examples=["2024-01-01T00:00:00Z"])
    application: str = Field(..., examples=["ICT Backend API"])
