import frappe
from frappe.tests import IntegrationTestCase


class TestCampus(IntegrationTestCase):
	def tearDown(self):
		frappe.db.rollback()

	def _make_institution(self):
		return frappe.get_doc(
			{
				"doctype": "Institution",
				"institution_name": "Campus Parent Institution VQ",
			}
		).insert(ignore_permissions=True)

	def test_campus_create(self):
		institution = self._make_institution()
		doc = frappe.get_doc(
			{
				"doctype": "Campus",
				"campus_name": "Main Campus VQ",
				"institution": institution.name,
				"campus_code": "CMP-VQ-1",
				"is_main_campus": 1,
			}
		).insert(ignore_permissions=True)
		self.assertTrue(frappe.db.exists("Campus", doc.name))
