# Requirements

> **Project status:** foundation / scaffold only. The 18 functional modules are **Planned**.
> These requirements describe what is needed to install and work on the scaffold.

Vidyqor is a Frappe app, so its requirements follow the
[Frappe Framework requirements](https://docs.frappe.io/framework/user/en/installation).

## Runtime

| Component | Version | Notes |
| --------- | ------- | ----- |
| Python    | 3.10+   | `requires-python = ">=3.10"` in `pyproject.toml` |
| Node.js   | 18+     | Required by Frappe for asset building |
| MariaDB   | 10.6+   | Primary database (Frappe also supports PostgreSQL) |
| Redis     | 6+      | Cache, queue, and socketio |
| Frappe    | v15 recommended | The framework the app runs on |

`required_apps` is empty: Vidyqor does **not** depend on ERPNext, Education, HRMS, or CRM.

## Development-only (no Frappe runtime)

To byte-compile and validate the scaffold you only need:

- Python 3.10+ (the standard library includes `tomllib` on 3.11+).
- Optionally PyYAML for the YAML parsing checks in `scripts/validate_scaffold.sh`.

## Next

Continue to the [installation guide](installation.md).
