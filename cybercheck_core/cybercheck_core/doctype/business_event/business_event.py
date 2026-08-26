# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BusinessEvent(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business: DF.Link
		description: DF.Text | None
		ends_at: DF.Datetime | None
		event_name: DF.Data
		is_recurring: DF.Check
		location: DF.Link | None
		starts_at: DF.Datetime
		status: DF.Literal["Scheduled", "Cancelled", "Completed"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Business Event"
