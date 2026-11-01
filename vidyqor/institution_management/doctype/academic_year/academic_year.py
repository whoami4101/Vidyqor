import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate


class AcademicYear(Document):
	def validate(self):
		if self.year_start_date and self.year_end_date:
			if getdate(self.year_end_date) <= getdate(self.year_start_date):
				frappe.throw(_("Year end date must be after start date"))
