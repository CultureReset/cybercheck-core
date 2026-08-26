# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Policy(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		body: DF.TextEditor | None
		business: DF.Link
		effective_from: DF.Date | None
		policy_type: DF.Literal["Cancellation", "Refund", "Privacy", "Terms", "Accessibility", "Other"]
		title: DF.Data
	# end: auto-generated types

	_DOCTYPE_NAME = "Policy"
