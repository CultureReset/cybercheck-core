# Gateway, REST, Public MCP and Private MCP

The Gateway is the single front door for UI, REST, MCP and webhooks. Protocol layers do not own the business logic.

## Source-grounded rules
- Public MCP exposes only publishable structured data.
- Private MCP requires authenticated membership and only exposes granted capabilities.
- Private MCP writes still pass through policy, approval, execution, verification and receipt.
- API should organize around businesses/datasets/installations/executions/approvals/receipts/devices/workspaces rather than a giant route jungle.

## This subsystem owns
- authentication boundary
- public/private routing
- request normalization
- dataset endpoints
- execution endpoints
- MCP transport
- webhook ingress/egress

## Core objects / data
- `api_clients`
- `api_tokens`
- `mcp_connections`
- `webhook_endpoints`
- `request_audit_refs`

## Main flow

```text
READ: UI/MCP/API → Gateway → Identity/Core → permission → Data/Projection → response
WRITE/ACTION: UI/MCP/API → Gateway → Identity/Core → Capability → Orchestrator → policy/approval → executor → verify → receipt
```

## UI / UX surfaces
- API key manager
- MCP connections
- Webhook manager
- Public data explorer
- Private tool explorer
- Permission test

## Required states and failures
- Expired token
- Wrong business scope
- Private request on public endpoint
- MCP client permission revoked
- Webhook replay
- Rate/quota limit

## Definition of done
- [ ] Public and private MCP cannot be confused by route or credential
- [ ] MCP contains no independent bypass business logic
- [ ] Every write request can be tied to ActorId/business/capability
- [ ] Webhook actions are authenticated/replay-protected

## Source basis
- text 9.txt — gateway routes and public/private MCP
- text 5(2).txt — MCP as thin interface to same API/permission/services
