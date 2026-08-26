# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BusinessRelationship(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		from_business: DF.Link
		relationship_type: DF.Literal["Parent", "Subsidiary", "Franchise", "Partner", "Vendor", "Other"]
		status: DF.Literal["Active", "Ended"]
		to_business: DF.Link
	# end: auto-generated types

	_DOCTYPE_NAME = "Business Relationship"
