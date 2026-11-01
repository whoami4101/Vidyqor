# Testing

> **Project status:** foundation / scaffold only. The 18 functional modules are **Planned**.

Vidyqor has two layers of checks: scaffold validation (runs anywhere) and Frappe tests
(require a Frappe environment).

## Scaffold validation (no Frappe required)

```bash
# Byte-compile the package
python3 -m compileall vidyqor

# Aggregate validation: compile + YAML/JSON/JSONC/TOML parsing + asset paths + git status.
# This explicitly SKIPS Frappe tests and prints a note saying so.
bash scripts/validate_scaffold.sh
```

## Frappe tests (require a Frappe environment)

Functional tests use `FrappeTestCase` and live inside the app at `vidyqor/tests/`. They can
only run inside a Frappe bench with a site:

```bash
bench --site your-site.localhost run-tests --app vidyqor
```

Currently there is a single smoke test asserting the package version. It is **not** executed
in local scaffold validation or in environments without Frappe installed.

## Continuous integration

- `.github/workflows/lint.yml` runs Ruff, Prettier, markdownlint, config validation, and
  pre-commit.
- `.github/workflows/ci.yml` spins up MariaDB + Redis, installs `frappe-bench`, creates a
  site, installs the app, and runs `bench run-tests --app vidyqor`.

> **Note:** CI has not yet run on this repository. The workflows are defined but no run has
> been triggered.

See the root [`tests/README.md`](../../tests/README.md) for where tests live.
