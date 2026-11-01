app_name = "vidyqor"
app_title = "Vidyqor"
app_publisher = "Vidyqor Community"
app_description = "Open Source Education ERP — One Platform. Every Institution."
app_license = "mit"

# Security / contact: this app does not advertise an email address. Report issues and
# vulnerabilities via GitHub private vulnerability reporting (Security Advisories) and the
# repository Issues / Discussions. See SECURITY.md.

# Apps that must be installed before this app. Intentionally empty: Vidyqor is an
# independent Frappe app and must NOT require ERPNext / Education / HRMS / CRM.
required_apps = []

# ------------------------------------------------------------------------------
# The block below is the standard Frappe hook scaffolding. Everything is commented
# out for the foundation scaffold; uncomment and populate as features are built.
# ------------------------------------------------------------------------------

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vidyqor/css/vidyqor.css"
# app_include_js = "/assets/vidyqor/js/vidyqor.js"

# include js, css files in header of web template
# web_include_css = "/assets/vidyqor/css/vidyqor.css"
# web_include_js = "/assets/vidyqor/js/vidyqor.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "vidyqor/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# -----

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "vidyqor.utils.jinja_methods",
# 	"filters": "vidyqor.utils.jinja_filters",
# }

# Installation
# ------------

# before_install = "vidyqor.install.before_install"
# after_install = "vidyqor.install.after_install"

# Uninstallation
# --------------

# before_uninstall = "vidyqor.uninstall.before_uninstall"
# after_uninstall = "vidyqor.uninstall.after_uninstall"

# Integration Setup
# ------------------

# before_app_install = "vidyqor.utils.before_app_install"
# after_app_install = "vidyqor.utils.after_app_install"

# before_app_uninstall = "vidyqor.utils.before_app_uninstall"
# after_app_uninstall = "vidyqor.utils.after_app_uninstall"

# Desk Notifications
# ------------------

# notification_config = "vidyqor.notifications.get_notification_config"

# Permissions
# -----------

# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# -------------

# override standard doctype classes
# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------

# Hook on document methods and events
# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method",
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"vidyqor.tasks.all"
# 	],
# 	"daily": [
# 		"vidyqor.tasks.daily"
# 	],
# 	"hourly": [
# 		"vidyqor.tasks.hourly"
# 	],
# 	"weekly": [
# 		"vidyqor.tasks.weekly"
# 	],
# 	"monthly": [
# 		"vidyqor.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "vidyqor.install.before_tests"

# Overriding Methods
# ------------------------------

# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "vidyqor.event.get_events"
# }

# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "vidyqor.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["vidyqor.utils.before_request"]
# after_request = ["vidyqor.utils.after_request"]

# Job Events
# ----------
# before_job = ["vidyqor.utils.before_job"]
# after_job = ["vidyqor.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"vidyqor.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# translated_search_doctypes = []
