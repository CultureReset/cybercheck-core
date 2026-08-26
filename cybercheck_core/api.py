import frappe


@frappe.whitelist()
def me() -> dict:
	"""Identity, business and installed modules for the session user."""
	business = business_for_user(frappe.session.user)
	return {
		"user": frappe.session.user,
		"business": business_summary(business),
		"installed_apps": installed_apps(business),
	}


def business_for_user(user: str) -> str | None:
	"""Name of the active business this user owns."""
	return frappe.db.get_value("Business", {"owner_user": user, "status": "Active"})


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
		"CyberCheck Installed App",
		filters={"business": business, "status": "Active"},
		fields=["app_id as id", "app_version as version", "runtime", "status"],
		order_by="app_id",
	)
