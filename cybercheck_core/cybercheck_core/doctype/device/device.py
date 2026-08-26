# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Device(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business: DF.Link
		device_name: DF.Data
		device_type: DF.Literal["Android", "Browser", "Container"]
		external_reference: DF.Data | None
		last_seen_at: DF.Datetime | None
		status: DF.Literal["Provisioning", "Online", "Offline", "Error"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Device"
