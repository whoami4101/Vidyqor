import frappe
from frappe.tests import IntegrationTestCase


class TestBatch(IntegrationTestCase):
	def tearDown(self):
		frappe.db.rollback()

	def _make_fixtures(self):
		institution = frappe.get_doc(
			{
				"doctype": "Institution",
				"institution_name": "Batch Parent Institution VQ",
			}
		).insert(ignore_permissions=True)
		department = frappe.get_doc(
			{
				"doctype": "Department",
				"department_name": "Batch Parent Department VQ",
				"institution": institution.name,
			}
		).insert(ignore_permissions=True)
		program = frappe.get_doc(
			{
				"doctype": "Program",
				"program_name": "Batch Parent Program VQ",
				"department": department.name,
			}
		).insert(ignore_permissions=True)
		academic_year = frappe.get_doc(
			{
				"doctype": "Academic Year",
				"academic_year_name": "Batch Parent AY VQ",
				"year_start_date": "2026-06-01",
				"year_end_date": "2027-05-31",
			}
		).insert(ignore_permissions=True)
		return program, academic_year

	def test_batch_create(self):
		program, academic_year = self._make_fixtures()
		doc = frappe.get_doc(
			{
				"doctype": "Batch",
				"batch_name": "Batch 2026 VQ",
				"program": program.name,
				"academic_year": academic_year.name,
				"start_year": 2026,
				"end_year": 2030,
			}
		).insert(ignore_permissions=True)
		self.assertTrue(frappe.db.exists("Batch", doc.name))

	def test_end_year_before_start_raises(self):
		program, academic_year = self._make_fixtures()
		doc = frappe.get_doc(
			{
				"doctype": "Batch",
				"batch_name": "Bad Batch VQ",
				"program": program.name,
				"academic_year": academic_year.name,
				"start_year": 2030,
				"end_year": 2026,
			}
		)
		self.assertRaises(frappe.ValidationError, doc.insert, ignore_permissions=True)
