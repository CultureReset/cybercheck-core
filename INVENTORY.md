# What you actually have

Every number here was read off the code on 2026-08-28. Nothing is estimated.

The short version: **you have built this platform at least four times.** Each
generation left behind a working piece the next one never picked up. Almost
nothing is finished, but very little needs to be invented — most of what the
platform needs already exists somewhere in the account, in an older repo.

---

## 1. The database — what is actually in it

`Data` (public) is the most valuable repo in the account. It is a live,
read-only audit of the production database, and it answers questions the design
documents only guess at.

- **295 tables carry `entity_slug`. 175 have rows. 120 are completely empty.**
- **4,067 businesses** in `entity`
- **4,476 per-business dumps** in `data-by-slug/`, one file each
- `table-stats.csv`, `industry-table-matrix.csv`, `subtype-table-matrix.csv`,
  `GAP-ANALYSIS.md`, `INDUSTRY-TABLE-REQUIREMENTS.md`, `FAILED-tables.txt`

The tables with real weight:

| table | rows | businesses |
|---|---|---|
| `entity_tags` | 83,480 | 3,194 |
| `entity_photos` | 52,191 | 2,789 |
| `entity_nearby_landmark_types` | 42,036 | 2,252 |
| `entity_modules` | 37,847 | 2,856 |
| `search_index` | 35,182 | 4,034 |
| `ai_photo_index_full` | 27,766 | 2,547 |
| `ai_entity_intent_tags_full` | 27,275 | 2,876 |
| `entity_attributes` | 21,744 | 2,332 |
| `entity_offer` | 18,138 | 1,478 |
| `entity_hours` | 15,116 | 2,137 |
| `catalog_items` | 12,216 | 216 |
| `menu_items` | 11,147 | 205 |
| `entity_reviews` | 10,988 | 2,248 |
| `entity_google_reviews` | 10,591 | 2,225 |
| `entity` | 4,067 | 4,067 |

**The 120 empty tables are the honest map of what does not work yet.** The
biggest cluster, quoted from your own gap analysis:

> **Booking / availability / calendar (14 tables) — the biggest single gap.**
> You have `bookable_resources` (1,055 rows) describing WHAT can be booked, but
> nothing tracking an actual booking, a calendar slot, or availability. The
> booking flow has no backing tables at all.

Also entirely empty: **customer / commerce / loyalty (16 tables)** — no
customer accounts, no order history, no loyalty tracking anywhere. And
`business_staff` — no staff, schedules or roles for any business.

So: the directory half of the platform is real and full. The transactional
half — booking, ordering, customers, loyalty, staff — is schema with nothing
in it.

---

## 2. The App Store already exists — 66 apps, already written

`cybercheck-login/apps/` (public) holds **69 files: 66 app manifests plus
`_categories.json`, `_presets.json` and `index.json`.**

The format, from `menu.json`:

```json
{ "id": "menu", "name": "Menu", "icon": "🍽️", "cat": "content", "price": 0,
  "desc": "Digital menu with sections, items, prices. One QR code, always current.",
  "block":      { "title": "Full Menu", "sub": "Browse the menu with prices" },
  "setup":      [ { "key": "style", "label": "Menu style", "type": "select",
                    "options": ["Text list", "With photos"], "def": "Text list" } ],
  "dataKey":    "menu_items",
  "fields":     [ { "key": "name", "label": "Item name", "type": "text" }, … ],
  "publicData": true }
```

Every app declares its install-time questions (`setup`), the table it owns
(`dataKey`), its editor form (`fields`), whether it appears publicly
(`publicData`), its category and its price.

The 66: about, addons, ai-concierge, analytics, availability, book-boat,
book-charter, book-class, book-dolphin, book-hairstylist, book-lodging,
book-photographer, booking, checklist, checkout, client-galleries, contact,
coupons, crowdfund, cta, customers, email-parser, events, faq, features, fleet,
footer, forms, gallery, gcr-listing, gift-cards, guest-videos, hero, highlight,
hours, inventory, links, locations, loyalty, memberships, menu, messaging,
oauth-google, oauth-instagram, oauth-square, ordering, payments, properties,
qr-codes, qr-redirect, reminders, reserve-table, reviews, reward-offers,
richtext, rides, seo, services, shoutouts, song-request, specials, staff,
steps, tipjar, waitlist, waivers.

And `_presets.json` bundles them by industry — `restaurant` installs 18 apps:
hero, about, menu, specials, events, booking, ordering, gift-cards, reviews,
hours, gallery, messaging, customers, qr-codes, cta, contact, footer, seo.

**This is the modular app model, fully specified. Do not recreate it from
memory.**

---

## 3. There are two orchestrators, not one

`check-mate-` (private, 200 MB) contains a complete earlier generation of the
execution platform that `cybercheck-orchestrator` was rebuilt without.

`check-mate-/voice-ai/` — **~29,000 lines of TypeScript across 24 subsystems**,
plus a **1,453-line Prisma schema with 35 models**:

| subsystem | lines | | subsystem | lines |
|---|---|---|---|---|
| `agents` | 5,988 | | `automation` | 1,445 |
| `templates` | 2,817 | | `ai-providers` | 1,411 |
| `concierge` | 2,665 | | `ai` | 1,409 |
| `testing` | 2,200 | | **`computer-use`** | **1,346** |
| `components` | 2,062 | | `monitoring` | 1,004 |
| `workflows` | 1,424 | | `deployment` | 886 |

