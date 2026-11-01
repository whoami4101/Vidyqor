import frappe
from frappe import _
from frappe.model.document import Document


class Course(Document):
	def validate(self):
		if self.credits is not None and self.credits != "" and int(self.credits) < 0:
			frappe.throw(_("Credits cannot be negative"))
