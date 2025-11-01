# Frontend Applications

The frontend implements data visualizations, dashboards, and configuration interfaces that make ICT Bitcoin trading signals accessible to analysts and end users.

## Planned Architecture

- **React + TypeScript** for building modular, testable UI components.
- **Vite** as the development server and build tool for fast iteration.
- **Tailwind CSS** for utility-first styling tailored to trading dashboards.
- **pnpm** (or npm/yarn) for dependency management across UI packages.

Additional micro frontends or mobile clients can live within this directory once the monorepo matures.

## Local Development Checklist

1. Copy `frontend/.env.example` to `frontend/.env` and configure environment values.
2. Install dependencies (e.g., `pnpm install`).
3. Start the development server (`pnpm dev`) once the application scaffold is added.

Consult the shared documentation in `../docs` for environment conventions and monorepo tooling guidelines.
