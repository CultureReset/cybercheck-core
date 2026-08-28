# Developer SDK and Publishing Workflow

The SDK allows third-party or internal developers to create packages that declare data requirements, capabilities, executors, UI surfaces, permissions, events and verification.

## Source-grounded rules
- Manifest-driven packages allow the Marketplace to reason about an app without hardcoding what it does.
- Third-party developers should build against stable contracts, not internal database layout.

## This subsystem owns
- CLI/package validation
- local test harness
- manifest schema
- capability SDK
- surface SDK
- verification SDK
- release publishing

## Core objects / data
- `developer_accounts`
- `developer_apps`
- `test_installations`
- `release_submissions`
- `package_signatures`

## Main flow

```text
new app → declare manifest → implement surfaces/capabilities → local test → permission/verification tests → package validation → release → Marketplace
```

## UI / UX surfaces
- Developer dashboard
- App builder
- Manifest editor
- Test console
- Permission simulator
- Release publish
- Install test workspace

## Required states and failures
- Manifest invalid
- Capability lacks verification
- Permission too broad
- Test workspace failure
- Release rejected

## Definition of done
- [ ] A developer can build/install a sample app without editing CyberCheck core/dashboard code
- [ ] Contract validation catches incompatible package
- [ ] Permissions are visible before publish/install
- [ ] Release is versioned and reproducible

## Source basis
- text 3(3).txt — app package structure
- text 9.txt — shared contracts and Marketplace manifest
