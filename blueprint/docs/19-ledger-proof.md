# Ledger, Audit History and Tamper Evidence

The ledger is a cross-platform transparency layer for actions. Detailed records remain private; later external anchoring can publish only hashes/checkpoints rather than customer data.

## Source-grounded rules
- Each completed execution receipt includes execution, business, actor, capability, verification, evidence, previous hash, payload/chain hash and timestamp.
- Ledger views can be derived per business/device/agent/workspace.
- Append-only history should avoid UPDATE/DELETE of audit events.

## This subsystem owns
- receipt generation
- hash chaining
- audit event history
- evidence references
- derived ledger views
- optional external checkpoint anchoring

## Core objects / data
- `receipts`
- `audit_events`
- `ledger_chains`
- `ledger_checkpoints`
- `evidence_refs`

## Main flow

```text
execution result + verification
      ↓
receipt payload
      ↓
hash previous + payload
      ↓
append event
      ↓
business/device/agent/workspace views
      ↓ optional
external hash checkpoint
```

## UI / UX surfaces
- Ledger list
- Receipt detail
- Audit history
- Evidence viewer
- Chain verification
- Export proof

## Required states and failures
- Missing previous hash
- Evidence unavailable
- Clock mismatch
- Duplicate execution
- External anchor unavailable

## Definition of done
- [ ] Audit/receipt rows are append-only
- [ ] Receipt can be validated against previous hash
- [ ] Private payload is never exposed by public proof checkpoint
- [ ] Actor/capability/result/verification are queryable

## Source basis
- text 9.txt — keep ledger/hash chain
- text 5(2).txt and text 4(2).txt — append-only audit and external tamper-evidence concept
