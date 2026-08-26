# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BusinessContact(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business: DF.Link
		contact_name: DF.Data
		email: DF.Data | None
		is_primary: DF.Check
		phone: DF.Data | None
		role: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Business Contact"
