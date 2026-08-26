import frappe
from frappe.tests import IntegrationTestCase

from cybercheck_core.api import me
from cybercheck_core.cybercheck_core.doctype.module_installation.test_module_installation import (
	make_business,
	make_install,
	make_user,
)


class TestMeEndpoint(IntegrationTestCase):
	def setUp(self):
		self.user = make_user("owner@cybercheck.test")
		frappe.set_user(self.user)

	def tearDown(self):
		frappe.set_user("Administrator")
		frappe.db.rollback()

	def test_me_returns_no_business_and_no_apps_when_user_owns_none(self):
		result = me()

		self.assertIsNone(result["business"])
		self.assertEqual(result["businesses"], [])
		self.assertEqual(result["installed_apps"], [])

	def test_me_returns_the_business_owned_by_the_session_user(self):
		make_business("Test Marina", owner=self.user)

		result = me()

		self.assertEqual(result["business"]["name"], "Test Marina")
		self.assertEqual(result["business"]["slug"], "test-marina")

	def test_me_lists_only_active_installs(self):
		business = make_business("Test Marina", owner=self.user)
		make_install(business, "menu", status="Active")
		make_install(business, "calendar", status="Disabled")

		ids = [app["id"] for app in me()["installed_apps"]]

		self.assertEqual(ids, ["menu"])

	def test_me_does_not_leak_installs_from_another_business(self):
		mine = make_business("Mine", owner=self.user)
		make_install(mine, "menu", status="Active")
		make_install(make_business("Theirs", owner=make_user("other@cybercheck.test")),
		             "reviews", status="Active")

		ids = [app["id"] for app in me()["installed_apps"]]

		self.assertEqual(ids, ["menu"])

	def test_me_lists_every_business_the_user_owns(self):
		make_business("First Marina", owner=self.user)
		make_business("Second Marina", owner=self.user)

		names = [b["name"] for b in me()["businesses"]]

		self.assertEqual(sorted(names), ["First Marina", "Second Marina"])

	def test_me_reports_the_requested_business_when_the_user_owns_several(self):
		make_business("First Marina", owner=self.user)
		second = make_business("Second Marina", owner=self.user)
		make_install(second, "song-requests", status="Active")

		result = me(business=second)

		self.assertEqual(result["business"]["name"], "Second Marina")
		self.assertEqual([a["id"] for a in result["installed_apps"]], ["song-requests"])

	def test_me_refuses_a_business_the_user_does_not_own(self):
		theirs = make_business("Theirs", owner=make_user("other@cybercheck.test"))

		with self.assertRaises(frappe.PermissionError) as caught:
			me(business=theirs)

		self.assertIn("do not have access", str(caught.exception))
