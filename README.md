# CyberCheck Core

The CyberCheck control plane, built as a [Frappe](https://github.com/frappe/frappe) app.

CyberCheck is the control plane; open-source projects are engines underneath it.
This app owns identity, tenants, and **installation state** — not module code and
not the module catalog.

## What lives here

| DocType | Purpose |
|---|---|
| `Business` | The tenant. Everything else hangs off `business_id`. |
| `CyberCheck Installed App` | Which modules a business has installed, at what version, in what runtime, and whether it is active. |
| `CyberCheck App Permission` | Capabilities granted to one install. |

## What deliberately does not live here

The **catalog** is separate from **installation state**.

- The catalog ("what apps exist?") is a registry of JSON manifests in its own
  repository. Titles, icons, and descriptions come from there.
- This app stores only what a given business has installed. `app_id` is a
  manifest id such as `song-requests` or `browser.playwright`.

Per the foundation rules, the central database also does **not** hold customer
passwords, third-party session secrets, or private workspace files. Those stay in
the private workspace and secret store; only secret *references* belong here.

## API

`GET /api/method/cybercheck_core.api.me` returns identity, business, and installs:

```json
{
  "user": "matt@example.com",
  "business": { "id": "Example Marina", "name": "Example Marina", "slug": "example-marina" },
  "installed_apps": [
    { "id": "menu", "version": "1.2.0", "runtime": "frappe", "status": "Active" }
  ]
}
```

The frontend renders whatever modules come back, rather than hard-coding a menu.
It joins `id` against the registry manifest to get the title and icon.

## Runtimes

An install declares how it runs, so one catalog can serve several backends:

- `frappe` — a structured-data Frappe app
- `container` — a container module deployed through the orchestrator
- `android` — a device capability module
- `ui` — frontend only

## Development

```bash
bench get-app https://github.com/CultureReset/cybercheck-core --branch cybercheck-main
bench --site <site> install-app cybercheck_core
bench --site <site> run-tests --app cybercheck_core
```

Requires Frappe `develop` (v17), which needs Python 3.14 and Node 24.

## License

MIT. See `license.txt`.

CyberCheck Core depends only on `frappe/frappe`, which is MIT. It deliberately
does not depend on `frappe/press` (AGPL-3.0) or `frappe/marketplace` (no LICENSE
file at time of writing).
