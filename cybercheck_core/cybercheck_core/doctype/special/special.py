# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Special(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business: DF.Link
		days_of_week: DF.Data | None
		description: DF.SmallText | None
		discount_type: DF.Literal["", "Percent", "Amount", "Other"]
		discount_value: DF.Float
		ends_at: DF.Datetime | None
		special_name: DF.Data
		starts_at: DF.Datetime | None
		status: DF.Literal["Active", "Expired", "Draft"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Special"
