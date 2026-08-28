# Verification System

An action is not complete because an executor returned success. CyberCheck defines capability-specific success criteria, reads the resulting state and compares it against the requested outcome.

## Source-grounded rules
- Known-channel sync loop is canonical value → AppMap/executor → target application → read back → compare → verified/drifted.
- Verification rules can be declared by app packages/capabilities.
- Verification failure should preserve the observation and enter repair/reconciliation rather than falsely report success.

## This subsystem owns
- verification policy registry
- observation comparison
- evidence references
- drift classification
- retry/repair decision

## Core objects / data
- `verification_policies`
- `verification_runs`
- `verification_checks`
- `verification_evidence`
- `drift_records`

## Main flow

```text
requested outcome
 ↓
execute
 ↓
observe target state
 ↓
run verification checks
 ├─ match → VERIFIED
 └─ mismatch → DRIFTED/FAILED → repair/reconcile
```

## UI / UX surfaces
- Verification policy editor
- Verification run detail
- Failure comparison
- Evidence viewer
- Drift queue

## Required states and failures
- No read-back available
- Partial match
- Target eventually consistent
- External service normalized value
- Evidence capture failed

## Definition of done
- [ ] Every consequential capability declares verification expectations
- [ ] Verified status requires passed checks
- [ ] Mismatch is visible as drift/failure
- [ ] Evidence references are attached to receipt

## Source basis
- text 9.txt — channel verification loop and ledger
- text 3(3).txt — verification in app package
