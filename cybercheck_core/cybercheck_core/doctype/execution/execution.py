# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Execution(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		device: DF.Link | None
		error_message: DF.SmallText | None
		executor_type: DF.Literal["browser", "android", "container", "api", "sms"]
		external_job_id: DF.Data | None
		finished_at: DF.Datetime | None
		started_at: DF.Datetime | None
		status: DF.Literal["Queued", "Running", "Succeeded", "Failed"]
		task: DF.Link
		workspace: DF.Link | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Execution"
