# Contracts and Repository Boundaries

The reconstruction starts by freezing a common vocabulary so scattered repos stop inventing different names for the same concepts.

## Source-grounded rules
- cybercheck-contracts defines IDs, vocabulary, manifest, capability, event and MCP contracts.
- Core does not own business facts; Data does not own installation state; Marketplace does not own what a business installed; runtimes do not decide permissions.
- Independent products use the platform contracts rather than becoming platform kernel code.

## This subsystem owns
- shared schemas
- versioning rules
- compatibility rules
- cross-repo event vocabulary

## Core objects / data
- `OrganizationId`
- `BusinessId`
- `ActorId`
- `AgentId`
- `WorkspaceId`
- `NodeId`
- `DeviceId`
- `ProductId`
- `ReleaseId`
- `InstallationId`
- `DatasetId`
- `CapabilityId`
- `ExecutionId`
- `ReceiptId`
- `AppMapId`

## Main flow

```text
Contract package v1
       ↓
Identity / Core / Data / Marketplace / Orchestrator / Gateway import it
       ↓
Products and runtimes depend only on required contracts
```

## UI / UX surfaces
- Contract browser
- Schema docs
- Compatibility checker
- Version diff
- Developer package validator

## Required states and failures
- Breaking schema change
- Old product manifest
- Unknown capability
- Missing field
- Deprecated contract version

## Definition of done
- [ ] One authoritative name for every shared object
- [ ] Contracts are versioned
- [ ] Cross-repo tests use the same schemas
- [ ] No new repo invents duplicate identifiers

## Source basis
- text 9.txt — final repository structure and shared contract package
