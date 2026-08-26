-- CyberCheck core: platform records only.
--
-- This schema owns tenancy and installation STATE: who exists, and what each
-- business has installed. It does not own the catalog (cybercheck-marketplace)
-- and it does not own canonical business facts such as menus and hours
-- (cybercheck-data-schema). Those are keyed by the same business id.

create schema if not exists core;

create domain core.contract_id as text
  check (value ~ '^[a-z0-9]+([.-][a-z0-9]+)*$');

create domain core.semver as text
  check (value ~ '^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$');

create table core.organizations (
  id         uuid primary key default gen_random_uuid(),
  slug       core.contract_id not null unique,
  name       text not null check (length(trim(name)) > 0),
  status     text not null default 'active' check (status in ('active', 'suspended')),
  created_at timestamptz not null default now()
);

-- Identity itself belongs to cybercheck-identity. Core stores only the
-- membership edge, referencing the external user id.
create table core.org_members (
  organization_id uuid not null references core.organizations (id) on delete cascade,
  user_id         text not null check (length(trim(user_id)) > 0),
  role            text not null check (role in ('owner', 'admin', 'manager', 'viewer')),
  added_at        timestamptz not null default now(),
  primary key (organization_id, user_id)
);

-- The tenant an installation binds to. Canonical facts about this business
-- (locations, hours, menus) live in cybercheck-data-schema under the same id.
create table core.businesses (
  id              uuid primary key default gen_random_uuid(),
  organization_id uuid not null references core.organizations (id) on delete cascade,
  slug            core.contract_id not null unique,
  name            text not null check (length(trim(name)) > 0),
  status          text not null default 'active' check (status in ('active', 'suspended')),
  created_at      timestamptz not null default now()
);

create table core.workspaces (
  id                 uuid primary key default gen_random_uuid(),
  business_id        uuid not null references core.businesses (id) on delete cascade,
  name               text not null check (length(trim(name)) > 0),
  kind               text not null check (kind in ('browser', 'android', 'container')),
  -- Pointers, never contents. Secrets live in the secret store.
  external_reference text,
  secret_reference   text,
  status             text not null default 'provisioning'
                       check (status in ('provisioning', 'active', 'stopped', 'error')),
  created_at         timestamptz not null default now(),
  unique (business_id, name)
);

-- Projection of the marketplace catalog. Core keeps just enough to resolve and
-- render an installation without calling the marketplace on every request.
create table core.products (
  id         uuid primary key default gen_random_uuid(),
  slug       core.contract_id not null unique,
  name       text not null,
  publisher  core.contract_id,
  synced_at  timestamptz not null default now()
);

create table core.product_versions (
  id         uuid primary key default gen_random_uuid(),
  product_id uuid not null references core.products (id) on delete cascade,
  version    core.semver not null,
  manifest   jsonb not null,
  synced_at  timestamptz not null default now(),
  unique (product_id, version)
);

-- An installation pins the manifest it was installed with. A later catalog
-- change must never retroactively alter what a running install is allowed to
-- do; changing that is an explicit update, recorded as a new pinned manifest.
create table core.installations (
  id                 uuid primary key default gen_random_uuid(),
  business_id        uuid not null references core.businesses (id) on delete cascade,
  workspace_id       uuid references core.workspaces (id) on delete set null,
  product_id         uuid not null references core.products (id) on delete restrict,
  product_version_id uuid not null references core.product_versions (id) on delete restrict,
  pinned_manifest    jsonb not null,
  status             text not null default 'pending'
                       check (status in ('pending', 'installing', 'installed', 'failed',
                                         'updating', 'uninstalling', 'uninstalled')),
  health_status      text not null default 'unknown'
                       check (health_status in ('unknown', 'healthy', 'unhealthy')),
  last_health_at     timestamptz,
  failure_reason     text,
  installed_by       text,
  installed_at       timestamptz,
  uninstalled_at     timestamptz,
  created_at         timestamptz not null default now()
);

-- A business may hold only one live installation of a product. Uninstalled rows
-- are kept for history, so the constraint is partial rather than a plain unique.
create unique index installations_one_live_per_product
  on core.installations (business_id, product_id)
  where status <> 'uninstalled';

-- An installed row must say when, and a failed row must say why.
alter table core.installations add constraint installations_installed_has_timestamp
  check (status <> 'installed' or installed_at is not null);
alter table core.installations add constraint installations_failed_has_reason
  check (status <> 'failed' or failure_reason is not null);
alter table core.installations add constraint installations_uninstalled_has_timestamp
  check (status <> 'uninstalled' or uninstalled_at is not null);

create table core.installation_permissions (
  installation_id uuid not null references core.installations (id) on delete cascade,
  permission_id   core.contract_id not null,
  granted_at      timestamptz not null default now(),
  granted_by      text,
  primary key (installation_id, permission_id)
);

-- Registered at install time. The dashboard reads these to discover what to
-- render; it never hardcodes a product.
create table core.installation_surfaces (
  id                  uuid primary key default gen_random_uuid(),
  installation_id     uuid not null references core.installations (id) on delete cascade,
  kind                text not null
                        check (kind in ('dashboard', 'public', 'direct-url', 'settings', 'onboarding')),
  path                text not null check (length(trim(path)) > 0),
  title               text,
  icon                text,
  requires_permission core.contract_id,
  enabled             boolean not null default true,
  unique (installation_id, kind, path)
);

create table core.installation_bindings (
  installation_id uuid not null references core.installations (id) on delete cascade,
  dataset         core.contract_id not null,
  access          text not null check (access in ('read', 'read-write')),
  primary key (installation_id, dataset)
);

-- What the installer actually provisioned. Pointers only.
create table core.service_registrations (
  id                 uuid primary key default gen_random_uuid(),
  installation_id    uuid not null references core.installations (id) on delete cascade,
  kind               text not null
                       check (kind in ('container', 'service', 'static', 'android', 'browser')),
  external_reference text,
  base_url           text,
  status             text not null default 'provisioning'
                       check (status in ('provisioning', 'running', 'stopped', 'error')),
  registered_at      timestamptz not null default now(),
  last_seen_at       timestamptz
);

create index businesses_org_idx             on core.businesses (organization_id);
create index workspaces_business_idx        on core.workspaces (business_id);
create index installations_business_idx     on core.installations (business_id);
create index installations_status_idx       on core.installations (status);
create index installation_surfaces_inst_idx on core.installation_surfaces (installation_id);
create index service_registrations_inst_idx on core.service_registrations (installation_id);
