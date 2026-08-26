#!/usr/bin/env bash
# Constraint tests. A schema that never rejects anything is not enforcing anything,
# so every case here asserts a specific failure or a specific success.
set -uo pipefail

DB="${TEST_DB:-core_test}"
MIGRATIONS="$(cd "$(dirname "$0")/../migrations" && pwd)"
PASS=0; FAIL=0

run_sql() { psql -v ON_ERROR_STOP=1 -q -d "$DB" -c "$1" 2>&1; }

expect_ok() {
  local name="$1" sql="$2" out
  if out=$(run_sql "$sql"); then
    PASS=$((PASS+1)); printf '  ok    %s\n' "$name"
  else
    FAIL=$((FAIL+1)); printf '  FAIL  %s\n        expected success, got: %s\n' "$name" "$(echo "$out" | head -2 | tr '\n' ' ')"
  fi
}

expect_fail() {
  local name="$1" sql="$2" want="$3" out
  if out=$(run_sql "$sql"); then
    FAIL=$((FAIL+1)); printf '  FAIL  %s\n        expected rejection, but it was accepted\n' "$name"
  elif echo "$out" | grep -qi "$want"; then
    PASS=$((PASS+1)); printf '  ok    %s\n' "$name"
  else
    FAIL=$((FAIL+1)); printf '  FAIL  %s\n        rejected, but not for %s: %s\n' "$name" "$want" "$(echo "$out" | head -2 | tr '\n' ' ')"
  fi
}

echo "Rebuilding $DB"
dropdb --if-exists "$DB" >/dev/null 2>&1
createdb "$DB"
for file in "$MIGRATIONS"/*.sql; do
  psql -v ON_ERROR_STOP=1 -q -d "$DB" -f "$file" || { echo "migration failed: $file"; exit 1; }
done

psql -q -d "$DB" <<'SEED'
insert into core.organizations (id, slug, name)
  values ('11111111-1111-1111-1111-111111111111', 'culturereset', 'CultureReset');
insert into core.businesses (id, organization_id, slug, name)
  values ('22222222-2222-2222-2222-222222222222', '11111111-1111-1111-1111-111111111111', 'coastal-grill', 'Coastal Grill');
insert into core.products (id, slug, name, publisher)
  values ('33333333-3333-3333-3333-333333333333', 'qr-menu', 'QR Menu', 'culturereset');
insert into core.product_versions (id, product_id, version, manifest)
  values ('44444444-4444-4444-4444-444444444444', '33333333-3333-3333-3333-333333333333', '1.0.0', '{"product":"qr-menu"}');
SEED

echo
echo "core identifiers"
expect_fail "organization slug must be lowercase contract id" \
  "insert into core.organizations (slug, name) values ('CultureReset', 'x');" "contract_id"
expect_fail "product version must be semver" \
  "insert into core.product_versions (product_id, version, manifest) values ('33333333-3333-3333-3333-333333333333', '1.0', '{}');" "semver"

echo
echo "installation lifecycle"
expect_ok "a business can install a product" \
  "insert into core.installations (id, business_id, product_id, product_version_id, pinned_manifest, status, installed_at)
   values ('55555555-5555-5555-5555-555555555555','22222222-2222-2222-2222-222222222222','33333333-3333-3333-3333-333333333333','44444444-4444-4444-4444-444444444444','{}','installed', now());"
expect_fail "the same product cannot be installed twice while live" \
  "insert into core.installations (business_id, product_id, product_version_id, pinned_manifest, status, installed_at)
   values ('22222222-2222-2222-2222-222222222222','33333333-3333-3333-3333-333333333333','44444444-4444-4444-4444-444444444444','{}','installed', now());" \
  "installations_one_live_per_product"
expect_fail "an installed row must record when it was installed" \
  "insert into core.installations (business_id, product_id, product_version_id, pinned_manifest, status)
   values ('22222222-2222-2222-2222-222222222222','33333333-3333-3333-3333-333333333333','44444444-4444-4444-4444-444444444444','{}','installed');" \
  "installed_has_timestamp"
expect_fail "a failed row must record why it failed" \
  "insert into core.installations (business_id, product_id, product_version_id, pinned_manifest, status)
   values ('22222222-2222-2222-2222-222222222222','33333333-3333-3333-3333-333333333333','44444444-4444-4444-4444-444444444444','{}','failed');" \
  "failed_has_reason"
expect_ok "uninstalling frees the slot" \
  "update core.installations set status='uninstalled', uninstalled_at=now() where id='55555555-5555-5555-5555-555555555555';"
expect_ok "the product can be reinstalled after uninstall" \
  "insert into core.installations (business_id, product_id, product_version_id, pinned_manifest, status, installed_at)
   values ('22222222-2222-2222-2222-222222222222','33333333-3333-3333-3333-333333333333','44444444-4444-4444-4444-444444444444','{}','installed', now());"
expect_ok "the uninstalled row is kept as history" \
  "do \$\$ begin if (select count(*) from core.installations where status='uninstalled') <> 1 then raise exception 'history lost'; end if; end \$\$;"

echo
echo "sockets"
expect_fail "an unknown surface kind is rejected" \
  "insert into core.installation_surfaces (installation_id, kind, path)
   values ('55555555-5555-5555-5555-555555555555','billboard','/x');" "check constraint"
expect_fail "an unknown binding access mode is rejected" \
  "insert into core.installation_bindings (installation_id, dataset, access)
   values ('55555555-5555-5555-5555-555555555555','menu','delete');" "check constraint"
expect_fail "an unknown workspace kind is rejected" \
  "insert into core.workspaces (business_id, name, kind)
   values ('22222222-2222-2222-2222-222222222222','w','teleporter');" "check constraint"
expect_fail "an unknown org member role is rejected" \
  "insert into core.org_members (organization_id, user_id, role)
   values ('11111111-1111-1111-1111-111111111111','usr_1','wizard');" "check constraint"

echo
if [ "$FAIL" -gt 0 ]; then echo "FAILED: $PASS passed, $FAIL failed"; exit 1; fi
echo "OK: $PASS passed"
