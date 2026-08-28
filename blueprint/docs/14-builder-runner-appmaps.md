# Builder, Runner, Procedure Library and AppMaps

The system should spend expensive reasoning to learn or repair a workflow, then store a reusable procedure and execute deterministically when possible.

## Source-grounded rules
- Known screen/workflow → deterministic route.
- Unknown screen → AI exploration → validation → saved AppMap/procedure.
- Failure must stop, capture the failed step/screen and enter repair mode; it should not guess blindly.
- Runner is intentionally cheaper and more deterministic than Builder.

## This subsystem owns
- procedure discovery
- procedure versioning
- AppMap versions
- repair queue
- human takeover
- procedure test suite

## Core objects / data
- `procedures`
- `procedure_versions`
- `procedure_steps`
- `app_maps`
- `app_map_versions`
- `repair_items`
- `human_takeovers`
- `procedure_tests`

## Main flow

```text
task understood?
 ├─ YES → Runner → known procedure → executor
 └─ NO  → Builder → discover → verify → save procedure
failure → capture evidence → repair queue → Builder → new version → tests → Runner
```

## UI / UX surfaces
- Procedure library
- Builder session
- Repair queue
- AppMap editor
- Test run
- Human takeover
- Version rollback

## Required states and failures
- Selector changed
- Accessibility tree changed
- Wrong app account
- Captcha/security challenge
- Ambiguous screen
- Procedure side effect already occurred

## Definition of done
- [ ] Successful Builder result produces versioned reusable procedure
- [ ] Runner never silently changes procedure definition
- [ ] Repair preserves failure evidence
- [ ] Human takeover can resume without blindly repeating completed steps
- [ ] Known workflow runs without frontier-model reasoning at every click

## Source basis
- text 2(20260827-201113).txt — Orchestrator/Builder/Runner
- text 9.txt — AppMaps and fail-stop repair loop
