# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BusinessMedia(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business: DF.Link
		caption: DF.Data | None
		file_url: DF.Data | None
		media_type: DF.Literal["Image", "Video", "Document", "Audio"]
		reference_doctype: DF.Link | None
		reference_name: DF.DynamicLink | None
		sort_order: DF.Int
	# end: auto-generated types

	_DOCTYPE_NAME = "Business Media"
