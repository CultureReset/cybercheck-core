# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BusinessHours(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business: DF.Link
		closes_at: DF.Time | None
		day_of_week: DF.Literal["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
		hours_type: DF.Literal["Regular", "Holiday", "Seasonal"]
		is_closed: DF.Check
		location: DF.Link | None
		opens_at: DF.Time | None
		valid_from: DF.Date | None
		valid_until: DF.Date | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Business Hours"
