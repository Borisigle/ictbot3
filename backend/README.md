# Backend Service

The backend provides synchronous APIs, upcoming background workers, and shared services that power ICT-informed Bitcoin trading signals.

## Project Structure

```
backend/
  ├── pyproject.toml         # Poetry project definition and tooling configuration
  ├── .env.example           # Template for service-specific environment variables
  ├── src/ict_backend/       # FastAPI application package
  │     ├── api/             # Route registrations and API modules
  │     ├── core/            # Settings, logging, and error handling utilities
  │     ├── dependencies/    # Dependency injection helpers
  │     ├── repositories/    # Data access abstractions
  │     ├── schemas/         # Pydantic models for requests/responses
  │     └── services/        # Business logic orchestrating repositories
  └── tests/                 # Pytest suites exercising the API and services
```

## Getting Started

1. **Prepare environment variables**

   ```bash
   cp backend/.env.example backend/.env
   ```

   Override values in `backend/.env` as needed for your local environment.

2. **Install dependencies**

   ```bash
   cd backend
   poetry install
   ```

3. **Run the development server**

   ```bash
   poetry run uvicorn ict_backend.app:app --reload
   ```

   The health check is available at `http://localhost:8000/api/health`.

4. **Run tooling**

   ```bash
   poetry run ruff check .        # Linting
   poetry run black --check .     # Formatting
   poetry run mypy .              # Static type checks
   poetry run pytest              # Test suite
   ```

## Architectural Notes

- FastAPI application creation happens inside `ict_backend.app.create_app`, enabling composable dependency injection and testability.
- `AppSettings` (in `core/settings.py`) centralizes configuration with a cached accessor so routes and services share consistent settings.
- Structured logging is configured once during application startup via `core/logging.py` and applies to Uvicorn as well as service loggers.
- Custom exception handlers in `core/errors.py` normalize application, HTTP, and validation errors into consistent JSON responses.

Future iterations will introduce persistence layers, domain services, and asynchronous task processing while keeping the modular boundaries established here.
