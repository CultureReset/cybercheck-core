# Failure, Recovery and Human Takeover Playbook

Failures are expected across websites, devices, APIs and connectors. CyberCheck should expose what failed, preserve evidence and choose resume/repair/human takeover rather than guessing.

## Source-grounded rules
- AppMap failure should stop and capture the failed step/screen.
- Builder can repair and publish a new procedure version.
- Connector comprehensive runs should abort on ETL failure instead of applying destructive partial state.
- Verification mismatch is drift/failure, not success.

## This subsystem owns
- failure classification
- resume/repeat decision
- repair queue
- human takeover
- rollback
- customer notification

## Core objects / data
- `failure_events`
- `repair_items`
- `takeover_sessions`
- `resume_tokens`
- `rollback_events`

## Main flow

```text
failure detected → freeze/record observation → classify side effects → choose retry/resume/repair/human → verify recovery → close incident with receipt/history
```

## UI / UX surfaces
- Repair queue
- Failure detail
- Human takeover
- Retry/resume modal
- Rollback view
- Customer notification

## Required states and failures
- Unknown side effect
- Partial external action
- Target security challenge
- Repeated verification mismatch
- Data import destructive risk

## Definition of done
- [ ] Recovery never silently duplicates irreversible action
- [ ] Evidence is captured before repair
- [ ] Human can see what already completed
- [ ] Rollback applies where supported and history remains

## Source basis
- text 9.txt — fail-stop AppMap repair
- text 5(2).txt — comprehensive connector safety
- text 2(20260827-201113).txt — failure → Builder repair
