# Quick Start

> **Project status:** foundation / scaffold only. The 18 functional modules are **Planned**.
> There is no application UI or feature to try yet. This guide shows how to obtain the
> scaffold and validate it.

## Prerequisites

- A working [Frappe Bench](https://docs.frappe.io/framework/user/en/installation) environment
  (Python 3.10+, Node.js, MariaDB, Redis) to install the app.
- Alternatively, just Python 3.10+ to byte-compile and validate the scaffold locally.

## Option A — install into a Frappe bench

```bash
bench get-app https://github.com/whoami4101/Vidyqor
bench --site your-site.localhost install-app vidyqor
```

Because no modules are implemented yet, installing the app only registers the scaffold.

## Option B — validate the scaffold locally (no Frappe)

```bash
git clone https://github.com/whoami4101/Vidyqor
cd Vidyqor

# Byte-compile the package (proves importable syntax)
python3 -m compileall vidyqor

# Run the aggregate scaffold validation (Frappe tests are skipped)
bash scripts/validate_scaffold.sh
```

## Where to go next

- [Installation requirements](../installation/requirements.md)
- [Full installation guide](../installation/installation.md)
- [Architecture overview](../architecture/overview.md)
