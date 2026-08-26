# CyberCheck Core

The CyberCheck control plane and canonical data model, built as a
[Frappe](https://github.com/frappe/frappe) app.

CyberCheck is the control plane; open-source projects are engines underneath it.

## Data, apps and executors are three different things

- **Data** — the permanent structured business information. It lives here, in real
  relational tables, and it is not owned by any app.
- **Apps** — optional functionality a business installs. Apps *use* the data; they
  are not the data. Hours, menus and events are data, not apps.
- **Executors** — the things that actually perform actions (browser, Android,
  container, API, SMS). Apps call executors.

Each table is defined as a DocType. The `.json` file is the *source-code definition
of the schema*, not a place customer data is stored — Frappe reads it and creates a
real SQL table. Business data stays normalized across those tables, never shoved
into a JSON column.

## Universal foundation schema

Everything connects through `business`, so nothing duplicates the tenant.

**Tenant**
| Table | Holds |
|---|---|
| `Business` | The tenant. Everything hangs off it. |
| `Business Location` | Physical locations, address, coordinates, timezone |
| `Business Relationship` | Parent, subsidiary, franchise, partner, vendor links |
| `Business Contact` | People at the business |

**Descriptive**
| Table | Holds |
|---|---|
| `Business Hours` | Per-day opening hours, with validity windows |
| `Business Media` | Images, video, documents, attachable to any record |
| `Category` | Hierarchical classification |
| `Business Tag` | Free-form labels |
| `Amenity` | Features a business offers |

**Offerings**
| Table | Holds |
|---|---|
| `Service` | Something the business does |
| `Product` | Something the business sells |
| `Price` | Prices, attachable to a service or product, with validity windows |
| `Availability` | Capacity and remaining slots over a time window |

**Content**
| Table | Holds |
|---|---|
| `Business Event` | Scheduled events |
| `Special` | Promotions and discounts |
| `Policy` | Cancellation, refund, privacy, terms |
| `FAQ` | Questions and answers |
| `Review` | Reviews, with the source they came from |

**Provenance**
| Table | Holds |
|---|---|
| `Source` | Where data comes from: manual, website, API, scrape, device, import |
| `Source Record` | Provenance of one record, with a *reference* to the payload |
| `External Identifier` | The business's id on an external platform |

**Platform**
| Table | Holds |
|---|---|
| `Module Installation` | Which modules a business has, version, runtime, status |
| `Module Permission` | Capabilities granted to one install |
| `Device` | Android, browser or container devices |
| `Private Workspace` | Isolated workspaces, by *reference* to the orchestrator |
| `Task` | Requested work, with priority and schedule |
| `Approval` | Who approved a task and when |
| `Execution` | One attempt to run a task on an executor |
| `Execution Proof` | Screenshot, video, DOM snapshot or log, by reference |

Four names are namespaced because Frappe core already owns them: `Contact`, `Tag`,
`Event` and `Workspace` became `Business Contact`, `Business Tag`, `Business Event`
and `Private Workspace`.

## What deliberately does not live here

- **The module catalog.** "What apps exist" is a registry of JSON manifests in its
  own repository. Titles, icons and descriptions come from there. This app stores
  only *installation state*; `app_id` is a manifest id such as `song-requests` or
  `browser.playwright`.
- **Secrets and private files.** No customer passwords, third-party session
  secrets, or private workspace files. `Private Workspace.secret_reference`,
  `Source Record.payload_reference` and `Execution Proof.storage_reference` hold
  *pointers*; the artifacts live in the secret store and private workspace.

## API

`GET /api/method/cybercheck_core.api.me` returns identity, businesses and installs:

```json
{
  "user": "matt@example.com",
  "business": { "id": "Example Marina", "name": "Example Marina", "slug": "example-marina" },
  "businesses": [ { "id": "Example Marina", "name": "Example Marina", "slug": "example-marina" } ],
  "installed_apps": [
    { "id": "menu", "version": "1.2.0", "runtime": "frappe", "status": "Active" }
  ]
}
```

Pass `business` to select one when a user owns several; requesting a business the
user does not own raises `PermissionError`. The frontend renders whatever modules
come back rather than hard-coding a menu, joining `id` against the registry
manifest for the title and icon.

## Runtimes

An install declares how it runs, so one catalog serves several backends:
`frappe`, `container`, `android`, `ui`.

## Development

```bash
bench get-app https://github.com/CultureReset/cybercheck-core --branch cybercheck-main
bench --site <site> install-app cybercheck_core
bench --site <site> run-tests --app cybercheck_core
```

Requires Frappe `develop` (v17), which needs Python 3.14 and Node 24.

## Not yet built

Industry extensions on top of this foundation: restaurant (`Menu`, `Menu Section`,
`Menu Item`, `Modifier`, `Happy Hour`), tourism (`Rental Product`, `Trip`,
`Session`, `Inventory Unit`, `Blackout Date`), marine (`Vessel Listing`,
`Charter Product`), salon (`Provider`, `Appointment Slot`), home services
(`Service Area`, `Job Type`, `Estimate`, `Technician`).

## License

MIT. See `license.txt`.

Depends only on `frappe/frappe`, which is MIT. It deliberately does not depend on
`frappe/press` (AGPL-3.0) or `frappe/marketplace` (no LICENSE file at time of
writing), both verified at the commits in use.
