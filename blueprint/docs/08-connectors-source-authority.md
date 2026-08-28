# Connectors, Mapping, Dry Runs and Source Authority

Ingestion is a pipeline: source → select → transform → map → destination. Changes should be previewable before they alter canonical truth.

## Source-grounded rules
- Connector run modes should distinguish default, comprehensive and deletion behavior.
- Dry runs should process selectors/transforms/mappings without applying changes.
- Source authority determines whether a new claim can auto-update, becomes a suggestion, or requires owner review.
- Publisher-to-canonical differences should become suggestions rather than silent overwrites.

## This subsystem owns
- connector definitions
- mapping rules
- run mode
- dry-run diff
- source authority rules
- suggestions/reconciliation

## Core objects / data
- `connectors`
- `connector_runs`
- `connector_mappings`
- `mapping_versions`
- `source_definitions`
- `source_authority`
- `suggestions`
- `suggestion_decisions`

## Main flow

```text
SOURCE → SELECT → TRANSFORM → MAP → DRY RUN → REVIEW → APPLY
                                     ↓
                              assertions/canonical suggestions
```

## UI / UX surfaces
- Connector builder
- Mapping editor
- Dry-run preview
- Import result
- Source authority editor
- Suggestion queue
- Publisher drift/reconciliation

## Required states and failures
- ETL fails in comprehensive run
- Mass deletion threshold exceeded
- Mapping confidence low
- Source authority unknown
- Duplicate entity match
- Publisher proposes different value

## Definition of done
- [ ] Dry-run shows creates/updates/deletes/warnings
- [ ] Comprehensive sync aborts on failed ETL
- [ ] Mappings are versioned and reusable
- [ ] Authority rules are inspectable
- [ ] No lower-authority source silently overwrites protected canonical fields

## Source basis
- text 5(2).txt — connector modes, dry runs, triggers
- text 4(2).txt — Suggestions/source authority concepts
