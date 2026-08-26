# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BusinessLocation(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address_line_1: DF.Data | None
		address_line_2: DF.Data | None
		business: DF.Link
		city: DF.Data | None
		country: DF.Link | None
		email: DF.Data | None
		is_primary: DF.Check
		latitude: DF.Float
		location_name: DF.Data
		longitude: DF.Float
		phone: DF.Data | None
		postal_code: DF.Data | None
		state: DF.Data | None
		status: DF.Literal["Active", "Temporarily Closed", "Closed"]
		timezone: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Business Location"
