# Copyright (c) 2026, CultureReset and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PrivateWorkspace(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		business: DF.Link
		external_reference: DF.Data | None
		secret_reference: DF.Data | None
		status: DF.Literal["Provisioning", "Active", "Stopped", "Error"]
		workspace_name: DF.Data
		workspace_type: DF.Literal["Browser", "Android", "Container"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Private Workspace"
