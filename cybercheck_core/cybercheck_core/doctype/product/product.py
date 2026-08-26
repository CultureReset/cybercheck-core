# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Product(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business: DF.Link
		category: DF.Link | None
		description: DF.SmallText | None
		product_name: DF.Data
		sku: DF.Data | None
		status: DF.Literal["Active", "Inactive"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Product"
