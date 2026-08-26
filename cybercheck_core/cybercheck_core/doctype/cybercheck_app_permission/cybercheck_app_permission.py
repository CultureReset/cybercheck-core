# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class CyberCheckAppPermission(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		permission: DF.Data
	# end: auto-generated types

	_DOCTYPE_NAME = "CyberCheck App Permission"
