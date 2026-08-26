# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Business(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business_name: DF.Data
		owner_user: DF.Link | None
		slug: DF.Data | None
		status: DF.Literal["Active", "Suspended"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Business"
