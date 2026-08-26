# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Task(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business: DF.Link
		module_installation: DF.Link | None
		payload_reference: DF.Data | None
		priority: DF.Literal["Low", "Normal", "High"]
		requested_by: DF.Link | None
		scheduled_for: DF.Datetime | None
		status: DF.Literal["Pending", "Awaiting Approval", "Approved", "Running", "Succeeded", "Failed", "Cancelled"]
		task_type: DF.Data
	# end: auto-generated types

	_DOCTYPE_NAME = "Task"
