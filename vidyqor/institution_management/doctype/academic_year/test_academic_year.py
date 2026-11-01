import frappe
from frappe.tests import IntegrationTestCase


class TestAcademicYear(IntegrationTestCase):
	def tearDown(self):
		frappe.db.rollback()

	def test_academic_year_create(self):
		doc = frappe.get_doc(
			{
				"doctype": "Academic Year",
				"academic_year_name": "2026-2027 VQ",
				"year_start_date": "2026-06-01",
				"year_end_date": "2027-05-31",
			}
		).insert(ignore_permissions=True)
		self.assertTrue(frappe.db.exists("Academic Year", doc.name))

	def test_end_before_start_raises(self):
		doc = frappe.get_doc(
			{
				"doctype": "Academic Year",
				"academic_year_name": "Bad Year VQ",
				"year_start_date": "2027-06-01",
				"year_end_date": "2026-05-31",
			}
		)
		self.assertRaises(frappe.ValidationError, doc.insert, ignore_permissions=True)
