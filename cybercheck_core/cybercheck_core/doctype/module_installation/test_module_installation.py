import frappe
from frappe.tests import IntegrationTestCase

from cybercheck_core.cybercheck_core.doctype.module_installation.module_installation import (
	ModuleInstallation,
)


def make_user(email: str) -> str:
	"""A user that owns nothing, so tests do not depend on ambient data."""
	if not frappe.db.exists("User", email):
		frappe.get_doc(
			{"doctype": "User", "email": email, "first_name": email.split("@")[0]}
		).insert(ignore_permissions=True)
	return email


def make_business(name: str = "Test Marina", owner: str | None = None) -> str:
	business = frappe.get_doc({
		"doctype": "Business",
		"business_name": name,
		"slug": name.lower().replace(" ", "-"),
		"owner_user": owner,
	})
	business.insert(ignore_permissions=True)
	return business.name


def make_install(business: str, app_id: str, **kw) -> ModuleInstallation:
	values = {
		"doctype": "Module Installation",
		"business": business,
		"app_id": app_id,
		"runtime": "frappe",
	}
	values.update(kw)
	install = frappe.get_doc(values)
	install.insert(ignore_permissions=True)
	return install


class TestModuleInstallation(IntegrationTestCase):
	def setUp(self):
		self.business = make_business()

	def tearDown(self):
		frappe.db.rollback()

	def test_uppercase_app_id_is_rejected_as_invalid_manifest_id(self):
		with self.assertRaises(frappe.ValidationError) as caught:
			make_install(self.business, "SongRequests")

		self.assertIn("is not a valid manifest id", str(caught.exception))

	def test_app_id_with_underscore_is_rejected_as_invalid_manifest_id(self):
		with self.assertRaises(frappe.ValidationError) as caught:
			make_install(self.business, "song_requests")

		self.assertIn("is not a valid manifest id", str(caught.exception))

	def test_dotted_manifest_id_is_accepted(self):
		install = make_install(self.business, "browser.playwright", runtime="container")

		self.assertEqual(install.app_id, "browser.playwright")

	def test_installing_the_same_app_twice_for_one_business_is_rejected(self):
		make_install(self.business, "song-requests")

		with self.assertRaises(frappe.DuplicateEntryError):
			make_install(self.business, "song-requests")

	def test_two_businesses_may_each_install_the_same_app(self):
		other = make_business("Other Marina")

		make_install(self.business, "song-requests")
		second = make_install(other, "song-requests")

		self.assertEqual(second.business, other)

	def test_installed_by_and_installed_on_are_stamped_on_insert(self):
		install = make_install(self.business, "menu")

		self.assertEqual(install.installed_by, frappe.session.user)
		self.assertIsNotNone(install.installed_on)

	def test_grants_is_true_only_for_a_granted_permission(self):
		install = make_install(
			self.business, "menu", granted_permissions=[{"permission": "business.read"}]
		)

		self.assertTrue(install.grants("business.read"))
		self.assertFalse(install.grants("business.write"))
