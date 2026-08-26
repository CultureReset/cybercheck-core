# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Approval(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		approver: DF.Link | None
		decided_at: DF.Datetime | None
		decision: DF.Literal["Pending", "Approved", "Rejected"]
		note: DF.SmallText | None
		task: DF.Link
	# end: auto-generated types

	_DOCTYPE_NAME = "Approval"
