-- Canonical business data stays relational.
create table business_hours (hour_id uuid primary key, business_id uuid not null, location_id uuid, weekday smallint, opens_at time, closes_at time, valid_from date, valid_until date, verification_status text, current_version_id uuid);
create table services (service_id uuid primary key, business_id uuid not null, name text not null, description text, active boolean not null default true, current_version_id uuid);
create table service_pricing (pricing_id uuid primary key, service_id uuid not null references services(service_id), basis text not null, amount numeric, currency text, valid_from date, valid_until date);
create table resources (resource_id uuid primary key, business_id uuid not null, resource_type text not null, name text not null, capacity integer);
create table availability (availability_id uuid primary key, business_id uuid not null, resource_id uuid references resources(resource_id), service_id uuid references services(service_id), starts_at timestamptz not null, ends_at timestamptz not null, quantity_available integer);
create table entity_relationships (relationship_id uuid primary key, subject_id uuid not null, relationship_type text not null, object_id uuid not null, valid_from timestamptz, valid_until timestamptz);
