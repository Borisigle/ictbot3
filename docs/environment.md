# Environment Management

This document standardizes how environment variables are organized, named, and loaded across the ICT BTC Signal Bot monorepo.

## Guiding Principles

1. **No secrets in Git**: Only commit example values or placeholder keys. Use secret managers for real credentials.
2. **Namespacing**: Prefix variables based on their scope (`GLOBAL_`, `BACKEND_`, `FRONTEND_`, `INFRA_`).
3. **Single source of truth**: The root `.env` file holds shared values. Service-specific files extend the root configuration.
4. **Parallels between environments**: Maintain consistent variable names across development, staging, and production to simplify deployments and automation.

## Directory Layout

```
.env.example      Root template containing shared variables and documentation comments.
backend/.env      Service-specific overrides for backend processes.
frontend/.env     Environment values for UI clients.
infra/.env        Credentials and settings for infrastructure tooling.
```

Each service ships with its own `.env.example` that lists required variables. When onboarding, copy these templates, fill in local values, and avoid checking the populated files into version control.

## Loading Strategy

1. **Local Development**
   - Copy the root `.env.example` to `.env` and populate shared values.
   - Copy the relevant service templates to `.env` files inside each directory.
   - Use tooling such as `direnv`, `dotenv-cli`, or framework-specific loaders to merge root and service-level configuration.

2. **Continuous Integration**
   - CI pipelines should inject secrets via environment variables or secret stores (e.g., GitHub OIDC → AWS SSM).
   - Use the same variable names defined in the templates to prevent drift between local and CI environments.

3. **Production**
   - Provision a centralized secret manager (AWS SSM, AWS Secrets Manager, HashiCorp Vault, etc.).
   - Store secrets under the same keys as the templates while keeping non-sensitive defaults in version control.
   - Infrastructure modules should reference these secrets securely and avoid writing to `.env` files on disk.

## Variable Namespaces

| Namespace  | Purpose | Examples |
|-----------|---------|----------|
| `GLOBAL_` | Shared values across services. | `GLOBAL_LOG_LEVEL`, `GLOBAL_DATA_PROVIDER_URL` |
| `BACKEND_` | Backend-only configuration. | `BACKEND_DATABASE_URL`, `BACKEND_REDIS_URL` |
| `FRONTEND_` | Frontend build-time values. | `FRONTEND_PUBLIC_API_URL`, `FRONTEND_ENABLE_ANALYTICS` |
| `INFRA_` | Infrastructure tooling credentials. | `INFRA_TERRAFORM_BACKEND_BUCKET`, `INFRA_AWS_ACCESS_KEY_ID` |

Keep shared values in the root `.env` file and reference them from services where appropriate (e.g., the backend may reuse `GLOBAL_DATA_PROVIDER_URL`). Services should only own variables they are responsible for managing.

## Secret Rotation & Auditing

- Rotate provider keys and tokens regularly.
- Record secret ownership and rotation cadence inside `docs/runbooks/` (to be created).
- Use automated scanners (e.g., `detect-secrets`) via pre-commit hooks to prevent accidental commits of sensitive data.

Adhering to these conventions ensures a consistent developer experience and lowers the risk of configuration drift across the monorepo.
