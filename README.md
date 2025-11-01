# ICT BTC Signal Bot Monorepo

Welcome to the ICT BTC Signal Bot monorepo. This repository hosts every component needed to research, build, and operate an automated signal generation and delivery platform inspired by the ICT methodology for Bitcoin trading. The goal is to provide an end-to-end system that ingests market data, evaluates ICT-informed strategies, surfaces actionable insights, and delivers them to end users through modern interfaces.

## Vision

- **Research-first**: Iterate quickly on quantitative hypotheses rooted in the ICT framework.
- **Production-ready**: Provide reliable infrastructure capable of scheduled analysis, live monitoring, and alert delivery.
- **Collaborative**: Standardize tooling, documentation, and configuration to help contributors work effectively across the stack.

## Repository Structure

```
backend/          Core services for data ingestion, backtesting, and signal generation.
frontend/         Web clients and experience layers that consume exposure from the backend.
infra/            Infrastructure-as-code for cloud resources, observability, and deployment.
config/           Shared configuration, schemas, and linting/tooling presets.
docs/             Living documentation covering architecture, environments, and runbooks.
```

Each directory contains its own README to describe intended responsibilities, setup instructions, and future plans.

## Technology Stack Overview

| Component | Primary Technologies | Purpose |
|-----------|----------------------|---------|
| **Backend** | Python (FastAPI), Celery, Pandas, PostgreSQL | Market data ingestion, strategy engines, scheduling, and API surfaces. |
| **Frontend** | TypeScript, React, Vite, Tailwind CSS | Analyst dashboard, signal explorer, and configuration UI. |
| **Infrastructure** | Terraform, Docker, GitHub Actions | Provisioning cloud resources, CI/CD pipelines, container orchestration. |
| **Shared Tooling** | Poetry, pnpm, pre-commit, EditorConfig | Consistent linting, formatting, and dependency management across the monorepo. |

> The above stack represents the baseline plan. Actual implementation choices can evolve as the project matures, but the monorepo should continue to coordinate shared tooling and conventions.

## Environment & Configuration Strategy

Environment variables are organized into three groups:

1. **Shared (`env/shared`)** – Values used by multiple services (e.g., data provider credentials, logging levels). These live in the root `.env` file and should be namespaced with a `GLOBAL_` prefix.
2. **Service-specific (`backend/.env`, `frontend/.env`, `infra/.env`)** – Variables unique to each service. Templates for these files should extend the root `.env.example` by adding service-prefixed keys (e.g., `BACKEND_DATABASE_URL`, `FRONTEND_PUBLIC_API_URL`).
3. **Secret Overrides** – Use deployment-specific secret managers (AWS SSM, Doppler, etc.) to override sensitive values in non-local environments. Do not commit actual secrets.

Refer to [`docs/environment.md`](docs/environment.md) for detailed guidance on naming conventions, local development setup, and secret management policies.

Shared linting and formatter rules reside in [`config/`](config/README.md). Future service packages can import or reference these settings to avoid duplication.

## Tooling & Developer Experience

- **Git Ignore** – `.gitignore` excludes build outputs, virtual environments, and editor cruft.
- **EditorConfig** – `.editorconfig` enforces consistent indentation, line endings, and character encoding.
- **pre-commit** – `.pre-commit-config.yaml` defines hooks for formatting, linting, and security checks. Install with `pre-commit install`.
- **Environment Templates** – `.env.example` demonstrates required environment variables and how they are grouped.

Additional tooling definitions (formatters, linters, container templates) should live beside the services that rely on them and reference shared presets from `config/` where applicable.

## Getting Started

1. **Clone the repo** and install the pre-commit hooks:
   ```bash
   pre-commit install
   ```
2. **Copy environment templates** into service-specific `.env` files, then adjust values for your local setup:
   ```bash
   cp .env.example .env
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env
   cp infra/.env.example infra/.env
   ```
3. **Review service READMEs** inside `backend/`, `frontend/`, and `infra/` for technology-specific instructions.
4. **Read the docs** under `docs/` to understand architectural decisions and operational guidelines.

With the foundational scaffold in place, you can now implement features, pipelines, and infrastructure incrementally while keeping configuration consistent across the monorepo.
