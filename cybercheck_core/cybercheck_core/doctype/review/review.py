# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Review(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		author_name: DF.Data | None
		body: DF.Text | None
		business: DF.Link
		external_id: DF.Data | None
		location: DF.Link | None
		rating: DF.Float
		reviewed_at: DF.Datetime | None
		source: DF.Link | None
		status: DF.Literal["New", "Responded", "Flagged"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Review"
