import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate


class Semester(Document):
	def validate(self):
		if self.start_date and self.end_date:
			if getdate(self.end_date) <= getdate(self.start_date):
				frappe.throw(_("End date must be after start date"))
