# Research Graph and Truth Center

The Research Graph stores what CyberCheck discovered, including contradictory, stale, historical and unverified claims. The Canonical Business Record stores what is currently accepted as truth.

## Source-grounded rules
- AI should identify claims, not silently decide truth.
- Assertions retain source, capture time and extraction confidence.
- Owner/authority review moves accepted claims into canonical data.
- Historical facts remain historical rather than being overwritten or discarded.

## This subsystem owns
- source discovery records
- raw captures
- assertions
- evidence
- conflicts
- verification decisions
- canonicalization decisions
- history

## Core objects / data
- `research_jobs`
- `sources`
- `source_snapshots`
- `assertions`
- `assertion_evidence`
- `conflicts`
- `verification_requests`
- `verification_decisions`
- `canonicalization_events`

## Main flow

```text
seed
 ↓
identity resolution
 ↓
source discovery + raw capture
 ↓
fact extraction
 ↓
assertions + evidence
 ↓
conflict detection
 ↓
Truth Center
 ↓
owner/authority decision
 ↓
canonical record
```

## UI / UX surfaces
- Research progress
- Research result summary
- Assertion detail
- Source evidence detail
- Conflict resolution
- Bulk verification
- Historical timeline
- New-discovery review

## Required states and failures
- Source unreachable
- Low extraction confidence
- Possible wrong business
- Conflicting authoritative sources
- Owner says historical
- Not-our-business source
- Research partial completion

## Definition of done
- [ ] Raw evidence is retained separately from canonical values
- [ ] Every canonicalization decision records who/what verified it
- [ ] Conflicts are explicit objects
- [ ] Historical facts are queryable
- [ ] Business owner can reject incorrect discovered claims without deleting evidence

## Source basis
- text 8.txt — Research Graph vs Canonical Record, assertions, Truth Center, onboarding verification
