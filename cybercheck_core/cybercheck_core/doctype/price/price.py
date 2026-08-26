# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Price(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amount: DF.Currency
		business: DF.Link
		currency: DF.Link | None
		price_label: DF.Data | None
		reference_doctype: DF.Link | None
		reference_name: DF.DynamicLink | None
		unit: DF.Data | None
		valid_from: DF.Date | None
		valid_until: DF.Date | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Price"
