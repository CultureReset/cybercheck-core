# Deployment, Observability and Operations

Production operation requires health visibility across workflows, connectors, projections, runtimes, providers and customer-facing surfaces.

## Source-grounded rules
- Durable workflows should not depend on a browser tab staying open.
- Usage and worker activity can be metered separately from subscriptions.
- Analytics/observability data should not pollute the canonical operational truth tables.

## This subsystem owns
- service deployment
- workflow scheduling
- event health
- runtime health
- usage metering
- telemetry
- incident operations

## Core objects / data
- `service_health`
- `workflow_health`
- `runtime_health`
- `usage_events`
- `provider_health`
- `incident_events`

## Main flow

```text
deploy service → health/readiness → event/workflow checks → metrics/traces → incident detection → customer/operator status → rollback/repair
```

## UI / UX surfaces
- System health
- Failed jobs
- Connector failures
- Runtime fleet
- Usage detail
- Incident view

## Required states and failures
- Event backlog
- Temporal/workflow outage
- Provider degradation
- Projection backlog
- Node fleet offline
- Quota exhausted

## Definition of done
- [ ] Operational health is visible without DB shell access
- [ ] Customer data truth remains separate from analytics telemetry
- [ ] Durable jobs resume/retry
- [ ] Usage is attributable to business/workspace/action

## Source basis
- text(20260827-201113).txt — durable scheduler/worker metering
- text 5(2).txt — ClickHouse vs operational Postgres