`computer-use/` is `browser-engine.ts`, `screen-understanding.ts`, `actions.ts`
— **the browser execution lane the current orchestrator does not have.**
`ai-providers/` covers OpenAI, Anthropic, Grok, Gemini, Azure, Watson behind a
registry. `provisioner`, `sandbox`, `queue`, `router`, `governance`,
`marketplace` all exist.

**Be careful with it.** Its own `WHATS-LEFT-TO-BUILD.md` marks core pieces
`❌ NOT BUILT` — the automation executor, the scheduler, agent logging, the
preference manager. Models exist in the schema without the code behind them. It
is not 95% done, whatever the other status files say. But ~29,000 lines is real,
and the orchestrator should be reconciled against it rather than extended past
it.

Also in `check-mate-`:

- `app-store-api/` — `marketplace.routes.js`, `developer.routes.js`,
  `admin.routes.js`, `sandbox.routes.js`
- `modules/` — 23 HTML modules: ai-assistant, analytics, calendar, contacts,
  contacts-mobile, custom-fields-manager, leads, loyalty-rewards, menu-manager,
  profile-editor, profile-templates, reviews, settings, sms-automations, tasks,
  usage, voice-calls, voice-notes
- `ghost-os/` (32 files), `dashboard-unified/` (99), `dashboard/` (73),
  `restaurant/` (141), `store/` (35), `api/` (70)

---

## 4. The owner dashboard was already built, twice

`cybercheck-dashboard` (public) — **51 JavaScript files, 14,921 lines**, with
real CRUD, not mockups:

`billing.js` · `seo.js` · `bookings.js` · `availability.js` · `coupons.js` ·
`social.js` · `reviews.js` · `staff.js` · `waivers.js` · `oauth.js` ·
`theme.js` · `messaging.js` · `analytics.js` · `locations.js` · `domain.js` ·
`profile.js` · `addons.js` · `site-editor.js` · `calendar-view.js` ·
`module-loader.js` · `shared-data.js` · `details.js` · `upload.js` · `router.js`

Note `billing.js` — billing was written here before I ported Huly's.

`gulf-coast-radar` (public) has a `CYBERCHECK-MODULAR-PLATFORM/` directory with
`modules-dashboard/app-store.html`, `module-loader.js` and `bookings-unified.js`
— an even earlier App Store generation.

---

## 5. The ingestion layer already exists

`cyber-admin` (private, **2.2 GB**) is where the data came from.

- `apps/` — ai-training, analytics, biopage, booking, loyalty, menu, ordering,
  referrals, sms, sms-automation, social
- `business-data/` — **450 per-business JSON files**
- `rag-api/` (Python), `scraper-deployment/`, `gcr-dedup-tool.py`,
  `import-4-businesses.js`, `gcr-directory` / `-v2` / `-cleaned`
- Pullers and importers for WordPress, Toast and Wix; dedupe, merge and
  completeness auditing
- Per-vertical builds: circleboats, charter-fishing, no-shoes, taxi, luna-sea,
  galley-restaurant, beachside

`cybercheck-api-database` (public, 726 MB) is the schema archaeology — full SQL,
schema variations, entity audits, data dictionaries, Google Place ID matching,
orphan recovery, photo indexing. **Freeze it and use it for migration fixtures.
Do not clean it up into production.**

---

## 6. What is actually running today

| | repo | state |
|---|---|---|
| API | `gcr-api-clean` | **live** — 59,034 lines, 70 route files, Supabase `mkepugvdlktfsossumox` |
| owner dashboard | `Dashboards-users-` | **live** — sections discovered from data |
| public directory | `gcr-unified` | **live** |
| admin | `Admin-dashboard-main` | **live** — 86 screens |

Independent products already inside `gcr-api-clean` as routes:
`email-parser` (1,467 lines) · `qr` (741) · `rides` (662) · `google-business`
(603) · `meta-webhook` (323) · `charter` (320) · `deals` (318) · `artists` (316)
· `rentals` (316) · `availability` (284) · `bookings` (236) · `menu-edit` (231)
· `messaging` (223) · `reviews` (222) · `links` (83)

Splitting those into packages is **extraction, not rebuilding**.

---

## 7. The honest summary

**You are not missing code. You are missing one assembled copy of it.**

- the app catalogue exists — `cybercheck-login/apps` (66 manifests + presets)
- the owner dashboard exists — `cybercheck-dashboard` (51 modules, 14,921 lines)
- the CRM modules exist — `check-mate-/modules` (23) and `dashboard-unified` (99)
- the agent/execution platform exists twice — `check-mate-/voice-ai` (~29k lines)
  and `cybercheck-orchestrator`
- the marketplace API exists — `check-mate-/app-store-api` (4 route files)
- the ingestion layer exists — `cyber-admin`
- the data exists — 4,067 businesses, 175 populated tables
- the schema truth exists — `Data`

What genuinely does not exist anywhere, confirmed against the live database:

1. **Booking.** 14 tables, all empty. `bookable_resources` says what can be
   booked; nothing records that anything was.
2. **Customers, orders, loyalty.** 16 tables, all empty.
3. **Staff.** `business_staff` empty for every business.
4. **A connection between the kernel and the live product.** They run on
   separate databases and have never spoken.

Everything else is a question of which generation has the best version, and
moving it — not writing it.
