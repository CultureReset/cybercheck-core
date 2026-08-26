# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ExecutionProof(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		captured_at: DF.Datetime | None
		checksum: DF.Data | None
		execution: DF.Link
		proof_type: DF.Literal["Screenshot", "Video", "DOM Snapshot", "API Response", "Log"]
		storage_reference: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Execution Proof"
