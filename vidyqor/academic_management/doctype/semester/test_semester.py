import frappe
from frappe.tests.utils import FrappeTestCase


class TestSemester(FrappeTestCase):
	def tearDown(self):
		frappe.db.rollback()

	def _make_academic_year(self):
		return frappe.get_doc(
			{
				"doctype": "Academic Year",
				"academic_year_name": "Semester Parent AY VQ",
				"year_start_date": "2026-06-01",
				"year_end_date": "2027-05-31",
			}
		).insert(ignore_permissions=True)

	def test_semester_create(self):
		academic_year = self._make_academic_year()
		doc = frappe.get_doc(
			{
				"doctype": "Semester",
				"semester_name": "Semester 1 VQ",
				"academic_year": academic_year.name,
				"semester_number": 1,
				"start_date": "2026-06-01",
				"end_date": "2026-11-30",
			}
		).insert(ignore_permissions=True)
		self.assertTrue(frappe.db.exists("Semester", doc.name))

	def test_end_before_start_raises(self):
		academic_year = self._make_academic_year()
		doc = frappe.get_doc(
			{
				"doctype": "Semester",
				"semester_name": "Bad Semester VQ",
				"academic_year": academic_year.name,
				"start_date": "2026-11-30",
				"end_date": "2026-06-01",
			}
		)
		self.assertRaises(frappe.ValidationError, doc.insert, ignore_permissions=True)
