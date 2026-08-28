# First Production Slice

This is the smallest end-to-end path that proves nearly every foundational subsystem before expanding into dozens of independent products.

## Source-grounded rules
- Onboarding should research first and turn owner setup into verification rather than blank data entry.
- Discovered claims and canonical truth must remain separate.
- One canonical change can project outward to public surfaces and installed channels.
- AI requests actions through the kernel; the model is not the authority.

## This subsystem owns
- vertical-slice acceptance criteria
- cross-service event sequence
- demo business lifecycle

## Core objects / data
- `research_job`
- `assertion`
- `verification`
- `business`
- `canonical_field`
- `projection`
- `product`
- `installation`
- `capability`
- `execution`
- `receipt`

## Main flow

```text
Create account
  ↓
Identify/seed business
  ↓
Research public existence
  ↓
Review claims/conflicts
  ↓
Verify ownership
  ↓
Approve canonical truth
  ↓
Dashboard live
  ↓
Install one app
  ↓
Change one canonical field
  ↓
Propagate to one public projection + one external channel
  ↓
Verify channel result
  ↓
Receipt / ledger
```

## UI / UX surfaces
- Signup
- Seed business
- Research progress
- Research results
- Claim verification
- Truth Center
- Dashboard
- Marketplace install
- Data editor
- Approval
- Execution detail
- Ledger receipt
- Updated public profile

## Required states and failures
- Research partial failure
- Business already claimed
- Claim verification failure
- Conflicting sources
- Install requirement missing
- External channel offline
- Write succeeds but verification fails
- Projection lags
- User cancels approval

## Definition of done
- [ ] A new business can complete this entire path without operator database edits
- [ ] The canonical field is visible in the public projection after change
- [ ] External action is either verified or clearly failed/drifted
- [ ] The receipt includes actor, capability, executor, verification and evidence reference
- [ ] Uninstalling the app does not remove the canonical business data

## Source basis
- text 8.txt — research → assertions → verification → canonical twin
- text 9.txt — install flow, one-update-everywhere flow, AI action flow
- text 2(20260827-201113).txt — Builder/Runner/verification model
