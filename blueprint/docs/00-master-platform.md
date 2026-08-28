# CyberCheck Master Platform

CyberCheck is a modular structured-data and execution platform. The durable foundation is not one app, one website, one model, or one device. It is a set of contracts connecting identity, durable business/entity identity, canonical structured truth, installable capabilities, safe execution, verification and independent user-facing products.

## Source-grounded rules
- Contracts define the common language.
- Identity knows people; Core knows businesses, workspaces, devices, agents and installations.
- Canonical data knows structured business truth; Marketplace knows what products/capabilities exist.
- Orchestrator decides what can happen, chooses how, verifies the outcome and records proof.
- Browser/Android/API/local/cloud runtimes execute but do not own policy or canonical business truth.
- Independent products can disappear without breaking the platform foundation.
- Public and private MCP surfaces are separate; private MCP never bypasses permission, approval or verification.

## This subsystem owns
- platform contracts
- identity
- core registry
- canonical data boundary
- marketplace catalog
- orchestration boundary
- gateway boundary
- surface registration
- runtime interfaces

## Core objects / data
- `organization`
- `business`
- `user`
- `actor`
- `agent`
- `workspace`
- `node`
- `device`
- `installation`
- `dataset`
- `capability`
- `permission`
- `surface`
- `execution`
- `approval`
- `verification`
- `receipt`
- `app_map`

## Main flow

```text
PERSON / AI / SOFTWARE
        ↓
Gateway / surface
        ↓
Identity + Core
   ┌────┴────┐
   ↓         ↓
READ DATA   DO ACTION
   ↓         ↓
Canonical  Orchestrator
Data       → Policy → Approval → Executor
   ↓                         ↓
Projection                 Verify
   ↓                         ↓
UI/API/MCP                 Receipt/Ledger
```

## UI / UX surfaces
- Public directory/profile/search
- Business dashboard
- Admin
- Developer portal
- Public MCP
- Private MCP
- Voice/SMS ingress
- Third-party embedded surfaces

## Required states and failures
- Unknown business identity
- Permission denied
- Private/public boundary violation
- Executor unavailable
- Verification failed
- Partial projection update
- Disconnected app
- Stale source data

## Definition of done
- [ ] One stable business/entity identity anchors all business data
- [ ] No repo owns concerns outside its boundary
- [ ] Read and write paths are explicit and testable
- [ ] Installed products register through contracts rather than dashboard hardcoding
- [ ] Every consequential write can be traced from actor to receipt
- [ ] Public surfaces cannot reach private data without authenticated authorized path

## Source basis
- text 9.txt — final repository structure, shared contracts, public/private MCP, install and execution flows
- text 7.txt — structured data foundation and durable business identity
- text 3(3).txt — universal executor and broad app package
- text(20260827-201113).txt — Ghost/runtime separation
