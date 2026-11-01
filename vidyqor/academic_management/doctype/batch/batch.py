import frappe
from frappe import _
from frappe.model.document import Document


class Batch(Document):
	def validate(self):
		if self.start_year and self.end_year and int(self.end_year) < int(self.start_year):
			frappe.throw(_("End year must be greater than or equal to start year"))
