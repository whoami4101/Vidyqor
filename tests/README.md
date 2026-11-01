# Tests

> **Project status:** foundation / scaffold only. The 18 functional modules are **Planned**.

This root-level `tests/` directory is a pointer, not a test suite. The actual tests for the
Vidyqor app live **inside the app package** at [`../vidyqor/tests/`](../vidyqor/tests/),
following Frappe conventions.

## Why tests live inside the app

Frappe discovers and runs tests from within the installed app. Keeping tests in
`vidyqor/tests/` lets `bench run-tests --app vidyqor` find them, and keeps them packaged with
the app.

## Running the Frappe tests

Frappe tests use `FrappeTestCase` and **require a Frappe environment** (a bench with a site):

```bash
bench --site your-site.localhost run-tests --app vidyqor
```

These tests are **not** executed by the local scaffold validation, and they cannot run
without Frappe installed.

## Scaffold validation (no Frappe required)

To validate the repository structure, configuration parsing, and asset paths without a
Frappe runtime:

```bash
bash scripts/validate_scaffold.sh
```

This script explicitly **skips** the Frappe tests and prints a note saying so.
