import re

import frappe
from frappe.model.document import Document

APP_ID_PATTERN = re.compile(r"^[a-z0-9]+([.-][a-z0-9]+)*$")


class CyberCheckInstalledApp(Document):
	def validate(self):
		self.validate_app_id()

	def validate_app_id(self):
		"""Registry manifest ids are lowercase, dot or hyphen separated."""
		if not APP_ID_PATTERN.match(self.app_id or ""):
			frappe.throw(
				f"App ID {self.app_id!r} is not a valid manifest id. "
				"Use lowercase words separated by . or -, such as browser.playwright."
			)

	def before_insert(self):
		self.installed_by = self.installed_by or frappe.session.user
		self.installed_on = self.installed_on or frappe.utils.now_datetime()

	def grants(self, permission: str) -> bool:
		"""Whether this install was granted a capability."""
		return any(row.permission == permission for row in self.granted_permissions)
