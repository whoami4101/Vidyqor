import frappe
from frappe.tests import IntegrationTestCase


class TestDepartment(IntegrationTestCase):
	def tearDown(self):
		frappe.db.rollback()

	def test_department_create(self):
		institution = frappe.get_doc(
			{
				"doctype": "Institution",
				"institution_name": "Department Parent Institution VQ",
			}
		).insert(ignore_permissions=True)
		doc = frappe.get_doc(
			{
				"doctype": "Department",
				"department_name": "Computer Science VQ",
				"department_code": "CS-VQ",
				"institution": institution.name,
				"head_of_department": "Dr. Test",
			}
		).insert(ignore_permissions=True)
		self.assertTrue(frappe.db.exists("Department", doc.name))
