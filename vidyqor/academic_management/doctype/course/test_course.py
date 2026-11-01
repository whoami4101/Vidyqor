import frappe
from frappe.tests import IntegrationTestCase


class TestCourse(IntegrationTestCase):
	def tearDown(self):
		frappe.db.rollback()

	def _make_program(self):
		institution = frappe.get_doc(
			{
				"doctype": "Institution",
				"institution_name": "Course Parent Institution VQ",
			}
		).insert(ignore_permissions=True)
		department = frappe.get_doc(
			{
				"doctype": "Department",
				"department_name": "Course Parent Department VQ",
				"institution": institution.name,
			}
		).insert(ignore_permissions=True)
		return frappe.get_doc(
			{
				"doctype": "Program",
				"program_name": "Course Parent Program VQ",
				"department": department.name,
			}
		).insert(ignore_permissions=True)

	def test_course_create(self):
		program = self._make_program()
		doc = frappe.get_doc(
			{
				"doctype": "Course",
				"course_name": "Data Structures VQ",
				"course_code": "CS201-VQ",
				"program": program.name,
				"credits": 3,
				"course_type": "Core",
			}
		).insert(ignore_permissions=True)
		self.assertTrue(frappe.db.exists("Course", doc.name))

	def test_negative_credits_raises(self):
		program = self._make_program()
		doc = frappe.get_doc(
			{
				"doctype": "Course",
				"course_name": "Bad Course VQ",
				"course_code": "BAD-VQ",
				"program": program.name,
				"credits": -1,
			}
		)
		self.assertRaises(frappe.ValidationError, doc.insert, ignore_permissions=True)
