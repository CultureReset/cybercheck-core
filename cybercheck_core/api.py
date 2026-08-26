import frappe


@frappe.whitelist()
def me(business: str | None = None) -> dict:
	"""Identity, businesses and installed modules for the session user."""
	owned = businesses_for_user(frappe.session.user)
	selected = select_business(business, owned)
	return {
		"user": frappe.session.user,
		"business": business_summary(selected),
		"businesses": [business_summary(name) for name in owned],
		"installed_apps": installed_apps(selected),
	}


def businesses_for_user(user: str) -> list[str]:
	"""Active businesses this user owns, oldest first."""
	return frappe.get_all(
		"Business",
		filters={"owner_user": user, "status": "Active"},
		pluck="name",
		order_by="creation asc",
	)


def select_business(requested: str | None, owned: list[str]) -> str | None:
	"""The business to report on. A requested one must be owned by the user."""
	if not requested:
		return owned[0] if owned else None

	if requested not in owned:
		frappe.throw(
			f"You do not have access to business {requested!r}.", frappe.PermissionError
		)
	return requested


def business_summary(business: str | None) -> dict | None:
	if not business:
		return None

	doc = frappe.get_cached_doc("Business", business)
	return {"id": doc.name, "name": doc.business_name, "slug": doc.slug}


def installed_apps(business: str | None) -> list[dict]:
	"""Active installs for a business.

	Only install state lives here. Titles and icons come from the registry
	manifest, so the catalog stays separate from what a customer has.
	"""
	if not business:
		return []

	return frappe.get_all(
		"Module Installation",
		filters={"business": business, "status": "Active"},
		fields=["app_id as id", "app_version as version", "runtime", "status"],
		order_by="app_id",
	)
