# CyberCheck — what this is

Read this first, every session. It exists because the shape of this platform
kept getting re-derived from scratch, and re-derived slightly wrong.

The authoritative spec is `blueprint/` — 28 documents, the contracts, and the
repository boundaries, written before this file. **Where they disagree, the
blueprint wins.** This file is the map from the blueprint to what is actually
built.

## The one-paragraph version

CyberCheck is a **business operating system**. A business signs up, installs
the tools it wants, and the platform holds the one true copy of that business's
facts. One update fans out everywhere that business lives — website, directory,
search, Google, Meta, QR pages, white-label sites, phone assistant — and where
no API exists, it gets there by **driving a real device**: a phone plugged into
a container, a browser, or a Linux desktop. Every push is read back and
verified. Anything unverifiable goes to a repair queue instead of being
reported as done.

It currently runs as **Gulf Coast Radar**, ~4,067 businesses. GCR is the first
tenant, not the platform.

## The three things this platform is made of

**1. The structured business data warehouse.** One canonical business identity
(`business_id`, name, aliases, category, address, phone, hours, coordinates),
then **shared public tables** every business has (contacts, locations, hours,
categories, amenities, media, social profiles, booking links, external
listings, reviews, events, specials, policies, FAQs), then **industry modules**
underneath (restaurant menus; lodging listings; charter captains/boats/trips;
parasailing products; rentals; photographer packages). Every fact carries its
**source and provenance** — source file, row, field, confidence, `observed_at`,
authority. No giant blob table; a business can carry several modules at once.

**2. One update, many outputs.** A canonical change raises an event
(`hours.updated`, `price.updated`, `availability.updated`, `special.updated`,
`policy.updated`) and every authorized output reacts to the same event.
Directories and white-label sites are *outputs of the event bus*, not separate
codebases — which is what makes one API serve many front ends.

**3. The remote control execution layer.** Voice, text, dashboard or phone call
→ understand intent → task router → an ordered task list, one task at a time,
pausing to confirm when needed → three execution lanes:

| lane | what it drives |
|---|---|
| A | Linux desktop — remote session, browser windows, logged-in tools |
| B | Browser — navigate, open profile, fill form, submit |
| C | Phone / device — mirror, open app, tap/type, mobile-only workflows |

Plus a fourth way in that needs no control at all: **the email parser**. Toast,
Square, Clover receipts, FareHarbor and Peek confirmations, reservation emails
and CSV exports get forwarded in, parsed into transactions, orders, bookings,
availability and calendar events, and used to keep public data fresh.

## Repository boundaries

From `blueprint/REPO-STRUCTURE.txt`, with what exists today. The rule there:
**no repository needs to understand the entire platform.**

| tier | repo in the spec | today |
|---|---|---|
| **contracts** | `cybercheck-contracts` | **missing** — spec in `blueprint/contracts/` |
| **foundation** | `cybercheck-identity` | **missing** |
| | `cybercheck-core` | **this repo** — tenancy, identity edges, installation state |
| | `cybercheck-data-schema` | **missing as a repo** — lives in Supabase, reached only through `gcr-api-clean` |
| | `cybercheck-research` | **missing** |
| | `cybercheck-marketplace` | exists, schema only |
| | `cybercheck-orchestrator` | **works** — capability → policy → execute → verify → receipt, fan-out, ADB executor |
| **access** | `cybercheck-gateway` | **`gcr-api-clean` is this** — live, 59k LOC, 70 routes |
| **read / distribution** | `streams`, `search`, `pages/public`, `media` | **all missing** |
| **surfaces** | `cybercheck-admin` | `Admin-dashboard-main` |
| | `cybercheck-business-dashboard` | `Dashboards-users-` |
| | `cybercheck-public` | `gcr-unified` (live) · `cybercheck-web` (new, undeployed) |
| | `cybercheck-developer` | **missing** |
| **runtimes** | `device-runtime` | inside orchestrator — `modules/android_local_node` |
| | `builder` | inside orchestrator — `src/kernel/builder.js` |
| | `browser-runtime`, `compute-runtime` | **missing — lanes A and B do not exist** |
| **proof / ops** | `cybercheck-ledger` | inside orchestrator — `ledger.js`, `signing.js`. External notary not built. |
| | `analytics`, `observability` | **missing** |

### Independent products

The spec lists these as their own repos. Most already exist as routes inside
`gcr-api-clean` — which is why that repo is 59k lines and why splitting it is
the extraction job, not a rewrite:

