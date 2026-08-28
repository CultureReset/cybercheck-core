# State-Level UX Matrix

Production UX is the complete set of states inside each major destination, not only the happy-path page.

## Source-grounded rules
- Installations, connectors, research jobs, workflows, executions, devices and projections all have lifecycles.
- Failure should stop safely and expose what happened instead of guessing through broken AppMaps or unknown UI.
- Connector dry runs and previews are safety mechanisms, not optional polish.

## This subsystem owns
- cross-product state vocabulary
- status labels
- recovery actions
- operator/customer escalation

## Core objects / data
- `LifecycleState`
- `ErrorCode`
- `RecoveryAction`
- `RetryPolicy`
- `HealthStatus`

## Main flow

```text
IDLE → LOADING → READY
                    ↘
                   EMPTY
                    ↘
                  ERROR → RETRY / REPAIR / SUPPORT
                    ↘
                 OFFLINE / STALE / PARTIAL
```

## UI / UX surfaces
- Install pending/validating/provisioning/connected/failed/updating/uninstalling
- Research queued/running/partial/complete/needs-review
- Execution pending-approval/running/verifying/verified/failed/drifted
- Device online/degraded/offline/repairing
- Projection current/lagging/failed

## Required states and failures
- Expired credential
- Permission revoked
- Source deleted
- Executor disconnected
- Verification mismatch
- Import partial failure
- Policy changed mid-run
- App version incompatible

## Definition of done
- [ ] Every lifecycle object exposes a machine-readable state
- [ ] Every state has customer-facing copy and a next action
- [ ] Failures preserve evidence and do not silently mark success
- [ ] Retries are idempotent or clearly ask whether to resume/repeat

## Source basis
- text 5(2).txt — connector run modes and dry runs
- text 9.txt — AppMap fail-stop and repair queue
- text 2(20260827-201113).txt — Builder repair mode and verification loop
