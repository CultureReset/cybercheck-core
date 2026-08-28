# Orchestrator, Policy and Approvals

The Orchestrator decides what needs to happen and under which capability/policy. It does not contain UI-click implementation details.

## Source-grounded rules
- Orchestrator resolves intent, capability, executor, approval requirements and success criteria.
- Policy is enforced before consequential actions.
- Subjects can include humans, apps, agents, workflows, MCP clients, API tokens and devices.
- Provider slots keep models/executors vendor-swappable.

## This subsystem owns
- execution planning
- policy evaluation
- approval creation
- executor selection
- retry/resume policy
- event lifecycle
- receipt orchestration

## Core objects / data
- `executions`
- `execution_steps`
- `policy_rules`
- `policy_decisions`
- `approvals`
- `provider_slots`
- `executor_candidates`
- `execution_observations`

## Main flow

```text
request
 ↓
resolve actor/business
 ↓
capability
 ↓
policy decision
 ↓
approval if required
 ↓
executor resolver
 ↓
execute
 ↓
observe
 ↓
verify
 ↓
receipt
```

## UI / UX surfaces
- Policy Center
- Rule editor
- Approval queue
- Approval detail
- Execution detail
- Provider/executor preference

## Required states and failures
- Denied policy
- Approval expired
- Executor becomes unavailable
- Policy changes while pending
- Duplicate request
- Action already completed
- Cost/quota threshold

## Definition of done
- [ ] No executor can bypass policy
- [ ] Approval record captures exact requested action
- [ ] Execution has idempotency key
- [ ] Provider swap does not change capability contract
- [ ] Policy subjects include non-human actors

## Source basis
- text 2(20260827-201113).txt — Orchestrator responsibilities
- text 4(2).txt — generalized authorization subjects
- text 9.txt — provider slots and AI action flow