`bookings` 236 · `availability` 284 · `menu-edit` 231 · `reviews` 222 ·
`messaging` 223 · `google-business` 603 · `meta-webhook` 323 ·
**`email-parser` 1,467** · `qr` 741 · `deals` 318 · `artists` 316 ·
`rides` 662 · `rentals` 316 · `charter` 320 · `links` 83

Not built anywhere: **loyalty**, **song requests**, **Trip Swipe**
(`gcr-trip-swipe*` repos exist but are not wired to the API).

## Facts that keep getting forgotten

**The kernel and the live product have never spoken.** `cybercheck-orchestrator`
runs its own Postgres. The businesses are in Supabase. The operating system and
the product are two separate systems.

**Billing does not exist.** In any repo. `price_tiers` is the only
billing-adjacent table anywhere.

**Only lane C exists.** The phone lane works. Linux desktop and browser control
are specified and unbuilt.

**The blueprint is a spec, not code.** `blueprint/database/*.sql` is 41 lines
total and says "illustrative schema draft" at the top. The 28 docs are the
substance.

## Rules that hold, and must keep holding

**The slug never comes from the request.** `middleware/ownerAuth.js` resolves
the business from the session token via `entity_owners`. Nothing in a request
can change the answer. This is the entire security model.

**Renderers are chosen by shape, not by name.** A table nobody has heard of
gets the right layout because its rows look like rows with a name and a price.
`cybercheck-web/src/lib/shape.js`.

**The kernel names no package.** Providers volunteer with `defaultPriority`;
capabilities declare their own `canonicalKey`. `tests/modularity.mjs` fails on
any list of package names in the kernel.

**Apps do not add screens.** One dashboard, sections from data. Twenty's app
model was ported *minus* every screen-adding primitive.

**Every fact keeps its source.** Provenance is part of the warehouse, not an
add-on: authority ranking is what stops a nightly scrape overwriting what the
owner typed this morning.

## Open source: what is taken from where

Forked to be cut apart and self-hosted. None of these are services anyone else
runs.

| fork | license | take | status |
|---|---|---|---|
| **huly-platform** | EPL-2.0 | `workbench` + `view`; **`billing`** (3,735 lines); `process` (workflow) | `plugins/cybercheck` scaffolded |
| **twenty-CRM** | AGPL-3.0 | `sdk/define` — manifest vocabulary | **ported** to orchestrator `src/define/` |
| **mindfs** | AGPL-3.0 | relay tunnel (2,839 lines Go); plugin write-back contract (377 lines) | not taken |
| **modular-mojo** | Apache-2.0 | MAX as the `model` provider — self-hosted inference, because renting a model API is the dependency the device runtime exists to avoid | not taken |
| foundations-cloudflare | BSD-3 | nothing — Rust service plumbing | — |

**License filing:** keep lifted files in their own directory, headers intact.
EPL is file-level and stays contained; AGPL spreads if blended into your own
files.

## Dead ends — do not re-investigate

- **`gcr-api-v2`, `gcr-unified-v2`** — single-commit snapshots from 2026-07-20,
  *"Initial copy … starting point for structured-data rebuild"*, never touched
  again. `gcr-api-v2` has **zero** files `gcr-api-clean` lacks; the reverse is
  51 files and 61 commits. The only thing unique to `gcr-unified-v2` is a
  committed `.env.vercel`.
- **8 empty repos** — `Artist-`, `Reviews`, `Universal-dashboard-`,
  `cyber-check-`, `cybercheck-cloud`, `launching-gcr-json`, `qr-menu`,
  `saas-cybercheck`.
- **`routes/dashboard.js`** — 5,640 lines, 206 handlers, 6 reachable endpoints.
  `routes/business-data.js` (304 lines) replaced it generically.

## Known security issue

The live Supabase **`service_role`** key — full read/write, bypasses row-level
security — is committed in public repos: `gcr-api-clean/run_migration.js`,
`gcr-api-v2/run_migration.js`, `gcr-trip-swipe-new/populate-all-data.js`,
`gcr-unified/dump-entire-db.mjs`, `gcr-unified/export-supabase-complete.mjs`,
and the same two in `gcr-unified-v2`. Valid until 2036.

Rotate in Supabase, **then** update `SUPABASE_SERVICE_ROLE_KEY` in Vercel — in
that order, or the API is down between the steps. Deleting the files does not
fix it; history and forks keep the key.

Also leaked: `xbptmkpbiqzvxptjkfoi` (`gar-front-end-data`),
`adpnhipmdefutkzzltbs` (`live-gcr`), `lvmsmjlallptylonscat` (`ghost-ai/.env`).
