import frappe
from frappe.tests.utils import FrappeTestCase
from frappe.utils import now_datetime


class TestInstitution(FrappeTestCase):
	def tearDown(self):
		frappe.db.rollback()

	def test_institution_create(self):
		doc = frappe.get_doc(
			{
				"doctype": "Institution",
				"institution_name": "Test Institution VQ",
				"institution_code": "TST-INST-VQ",
				"institution_type": "University",
				"established_year": 2000,
			}
		).insert(ignore_permissions=True)
		self.assertTrue(frappe.db.exists("Institution", doc.name))

	def test_future_established_year_raises(self):
		future_year = now_datetime().year + 5
		doc = frappe.get_doc(
			{
				"doctype": "Institution",
				"institution_name": "Future Institution VQ",
				"established_year": future_year,
			}
		)
		self.assertRaises(frappe.ValidationError, doc.insert, ignore_permissions=True)
