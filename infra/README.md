# Infrastructure

This directory contains infrastructure-as-code, provisioning scripts, and operational automation that support the ICT BTC Signal Bot platform.

## Planned Components

- **Terraform** modules for cloud resources (compute, networking, secrets, observability).
- **Docker** build definitions used to package backend and auxiliary services.
- **GitHub Actions** or other CI/CD pipelines for automated builds, tests, and deployments.
- **Monitoring & alerts** configuration (e.g., Prometheus, Grafana, PagerDuty integrations).

## Local Development Checklist

1. Copy `infra/.env.example` to `infra/.env` and configure required credentials (provider, state backends, etc.).
2. Install Terraform and other CLI tools referenced by modules.
3. Use remote state backends (S3, GCS) for shared environments; local state is acceptable for sandbox experiments.

Refer to documentation in `../docs` for environment policies and shared configuration patterns.
