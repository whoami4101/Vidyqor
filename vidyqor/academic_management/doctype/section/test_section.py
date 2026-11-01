import frappe
from frappe.tests.utils import FrappeTestCase


class TestSection(FrappeTestCase):
	def tearDown(self):
		frappe.db.rollback()

	def _make_batch(self):
		institution = frappe.get_doc(
			{
				"doctype": "Institution",
				"institution_name": "Section Parent Institution VQ",
			}
		).insert(ignore_permissions=True)
		department = frappe.get_doc(
			{
				"doctype": "Department",
				"department_name": "Section Parent Department VQ",
				"institution": institution.name,
			}
		).insert(ignore_permissions=True)
		program = frappe.get_doc(
			{
				"doctype": "Program",
				"program_name": "Section Parent Program VQ",
				"department": department.name,
			}
		).insert(ignore_permissions=True)
		academic_year = frappe.get_doc(
			{
				"doctype": "Academic Year",
				"academic_year_name": "Section Parent AY VQ",
				"year_start_date": "2026-06-01",
				"year_end_date": "2027-05-31",
			}
		).insert(ignore_permissions=True)
		return frappe.get_doc(
			{
				"doctype": "Batch",
				"batch_name": "Section Parent Batch VQ",
				"program": program.name,
				"academic_year": academic_year.name,
			}
		).insert(ignore_permissions=True)

	def test_section_create(self):
		batch = self._make_batch()
		doc = frappe.get_doc(
			{
				"doctype": "Section",
				"section_name": "A",
				"batch": batch.name,
				"capacity": 40,
			}
		).insert(ignore_permissions=True)
		self.assertTrue(frappe.db.exists("Section", doc.name))

	def test_zero_capacity_raises(self):
		batch = self._make_batch()
		doc = frappe.get_doc(
			{
				"doctype": "Section",
				"section_name": "B",
				"batch": batch.name,
				"capacity": 0,
			}
		)
		self.assertRaises(frappe.ValidationError, doc.insert, ignore_permissions=True)
