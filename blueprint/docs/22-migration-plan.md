# Controlled Repository and Data Migration

The existing repos should be mined and reassembled around authoritative boundaries rather than physically merged into one giant codebase.

## Source-grounded rules
- For every existing table, inventory columns, keys, business identifier, readers/writers, public/private classification and target dataset.
- Build one stable legacy identity map to core BusinessId.
- Migrate canonical data with row-count/duplicate/rejected/unmapped validation.
- Import provenance separately from canonical truth.
- Use compatibility adapters during transition; retire site_id/entity_slug ownership after callers migrate.

## This subsystem owns
- inventory
- identity mapping
- data migration
- provenance migration
- compatibility adapters
- caller migration
- legacy retirement

## Core objects / data
- `legacy_identity_map`
- `migration_runs`
- `migration_errors`
- `migration_reconciliations`
- `compatibility_routes`

## Main flow

```text
freeze existing systems → inventory → stable BusinessId map → migrate canonical tables → import provenance → validate → compatibility adapter → migrate callers → parity test → retire dual architecture
```

## UI / UX surfaces
- Migration dashboard
- Table mapping
- Unmapped identity queue
- Validation result
- Compatibility traffic monitor
- Legacy retirement checklist

## Required states and failures
- Unmapped slug
- Duplicate business
- Row-count mismatch
- Unknown source
- Caller still writing old table
- Dual-write divergence

## Definition of done
- [ ] No silent loss
- [ ] Every migrated row resolves through one identity map
- [ ] Compatibility layer is temporary and measurable
- [ ] Legacy identifiers stop owning data after cutover
- [ ] Rollback/export exists for migration run

## Source basis
- text 9.txt — controlled migration steps and compatibility adapter
