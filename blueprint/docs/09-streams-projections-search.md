# Streams, Projections, Search and Pages

Consumers should read purpose-built projections instead of traversing the full canonical warehouse for every request.

## Source-grounded rules
- Streams/projections are read models for downstream consumers.
- Search should use structured filtering for structured facts, semantic retrieval where appropriate and document retrieval for long-form text.
- The map is one renderer of a result set; users search facts, not pins.
- Page templates consume projections so data and design remain separate.

## This subsystem owns
- projection definitions
- change evaluation
- search verticals
- geo/media indexing
- page/template consumers

## Core objects / data
- `stream_definitions`
- `projection_versions`
- `projection_jobs`
- `search_verticals`
- `search_documents`
- `geo_index_refs`
- `page_templates`

## Main flow

```text
canonical change
      ↓
event
      ↓
stream evaluator
      ↓
projection updated
      ↓
Search / Pages / Map / Public API / MCP / Widget
```

## UI / UX surfaces
- Projection monitor
- Search configuration
- Search result explorer
- Map discovery
- Page preview
- Template builder

## Required states and failures
- Projection lag
- Search index stale
- Template incompatible with projection version
- Geo data missing
- Semantic result lacks structured verification

## Definition of done
- [ ] Public profile does not query dozens of raw tables directly
- [ ] Search verticals can express capacity/price/date/availability filters
- [ ] Page rebuilds can be incremental
- [ ] Map/list/photos/AI views share one result set

## Source basis
- text 5(2).txt — Streams/read models/search stack
- text 4(2).txt — projections/pages/search strategies
- text 10.txt — map as renderer of structured results
