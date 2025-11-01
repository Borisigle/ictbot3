# System Architecture (Draft)

This document will capture the evolving architecture of the ICT BTC Signal Bot platform.

## Initial Component Overview

1. **Data Ingestion Layer**
   - Scheduled jobs pull historical and real-time market data from crypto exchanges and liquidity providers.
   - Data is normalized and stored in the analytics database for downstream processing.

2. **Strategy Engine**
   - Implements ICT-based trading logic for signal generation.
   - Supports backtesting, paper trading, and live evaluation modes.

3. **API Gateway / Backend Services**
   - Exposes REST and WebSocket endpoints for consumers (frontends, integrations).
   - Handles authentication, authorization, and rate limiting.

4. **Frontend Clients**
   - Dashboards for analysts to review signals, configure alerts, and monitor performance.
   - Interfaces for end users to subscribe to alerts.

5. **Infrastructure & Operations**
   - Terraform-managed cloud resources, observability stack, and CI/CD pipelines.
   - Automated deployments ensure consistency across environments.

As the system evolves, expand this document with diagrams, data flow descriptions, and service-level design decisions.
