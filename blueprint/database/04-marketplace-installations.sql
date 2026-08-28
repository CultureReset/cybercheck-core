create table products (product_id uuid primary key, developer_id uuid, name text not null, status text not null);
create table product_versions (version_id uuid primary key, product_id uuid references products(product_id), version text not null, manifest jsonb not null);
create table releases (release_id uuid primary key, version_id uuid references product_versions(version_id), channel text not null, published_at timestamptz);
create table installation_permissions (installation_id uuid not null, permission_id text not null, state text not null, primary key (installation_id,permission_id));
create table installation_bindings (installation_id uuid not null, dataset_id text not null, access_mode text not null, primary key (installation_id,dataset_id));
