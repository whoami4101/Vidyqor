import frappe
from frappe.tests.utils import FrappeTestCase


class TestClassroom(FrappeTestCase):
	def tearDown(self):
		frappe.db.rollback()

	def _make_building(self):
		institution = frappe.get_doc(
			{
				"doctype": "Institution",
				"institution_name": "Classroom Parent Institution VQ",
			}
		).insert(ignore_permissions=True)
		campus = frappe.get_doc(
			{
				"doctype": "Campus",
				"campus_name": "Classroom Parent Campus VQ",
				"institution": institution.name,
			}
		).insert(ignore_permissions=True)
		return frappe.get_doc(
			{
				"doctype": "Building",
				"building_name": "Classroom Parent Building VQ",
				"campus": campus.name,
			}
		).insert(ignore_permissions=True)

	def test_classroom_create(self):
		building = self._make_building()
		doc = frappe.get_doc(
			{
				"doctype": "Classroom",
				"room_name": "Room 101 VQ",
				"building": building.name,
				"capacity": 30,
				"room_type": "Lecture Hall",
			}
		).insert(ignore_permissions=True)
		self.assertTrue(frappe.db.exists("Classroom", doc.name))

	def test_zero_capacity_raises(self):
		building = self._make_building()
		doc = frappe.get_doc(
			{
				"doctype": "Classroom",
				"room_name": "Bad Room VQ",
				"building": building.name,
				"capacity": 0,
			}
		)
		self.assertRaises(frappe.ValidationError, doc.insert, ignore_permissions=True)
