-- Identity and tenancy: the acting identities.
--
-- Before anything can run, Ghost must resolve three things:
--   tenant  -- which workspace and business?
--   target  -- which business or location?
--   actor   -- human or agent, and which one?
--
-- 001 covered organizations, businesses and workspaces. This adds the acting
-- identities that were missing: agent, node and device. Human identity itself
-- belongs to cybercheck-identity; core stores only the edge and the external id.

-- Software identities that can act on a tenant's behalf.
create table core.agents (
  id              uuid primary key default gen_random_uuid(),
  organization_id uuid not null references core.organizations (id) on delete cascade,
  business_id     uuid references core.businesses (id) on delete cascade,
  slug            core.contract_id not null,
  name            text not null check (length(trim(name)) > 0),
  kind            text not null check (kind in ('assistant', 'automation', 'integration')),
  status          text not null default 'active'
                    check (status in ('active', 'suspended', 'revoked')),
  created_by      text,
  created_at      timestamptz not null default now(),
  revoked_at      timestamptz,
  unique (organization_id, slug),
  -- A revoked agent must record when. Revocation is a security event.
  constraint agents_revoked_has_timestamp check (status <> 'revoked' or revoked_at is not null)
);

-- Registered compute environments: a cloud worker, a box at the business, a
-- workstation. A node advertises what it can run and heartbeats its health.
create table core.nodes (
  id                uuid primary key default gen_random_uuid(),
  organization_id   uuid not null references core.organizations (id) on delete cascade,
  business_id       uuid references core.businesses (id) on delete set null,
  slug              core.contract_id not null,
  name              text not null check (length(trim(name)) > 0),
  kind              text not null check (kind in ('cloud', 'box', 'workstation', 'hybrid')),
  status            text not null default 'provisioning'
                      check (status in ('provisioning', 'online', 'offline', 'error')),
  external_reference text,
  last_heartbeat_at timestamptz,
  registered_at     timestamptz not null default now(),
  unique (organization_id, slug),
  -- An online node must have heartbeated. Otherwise "online" means nothing.
  constraint nodes_online_has_heartbeat
    check (status <> 'online' or last_heartbeat_at is not null)
);

-- What a node advertises it can execute. The router reads this to place work.
create table core.node_capabilities (
  node_id       uuid not null references core.nodes (id) on delete cascade,
  capability_id core.contract_id not null,
  primary key (node_id, capability_id)
);

-- Android, browser and hardware identities. A device may be attached to a node
-- or provisioned in the cloud.
create table core.devices (
  id                 uuid primary key default gen_random_uuid(),
  business_id        uuid not null references core.businesses (id) on delete cascade,
  node_id            uuid references core.nodes (id) on delete set null,
  name               text not null check (length(trim(name)) > 0),
  kind               text not null
                       check (kind in ('android-physical', 'android-cloud', 'browser',
                                       'desktop', 'hardware')),
  status             text not null default 'provisioning'
                       check (status in ('provisioning', 'online', 'offline', 'error')),
  external_reference text,
  last_seen_at       timestamptz,
  created_at         timestamptz not null default now(),
  unique (business_id, name),
  -- A physical device is attached to a node; a cloud one is not.
  constraint devices_physical_has_node
    check (kind <> 'android-physical' or node_id is not null),
  constraint devices_online_has_last_seen
    check (status <> 'online' or last_seen_at is not null)
);

-- A workspace can be backed by a device, so persistent Android and browser
-- state stays attached to the user across compute cycles.
alter table core.workspaces
  add column device_id uuid references core.devices (id) on delete set null;

-- Every acting identity resolves through one row, so "who is acting" has a
-- single answer rather than three parallel ones.
create table core.actors (
  id              uuid primary key default gen_random_uuid(),
  organization_id uuid not null references core.organizations (id) on delete cascade,
  kind            text not null check (kind in ('user', 'agent', 'system')),
  user_id         text,
  agent_id        uuid references core.agents (id) on delete cascade,
  created_at      timestamptz not null default now(),
  -- The kind decides which column is populated. Nothing may be both or neither.
  constraint actors_shape_matches_kind check (
    (kind = 'user'   and user_id is not null and agent_id is null)
    or (kind = 'agent'  and agent_id is not null and user_id is null)
    or (kind = 'system' and user_id is null and agent_id is null)
  )
);

create unique index actors_one_per_user  on core.actors (organization_id, user_id) where kind = 'user';
create unique index actors_one_per_agent on core.actors (agent_id) where kind = 'agent';

create index agents_org_idx        on core.agents (organization_id);
create index nodes_org_idx         on core.nodes (organization_id);
create index nodes_status_idx      on core.nodes (status);
create index devices_business_idx  on core.devices (business_id);
create index devices_node_idx      on core.devices (node_id);
create index node_capabilities_idx on core.node_capabilities (capability_id);
