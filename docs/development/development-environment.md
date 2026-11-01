# Development Environment

> **Project status:** foundation / scaffold only. The 18 functional modules are **Planned**.

## Full Frappe development setup

To develop app functionality you need a Frappe Bench. Follow the
[official installation guide](https://docs.frappe.io/framework/user/en/installation), then:

```bash
# Inside your bench directory
bench get-app https://github.com/whoami4101/Vidyqor
bench --site your-site.localhost install-app vidyqor

# Start the dev server
bench start
```

## Lightweight setup (no Frappe)

For documentation, tooling, and scaffold work you only need Python 3.10+:

```bash
git clone https://github.com/whoami4101/Vidyqor
cd Vidyqor

# Byte-compile the package
python3 -m compileall vidyqor

# Validate the scaffold (Frappe tests are skipped)
bash scripts/validate_scaffold.sh
```

## Pre-commit hooks

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

Hooks run Ruff (lint + format), Prettier, and basic file checks. See
[coding-standards.md](coding-standards.md).

## Next

- [Coding standards](coding-standards.md)
- [Testing](testing.md)
