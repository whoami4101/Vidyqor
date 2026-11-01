"""Documentation source configuration for the Vidyqor app.

These values point the Frappe docs tooling at the project's documentation. They
are placeholders for the foundation scaffold and can be refined as the hosted
docs site comes online.
"""

source_link = "https://github.com/whoami4101/Vidyqor"
docs_base_url = "https://github.com/whoami4101/Vidyqor/tree/main/docs"
headline = "Open Source Education ERP"
sub_heading = "One Platform. Every Institution."


def get_context(context):
	context.brand_html = "Vidyqor"
