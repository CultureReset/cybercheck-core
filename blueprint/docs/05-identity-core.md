# Identity and Core

Identity answers who the human or authenticated actor is. Core answers which organizations, businesses, workspaces, agents, nodes, devices and installations exist and how they relate.

## Source-grounded rules
- Durable business identity must survive changing names, slugs, URLs, providers and public presentation.
- Slugs remain useful public identifiers but should not be the internal ownership key.
- Device registration and installation state belong to Core, not the Data schema or Marketplace catalog.

## This subsystem owns
- humans/auth/session references
- organizations
- businesses
- workspaces
- agents
- nodes/devices
- installation state
- membership relationships

## Core objects / data
- `users`
- `sessions`
- `organizations`
- `organization_members`
- `businesses`
- `business_members`
- `workspaces`
- `agents`
- `nodes`
- `devices`
- `installations`
- `connections`

## Main flow

```text
authenticate actor
      ↓
resolve organization/business/workspace
      ↓
resolve membership/role
      ↓
provide actor context to data/gateway/orchestrator
```

## UI / UX surfaces
- Organization switcher
- Business switcher
- Team/members
- Device registry
- Workspace settings
- Claimed-business ownership

## Required states and failures
- Business not claimed
- User removed
- Session expired
- Device moved to another workspace
- Duplicate business match
- Organization ownership transfer

## Definition of done
- [ ] Every request resolves an ActorId and business/workspace context
- [ ] Stable BusinessId is used internally
- [ ] Membership revocation takes effect without rewriting business data
- [ ] Device and installation lifecycle are auditable

## Source basis
- text 7.txt — permanent business ID
- text 9.txt — Identity/Core responsibilities and migration away from site_id/entity_slug ownership
