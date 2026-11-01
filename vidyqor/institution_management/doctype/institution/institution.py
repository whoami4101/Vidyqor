import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import now_datetime


class Institution(Document):
	def validate(self):
		if self.established_year and int(self.established_year) > now_datetime().year:
			frappe.throw(_("Established year cannot be in the future"))
