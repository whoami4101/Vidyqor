"""Smoke test for the Vidyqor app foundation.

This test uses Frappe's ``FrappeTestCase`` and therefore requires a running
Frappe environment to EXECUTE (``bench --site <site> run-tests --app vidyqor``).
It is intentionally trivial — it only asserts the packaged version string. The
module still byte-compiles without Frappe installed, since ``compileall`` parses
source without importing it.
"""

from frappe.tests.utils import FrappeTestCase

import vidyqor


class TestSmoke(FrappeTestCase):
	def test_version(self):
		self.assertEqual(vidyqor.__version__, "0.1.0")
