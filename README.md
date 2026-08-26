# cybercheck-core

**Platform records only.** This is Step 2 of the App Store foundation.

Core owns tenancy and installation **state**: who exists, and what each business
has installed. It owns neither of the two things it sits between:

| Concern | Owner |
|---|---|
| What products *exist* — catalog, versions, releases | `cybercheck-marketplace` |
| What a business *has installed* | **this repo** |
| Canonical business facts — menus, hours, locations | `cybercheck-data-schema` |

Canonical facts are keyed by the same `business_id` core issues, which is why
uninstalling a product never touches them.

## Tables

**Tenancy** — `organizations`, `org_members`, `businesses`, `workspaces`
**Catalog projection** — `products`, `product_versions`
**Installation state** — `installations`, `installation_permissions`,
`installation_surfaces`, `installation_bindings`, `service_registrations`

Identity lives in `cybercheck-identity`. `org_members` stores only the
membership edge and an external `user_id`.

## Two decisions worth knowing

**An installation pins the manifest it installed with.** `installations.pinned_manifest`
is a copy, not a reference. A later catalog change must never retroactively widen
what a running install may do — changing that is an explicit update that writes a
new pinned manifest.

**Uninstalled rows are kept.** The one-installation-per-product rule is a partial
unique index over `status <> 'uninstalled'`, so history survives and the product
can be reinstalled. Verified: install → uninstall → reinstall leaves the
uninstalled row in place.

## Enforced, not documented

- an `installed` row must record `installed_at`; a `failed` row must record `failure_reason`
- identifiers must be lowercase contract ids; versions must be semver
- surface kinds, binding access modes, workspace kinds and member roles are constrained enums
- workspaces hold `external_reference` and `secret_reference` — pointers only, never secrets

## Tests

```bash
createdb core_test
TEST_DB=core_test ./tests/run_tests.sh
```

13 cases, each asserting a specific rejection or success. A schema that never
rejects anything is not enforcing anything.

## History

Before this, the repo held a Frappe app modelling 28 business entities. That was
the wrong runtime — Frappe is research, not the platform, and canonical facts
belong to `cybercheck-data-schema`. The entity model remains useful and is
recoverable at commit `f65a04d`; it should be ported to `cybercheck-data-schema`
as Postgres migrations rather than revived here.

## License

Proprietary. See `LICENSE`.
