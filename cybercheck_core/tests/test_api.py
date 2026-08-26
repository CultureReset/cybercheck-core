import frappe
from frappe.tests import IntegrationTestCase

from cybercheck_core.api import me
from cybercheck_core.cybercheck_core.doctype.cybercheck_installed_app.test_cybercheck_installed_app import (
	make_business,
	make_install,
)


class TestMeEndpoint(IntegrationTestCase):
	def tearDown(self):
		frappe.db.rollback()

	def test_me_returns_no_business_and_no_apps_when_user_owns_none(self):
		result = me()

		self.assertIsNone(result["business"])
		self.assertEqual(result["installed_apps"], [])

	def test_me_returns_the_business_owned_by_the_session_user(self):
		business = make_business()
		frappe.db.set_value("Business", business, "owner_user", frappe.session.user)

		result = me()

		self.assertEqual(result["business"]["name"], "Test Marina")
		self.assertEqual(result["business"]["slug"], "test-marina")

	def test_me_lists_only_active_installs(self):
		business = make_business()
		frappe.db.set_value("Business", business, "owner_user", frappe.session.user)
		make_install(business, "menu", status="Active")
		make_install(business, "calendar", status="Disabled")

		ids = [app["id"] for app in me()["installed_apps"]]

		self.assertEqual(ids, ["menu"])

	def test_me_does_not_leak_installs_from_another_business(self):
		mine = make_business("Mine")
		frappe.db.set_value("Business", mine, "owner_user", frappe.session.user)
		make_install(mine, "menu", status="Active")
		make_install(make_business("Theirs"), "reviews", status="Active")

		ids = [app["id"] for app in me()["installed_apps"]]

		self.assertEqual(ids, ["menu"])
