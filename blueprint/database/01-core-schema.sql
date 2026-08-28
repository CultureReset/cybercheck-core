-- Illustrative schema draft based on the supplied architecture.
create table organizations (organization_id uuid primary key, name text not null, created_at timestamptz not null default now());
create table businesses (business_id uuid primary key, organization_id uuid references organizations(organization_id), public_slug text unique, legal_name text, display_name text not null, status text not null default 'active', created_at timestamptz not null default now());
create table users (user_id uuid primary key, email text unique, phone text, created_at timestamptz not null default now());
create table business_members (business_id uuid references businesses(business_id), user_id uuid references users(user_id), role text not null, primary key (business_id,user_id));
create table workspaces (workspace_id uuid primary key, business_id uuid references businesses(business_id), name text not null);
create table nodes (node_id uuid primary key, business_id uuid references businesses(business_id), kind text not null, status text not null, runtime_version text);
create table devices (device_id uuid primary key, node_id uuid references nodes(node_id), platform text not null, label text, status text not null);
create table installations (installation_id uuid primary key, business_id uuid references businesses(business_id), product_id uuid not null, release_id uuid not null, state text not null, manifest_snapshot jsonb not null, installed_at timestamptz);
