# Canonical Structured Data Warehouse

The canonical warehouse stores accepted structured business truth in normalized relational domains. Flexible metadata and relationships sit above those real tables instead of replacing them with one giant JSON property bag.

## Source-grounded rules
- Every business can use any relevant domain table; one business identity anchors many tables.
- Operational domains remain relational: hours, menus, services, pricing, events, availability, policies, media and related records.
- Schema registry/entity metadata provides flexibility without sacrificing relational correctness.
- Apps do not own canonical data and uninstalling an app must not erase canonical truth.

## This subsystem owns
- common-core business facts
- industry extension tables
- relationships
- provenance references
- version references
- data-level access classifications

## Core objects / data
- `businesses`
- `locations`
- `contacts`
- `business_hours`
- `services`
- `service_pricing`
- `products`
- `resources`
- `events`
- `availability`
- `policies`
- `media`
- `reviews`
- `entity_registry`
- `entity_types`
- `field_definitions`
- `entity_relationships`

## Main flow

```text
verified claim / owner edit
        ↓
canonical service
        ↓
normalized domain table
        ↓
change event
        ↓
projections / search / public surfaces / installed channels
```

## UI / UX surfaces
- Data Hub
- Section editor
- Relationship manager
- Schema registry
- History panel
- Source/provenance panel

## Required states and failures
- Invalid cross-industry field
- Duplicate resource
- Deleted parent entity
- Orphan relationship
- Conflicting current values
- Attempt to delete referenced canonical record

## Definition of done
- [ ] No giant JSON storage for core operational domains
- [ ] Every current value can be traced to source/verification history
- [ ] Industry extensions share common identity/relationship patterns
- [ ] App uninstall preserves canonical data

## Source basis
- text 5(2).txt — PostgreSQL canonical truth + normalized domain tables + metadata tables
- text 7.txt — warehouse analogy/universal core
- text 9.txt — canonical data boundary
