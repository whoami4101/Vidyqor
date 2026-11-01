import frappe
from frappe import _
from frappe.model.document import Document


class Classroom(Document):
	def validate(self):
		if self.capacity is not None and self.capacity != "" and int(self.capacity) <= 0:
			frappe.throw(_("Capacity must be greater than 0"))
