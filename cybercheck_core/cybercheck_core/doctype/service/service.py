# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Service(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business: DF.Link
		category: DF.Link | None
		description: DF.SmallText | None
		duration_minutes: DF.Int
		service_name: DF.Data
		status: DF.Literal["Active", "Inactive"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Service"
