import frappe
from frappe.tests import IntegrationTestCase


class TestProgram(IntegrationTestCase):
	def tearDown(self):
		frappe.db.rollback()

	def test_program_create(self):
		institution = frappe.get_doc(
			{
				"doctype": "Institution",
				"institution_name": "Program Parent Institution VQ",
			}
		).insert(ignore_permissions=True)
		department = frappe.get_doc(
			{
				"doctype": "Department",
				"department_name": "Program Parent Department VQ",
				"institution": institution.name,
			}
		).insert(ignore_permissions=True)
		doc = frappe.get_doc(
			{
				"doctype": "Program",
				"program_name": "B.Tech CSE VQ",
				"program_abbreviation": "BT-CSE",
				"department": department.name,
				"duration_years": 4,
				"program_level": "Undergraduate",
			}
		).insert(ignore_permissions=True)
		self.assertTrue(frappe.db.exists("Program", doc.name))
