# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SourceRecord(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		confidence: DF.Float
		external_id: DF.Data | None
		fetched_at: DF.Datetime | None
		payload_reference: DF.Data | None
		reference_doctype: DF.Link | None
		reference_name: DF.DynamicLink | None
		source: DF.Link
	# end: auto-generated types

	_DOCTYPE_NAME = "Source Record"
