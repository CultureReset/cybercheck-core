# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ExternalIdentifier(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business: DF.Link
		external_id: DF.Data
		source: DF.Link
		url: DF.Data | None
		verified: DF.Check
	# end: auto-generated types

	_DOCTYPE_NAME = "External Identifier"
