# Ghost and Compute Runtime

Ghost is a plug-and-play execution node, not the platform itself. Cloud workers, customer PCs, mobile devices and Ghost can all satisfy executor/runtime roles.

## Source-grounded rules
- Control plane should not care whether work runs on cloud VM, physical Ghost box, Raspberry Pi, Linux, Windows or Mac.
- Persistent computers can retain browser sessions and local app state, making tenant isolation and credential protection critical.
- Durable scheduling/workflows must exist outside a user browser session.

## This subsystem owns
- node registration
- worker daemon
- local/cloud execution
- device bridge
- browser session
- health telemetry
- runtime capability advertisement

## Core objects / data
- `nodes`
- `node_capabilities`
- `worker_instances`
- `worker_sessions`
- `node_health`
- `runtime_versions`

## Main flow

```text
register node → attest/runtime health → advertise capabilities → Core records node → Orchestrator selects node → worker executes → returns observation/health
```

## UI / UX surfaces
- Ghost setup wizard
- Node registration
- Node detail
- Runtime update
- Local/cloud preference
- Health/telemetry

## Required states and failures
- Node offline
- Version incompatible
- Credential store unavailable
- No network
- Device bridge missing
- Resource exhaustion

## Definition of done
- [ ] Ghost can disappear and platform still functions via other runtimes
- [ ] Node capability advertisement is contract-based
- [ ] Workflows can wake/resume workers durably
- [ ] Node secrets are isolated

## Source basis
- text(20260827-201113).txt — Ghost as one execution location and persistent worker model
