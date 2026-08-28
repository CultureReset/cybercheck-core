# Security, QA and Production Acceptance

Security and reliability are cross-cutting requirements, especially because the platform can hold private business data, persistent authenticated computers and consequential action capabilities.

## Source-grounded rules
- Authorization subjects extend beyond users to apps, agents, workflows, MCP clients, devices and API tokens.
- Public/private separation must be enforced by the kernel.
- Persistent browser/device sessions make tenant isolation and credential security critical.
- Execution must verify results and fail safely.

## This subsystem owns
- tenant isolation tests
- RBAC/capability authorization
- public/private boundary tests
- secret isolation
- execution/idempotency tests
- migration/data integrity tests
- backup/restore tests

## Core objects / data
- `security_events`
- `test_runs`
- `policy_test_cases`
- `isolation_test_cases`
- `backup_manifests`

## Main flow

```text
change → automated tests → staging workspace → execution/verification test → security checks → deploy → observe → rollback if needed
```

## UI / UX surfaces
- Security events
- Policy test console
- Data-quality dashboard
- System health
- Backup/restore
- Feature flags

## Required states and failures
- Cross-tenant data leak
- Private tool exposed publicly
- Replay/double execution
- Credential leakage
- Failed rollback
- Ledger mismatch

## Definition of done
- [ ] Public MCP cannot access private datasets
- [ ] App/agent permissions are least-privilege and testable
- [ ] Every write path is auditable
- [ ] Backups restore canonical + provenance + core relationships
- [ ] Critical workflows have idempotency/resume tests

## Source basis
- text 4(2).txt — generalized authorization
- text(20260827-201113).txt — persistent computer credential/tenant isolation caution
- text 9.txt — public/private MCP and definition-of-done themes
