# Installation Lifecycle

Installing an app is a controlled provisioning flow, not just adding a navigation card.

## Source-grounded rules
- Marketplace resolves product and stable release; Core creates/pins installation; Orchestrator validates requirements.
- Permissions, datasets, surfaces and runtime needs are evaluated before activation.
- After provisioning, capabilities are registered and the dashboard discovers the new surfaces automatically.

## This subsystem owns
- installation state machine
- dataset bindings
- permission grants
- surface registrations
- runtime bindings
- health status

## Core objects / data
- `installations`
- `installation_bindings`
- `installation_permissions`
- `installation_surfaces`
- `installation_runtime_bindings`
- `installation_health`

## Main flow

```text
CLICK INSTALL
 ↓
resolve release
 ↓
create installation + pin manifest
 ↓
validate requirements
 ↓
show permissions/datasets/runtime
 ↓
user approval
 ↓
provision runtime/connections
 ↓
register capabilities + surfaces
 ↓
health check
 ↓
INSTALLED
```

## UI / UX surfaces
- Install review
- Install progress
- Connection setup
- OAuth success/failure
- Health check
- Permission changes
- Update available
- Uninstall confirmation

## Required states and failures
- Permission denied
- Credential connection fails
- Runtime missing
- Dataset missing
- Health check fails
- App update requests new permission
- Uninstall while workflow running

## Definition of done
- [ ] Installation can resume after connection interruption
- [ ] Permission increases require explicit review
- [ ] Uninstall disables workflows/capabilities and preserves canonical data
- [ ] Dashboard removes surfaces dynamically
- [ ] Pinned manifest/release is auditable

## Source basis
- text 9.txt — final application install flow
