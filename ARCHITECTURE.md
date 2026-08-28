# CyberCheck — what this is

Read this first, every session. It exists because the shape of this platform
kept getting re-derived from scratch and re-derived slightly wrong.

## The one-paragraph version

CyberCheck is a **business operating system**. A business signs up, picks the
tools it wants, and the platform holds the one true copy of that business's
facts. When a fact changes, the platform pushes it everywhere that business
lives — including apps with no API, by **driving a real Android device** plugged
into a container. Every push is read back and verified; anything that cannot be
verified goes to a repair queue rather than being reported as done.

It currently runs as **Gulf Coast Radar**, a Gulf Coast directory with ~4,067
businesses. GCR is the first tenant of the platform, not the platform.

## Four layers, one API

    ┌─────────────┐  ┌──────────────┐  ┌────────────────────────────┐
    │   ADMIN     │  │     USER     │  │   FRONT ENDS (many)        │
    │  dashboard  │  │  dashboard   │  │  GCR · a chamber · a niche │
    └──────┬──────┘  └──────┬───────┘  └─────────────┬──────────────┘
           └────────────────┴────────────────────────┘
                            │
                   ┌────────▼─────────┐
                   │    API LAYER     │   the only thing that touches data
                   └────────┬─────────┘
                            │
              ┌─────────────▼──────────────┐
              │ data plane · device runtime │
              └─────────────────────────────┘

**Only the API layer talks to the database.** No dashboard holds a database
key. No front end holds one. This is already true and must stay true.

### The part that does not exist yet

A front end is **not** hardcoded to a directory. The API decides what a given
front end may publish, so a chamber of commerce directory, a niche directory
and GCR are three configurations of the same API, not three codebases.

Today `entity` is one flat table and there is no notion of *which directory a
business appears in*. That is the missing piece, and it is a data-model change
before it is a UI change.

## What exists today, honestly

| layer | repo | state |
|---|---|---|
| API | **gcr-api-clean** | **live.** 59,034 LOC, 70 route files. Deployed. Supabase `mkepugvdlktfsossumox`. |
| user dashboard | **Dashboards-users-** | **live.** Sections discovered from data, not a fixed list. |
| public front end | **gcr-unified** | **live.** But `BusinessDetail.jsx` is 2,467 lines with zero `sections.map()` — the one surface that never got the registry treatment. |
| admin | **Admin-dashboard-main** | **live.** 86 registered screens. |
| new front end | **cybercheck-web** | built, not deployed. 13 renderers chosen by data shape; a check script fails the build on any hardcoded slug, host, industry or section list. |
| kernel | **cybercheck-orchestrator** | works, **never connected to the live API.** Capability → policy → execute → verify → receipt. Fan-out. Android executor over ADB. |
| platform records | **cybercheck-core** (here) | schema only: tenancy, identity, installation state. |
| catalog | **cybercheck-marketplace** | schema only. |
| foundation fork | **huly-platform** | `plugins/cybercheck` + `models/cybercheck` scaffolded. EPL-2.0. |

### Two facts that keep getting forgotten

**The kernel and the live product have never spoken.** `cybercheck-orchestrator`
runs its own Postgres. The 4,067 businesses are in Supabase. The operating
system and the product are two separate systems.

**Billing does not exist.** Not in any repo. The only billing-adjacent table
anywhere is `price_tiers`. This is the largest single gap.

## Rules that already hold, and must keep holding

**The slug never comes from the request.** `middleware/ownerAuth.js` resolves
which business a caller is from the session token via `entity_owners`.
Handlers filter on `req.entitySlug`. There is nothing in a request that can
change the answer. This is the entire security model.

**Renderers are chosen by shape, not by name.** A table nobody has heard of
gets the right layout because its rows look like rows with a name and a price —
not because someone added it to a list. `cybercheck-web/src/lib/shape.js`.

**The kernel names no package.** Providers volunteer with `defaultPriority`;
capabilities declare their own `canonicalKey`. Anywhere the kernel keeps a list
of package or capability names is a bug, and `tests/modularity.mjs` fails on it.

**Apps do not add screens.** One dashboard, sections from data. This is why
Twenty's app model (`defineNavigationMenuItem`, `definePageLayoutTab`) was
ported *minus* every screen-adding primitive.

## Open source: what is taken from where

Forked to be cut apart, not adopted. All self-hosted; none of these are
services anyone else runs.

| fork | license | take | status |
|---|---|---|---|
| **huly-platform** | EPL-2.0 | `workbench` (one shell) + `view`; **`billing`** (3,735 lines) — the gap above; `process` (workflow) | plugin scaffolded |
| **twenty-CRM** | AGPL-3.0 | `sdk/define` — the manifest vocabulary | **ported** into orchestrator `src/define/` |
| **mindfs** | AGPL-3.0 | the relay tunnel (2,839 lines Go — reach a machine behind a firewall); the plugin write-back contract (377 lines) | not taken yet |
| **modular-mojo** | Apache-2.0 | MAX as the `model` provider — self-hosted inference, because renting a model API is the dependency the device runtime exists to avoid | not taken yet |
| foundations-cloudflare | BSD-3 | nothing — Rust service plumbing, wrong language, no business features | — |

**License filing rule:** keep lifted files in their own directory with headers
intact. EPL is file-level and stays contained. AGPL spreads if blended into
your own files.

## Dead ends — do not re-investigate

- **`gcr-api-v2`, `gcr-unified-v2`** — single-commit snapshots from 2026-07-20,
  message: *"Initial copy … starting point for structured-data rebuild."*
  Never touched again. `gcr-api-v2` contains **zero** files `gcr-api-clean`
  lacks; `gcr-api-clean` has 51 it lacks and 61 commits to its 1. The only
  thing unique to `gcr-unified-v2` is a committed `.env.vercel`.
- **8 empty repos** — `Artist-`, `Reviews`, `Universal-dashboard-`,
  `cyber-check-`, `cybercheck-cloud`, `launching-gcr-json`, `qr-menu`,
  `saas-cybercheck`. Zero files each.
- **`routes/dashboard.js`** (5,640 lines, 206 handlers) — only 6 endpoints are
  still reachable from any live front end. `routes/business-data.js` (304
  lines) replaced it generically.

## Known security issue

The live Supabase **`service_role`** key — full read/write, bypasses row-level
security — is committed in public repos: `gcr-api-clean/run_migration.js`,
`gcr-api-v2/run_migration.js`, `gcr-trip-swipe-new/populate-all-data.js`,
`gcr-unified/dump-entire-db.mjs`, `gcr-unified/export-supabase-complete.mjs`,
and the same two files in `gcr-unified-v2`. Valid until 2036.

Rotate in Supabase, **then** update `SUPABASE_SERVICE_ROLE_KEY` in Vercel — in
that order, or the API goes down between the two steps. Deleting the files does
not fix it; git history and forks keep the old key.

Other projects also leaked: `xbptmkpbiqzvxptjkfoi` (`gar-front-end-data`),
`adpnhipmdefutkzzltbs` (`live-gcr`), `lvmsmjlallptylonscat` (`ghost-ai/.env`).
