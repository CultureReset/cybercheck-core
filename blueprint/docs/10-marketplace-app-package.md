# Marketplace and Universal App Package

The Marketplace knows which products, versions, releases, manifests, capabilities, permissions and prices exist. Core separately records which business installed which release.

## Source-grounded rules
- One app package can include skills, agents, workflows, hooks, MCP/API, browser/Android/Linux executors, schemas, UI, permissions and verification.
- Marketplace catalog and installation state are separate concerns.
- Dashboard surfaces are registered from the installed package rather than hardcoded.

## This subsystem owns
- product catalog
- version/release management
- manifest validation
- capability declarations
- permission declarations
- surface declarations
- executor declarations
- pricing metadata

## Core objects / data
- `products`
- `product_versions`
- `releases`
- `manifests`
- `capabilities`
- `permissions`
- `surfaces`
- `runtime_requirements`
- `verification_policies`
- `pricing`

## Main flow

```text
developer package
     ↓
validate manifest
     ↓
publish release
     ↓
Marketplace catalog
     ↓
business chooses install
     ↓
Core creates installation
```

## UI / UX surfaces
- Marketplace browse
- App detail
- Release notes
- Permission preview
- Developer app builder
- Test console
- Publish release

## Required states and failures
- Invalid manifest
- Unsupported runtime
- Dangerous permission increase
- Unverified developer release
- Capability schema breaking change

## Definition of done
- [ ] Package declares everything needed to install safely
- [ ] Marketplace can show permissions/data/runtime requirements before install
- [ ] Release can be pinned
- [ ] App can be disabled/updated/uninstalled without deleting canonical business data

## Source basis
- text 3(3).txt — expanded app package
- text 9.txt — Marketplace/Core separation and manifest vocabulary
