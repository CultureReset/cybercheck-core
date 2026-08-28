# CyberCheck Master Build Checklist

This combines 122 definition-of-done checks from the production blueprint documents.


## CyberCheck Master Platform
- [ ] One stable business/entity identity anchors all business data
- [ ] No repo owns concerns outside its boundary
- [ ] Read and write paths are explicit and testable
- [ ] Installed products register through contracts rather than dashboard hardcoding
- [ ] Every consequential write can be traced from actor to receipt
- [ ] Public surfaces cannot reach private data without authenticated authorized path

## First Production Slice
- [ ] A new business can complete this entire path without operator database edits
- [ ] The canonical field is visible in the public projection after change
- [ ] External action is either verified or clearly failed/drifted
- [ ] The receipt includes actor, capability, executor, verification and evidence reference
- [ ] Uninstalling the app does not remove the canonical business data

## Design System and Surface Registry
- [ ] All core surfaces share tokens and interaction patterns
- [ ] Apps can register navigation without modifying the dashboard shell
- [ ] Every action control can show policy/approval state
- [ ] Every data field can expose source/provenance when relevant
- [ ] Every primary screen has loading/empty/error/offline states

## State-Level UX Matrix
- [ ] Every lifecycle object exposes a machine-readable state
- [ ] Every state has customer-facing copy and a next action
- [ ] Failures preserve evidence and do not silently mark success
- [ ] Retries are idempotent or clearly ask whether to resume/repeat

## Contracts and Repository Boundaries
- [ ] One authoritative name for every shared object
- [ ] Contracts are versioned
- [ ] Cross-repo tests use the same schemas
- [ ] No new repo invents duplicate identifiers

## Identity and Core
- [ ] Every request resolves an ActorId and business/workspace context
- [ ] Stable BusinessId is used internally
- [ ] Membership revocation takes effect without rewriting business data
- [ ] Device and installation lifecycle are auditable

## Canonical Structured Data Warehouse
- [ ] No giant JSON storage for core operational domains
- [ ] Every current value can be traced to source/verification history
- [ ] Industry extensions share common identity/relationship patterns
- [ ] App uninstall preserves canonical data

## Research Graph and Truth Center
- [ ] Raw evidence is retained separately from canonical values
- [ ] Every canonicalization decision records who/what verified it
- [ ] Conflicts are explicit objects
- [ ] Historical facts are queryable
- [ ] Business owner can reject incorrect discovered claims without deleting evidence

## Connectors, Mapping, Dry Runs and Source Authority
- [ ] Dry-run shows creates/updates/deletes/warnings
- [ ] Comprehensive sync aborts on failed ETL
- [ ] Mappings are versioned and reusable
- [ ] Authority rules are inspectable
- [ ] No lower-authority source silently overwrites protected canonical fields

## Streams, Projections, Search and Pages
- [ ] Public profile does not query dozens of raw tables directly
- [ ] Search verticals can express capacity/price/date/availability filters
- [ ] Page rebuilds can be incremental
- [ ] Map/list/photos/AI views share one result set

## Marketplace and Universal App Package
- [ ] Package declares everything needed to install safely
- [ ] Marketplace can show permissions/data/runtime requirements before install
- [ ] Release can be pinned
- [ ] App can be disabled/updated/uninstalled without deleting canonical business data

## Installation Lifecycle
- [ ] Installation can resume after connection interruption
- [ ] Permission increases require explicit review
- [ ] Uninstall disables workflows/capabilities and preserves canonical data
- [ ] Dashboard removes surfaces dynamically
- [ ] Pinned manifest/release is auditable

## Gateway, REST, Public MCP and Private MCP
- [ ] Public and private MCP cannot be confused by route or credential
- [ ] MCP contains no independent bypass business logic
- [ ] Every write request can be tied to ActorId/business/capability
- [ ] Webhook actions are authenticated/replay-protected

## Orchestrator, Policy and Approvals
- [ ] No executor can bypass policy
- [ ] Approval record captures exact requested action
- [ ] Execution has idempotency key
- [ ] Provider swap does not change capability contract
- [ ] Policy subjects include non-human actors

## Builder, Runner, Procedure Library and AppMaps
- [ ] Successful Builder result produces versioned reusable procedure
- [ ] Runner never silently changes procedure definition
- [ ] Repair preserves failure evidence
- [ ] Human takeover can resume without blindly repeating completed steps
- [ ] Known workflow runs without frontier-model reasoning at every click

## Browser Runtime
- [ ] Browser runtime cannot approve its own action
- [ ] Profile isolation is tenant-safe
- [ ] Runtime returns observations not just click success
- [ ] Unknown screen can stop and request repair/human takeover

## Android and iOS Runtime
- [ ] Semantic IDs survive coordinate/layout changes when possible
- [ ] Device actions produce read-back observations
- [ ] Device does not decide permissions
- [ ] Human takeover is available for unknown/blocked state

## Ghost and Compute Runtime
- [ ] Ghost can disappear and platform still functions via other runtimes
- [ ] Node capability advertisement is contract-based
- [ ] Workflows can wake/resume workers durably
- [ ] Node secrets are isolated

## Verification System
- [ ] Every consequential capability declares verification expectations
- [ ] Verified status requires passed checks
- [ ] Mismatch is visible as drift/failure
- [ ] Evidence references are attached to receipt

## Ledger, Audit History and Tamper Evidence
- [ ] Audit/receipt rows are append-only
- [ ] Receipt can be validated against previous hash
- [ ] Private payload is never exposed by public proof checkpoint
- [ ] Actor/capability/result/verification are queryable

## Independent Product Layer
- [ ] Each product can be disabled independently
- [ ] Product code does not modify Core schema ownership rules
- [ ] Product surfaces come from registrations
- [ ] Shared canonical data survives uninstall

## Developer SDK and Publishing Workflow
- [ ] A developer can build/install a sample app without editing CyberCheck core/dashboard code
- [ ] Contract validation catches incompatible package
- [ ] Permissions are visible before publish/install
- [ ] Release is versioned and reproducible

## Controlled Repository and Data Migration
- [ ] No silent loss
- [ ] Every migrated row resolves through one identity map
- [ ] Compatibility layer is temporary and measurable
- [ ] Legacy identifiers stop owning data after cutover
- [ ] Rollback/export exists for migration run

## Security, QA and Production Acceptance
- [ ] Public MCP cannot access private datasets
- [ ] App/agent permissions are least-privilege and testable
- [ ] Every write path is auditable
- [ ] Backups restore canonical + provenance + core relationships
- [ ] Critical workflows have idempotency/resume tests

## Deployment, Observability and Operations
- [ ] Operational health is visible without DB shell access
- [ ] Customer data truth remains separate from analytics telemetry
- [ ] Durable jobs resume/retry
- [ ] Usage is attributable to business/workspace/action

## Build Order and Roadmap
- [ ] Each milestone has a working acceptance demo
- [ ] First vertical slice passes before broad product rollout
- [ ] Legacy retirement is scheduled, not indefinite

## Data Portability, Owner Control and Public/Private Boundaries
- [ ] Every dataset has explicit classification
- [ ] Export is reproducible and documented
- [ ] Public projection contains no credentials/private operational rows
- [ ] Apps reference datasets through bindings rather than owning them

## Failure, Recovery and Human Takeover Playbook
- [ ] Recovery never silently duplicates irreversible action
- [ ] Evidence is captured before repair
- [ ] Human can see what already completed
- [ ] Rollback applies where supported and history remains
