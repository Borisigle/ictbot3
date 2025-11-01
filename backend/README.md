# Backend Service

The backend hosts data ingestion pipelines, strategy simulation engines, and APIs that expose ICT-based Bitcoin trading signals to downstream consumers.

## Planned Architecture

- **FastAPI** for synchronous APIs and websocket streaming of actionable signals.
- **Celery** workers orchestrated via a message broker (Redis / RabbitMQ) for scheduled data ingestion and strategy evaluation.
- **PostgreSQL** (with TimescaleDB extensions) as the primary persistence layer for historical candles, strategy metadata, and analytics.
- **Pandas** and numerical libraries for backtesting, validation, and feature engineering.

Future iterations may introduce specialized microservices (e.g., real-time alerting) while preserving a cohesive deployment model within this monorepo.

## Local Development Checklist

1. Copy `backend/.env.example` to `backend/.env` and configure service-specific variables.
2. Install dependencies (e.g., `poetry install`) once the project scaffolding is in place.
3. Run unit and integration tests before committing changes.

Refer to the root documentation (`../docs`) for guidance on environment variables, dependency management, and shared tooling conventions.
