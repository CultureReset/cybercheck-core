# Data Portability, Owner Control and Public/Private Boundaries

The platform should allow a business to retain control of its structured data and expose public/private surfaces deliberately rather than locking the data to one renderer or vendor.

## Source-grounded rules
- Public business data can feed profiles, search, widgets, APIs and public MCP.
- Private operational data remains authenticated/permissioned and should stay in business-controlled/private environments where applicable.
- Presentation changes do not change the underlying structured record.

## This subsystem owns
- dataset classification
- export interfaces
- public projections
- private capability interfaces
- owner-controlled storage/connection options

## Core objects / data
- `dataset_classifications`
- `exports`
- `external_data_bindings`
- `public_projection_bindings`
- `private_workspace_bindings`

## Main flow

```text
canonical dataset → classify public/private → projection/export binding → authorized consumer
private write/action → authenticated private gateway → policy/orchestrator
```

## UI / UX surfaces
- Public/private data settings
- Export center
- Cloud/data destination settings
- Public projection preview
- Private MCP settings

## Required states and failures
- Dataset accidentally classified public
- Export incomplete
- Owner cloud unavailable
- Private connection revoked

## Definition of done
- [ ] Every dataset has explicit classification
- [ ] Export is reproducible and documented
- [ ] Public projection contains no credentials/private operational rows
- [ ] Apps reference datasets through bindings rather than owning them

## Source basis
- text 9.txt — public/private MCP split
- text 4(2).txt — data/design separation
- text 7.txt — owner-controlled structured substrate
