import frappe
from frappe.tests.utils import FrappeTestCase


class TestBuilding(FrappeTestCase):
	def tearDown(self):
		frappe.db.rollback()

	def test_building_create(self):
		institution = frappe.get_doc(
			{
				"doctype": "Institution",
				"institution_name": "Building Parent Institution VQ",
			}
		).insert(ignore_permissions=True)
		campus = frappe.get_doc(
			{
				"doctype": "Campus",
				"campus_name": "Building Parent Campus VQ",
				"institution": institution.name,
			}
		).insert(ignore_permissions=True)
		doc = frappe.get_doc(
			{
				"doctype": "Building",
				"building_name": "Science Block VQ",
				"campus": campus.name,
				"building_code": "BLD-VQ-1",
				"number_of_floors": 4,
			}
		).insert(ignore_permissions=True)
		self.assertTrue(frappe.db.exists("Building", doc.name))
