# Application Structure

> **Project status:** foundation / scaffold only. The 18 functional modules are **Planned**.
> The structure below exists today, but the module folders are placeholders.

## Repository layout

```text
Vidyqor/
├── vidyqor/                 # the Frappe app package
│   ├── __init__.py          # __version__ = "0.1.0"
│   ├── hooks.py             # app metadata + commented hook scaffolding
│   ├── modules.txt          # 18 Title Case module names
│   ├── patches.txt          # header only, no patches yet
│   ├── config/              # desktop.py, docs.py
│   ├── api/                 # whitelisted endpoints (stub)
│   ├── services/            # domain logic (stub)
│   ├── utils/               # shared helpers (stub)
│   ├── templates/           # Jinja templates (stub)
│   ├── www/                 # portal pages (.gitkeep)
│   ├── public/              # static assets, incl. images/vidyqor-logo.svg
│   ├── tests/               # FrappeTestCase smoke test
│   └── <18 module folders>/ # each with doctype/ placeholder (Planned)
├── docs/                    # this documentation tree
├── scripts/                 # validate_scaffold.sh
├── tests/                   # root-level pointer to vidyqor/tests/
├── .github/                 # issue forms, templates, workflows
├── pyproject.toml           # flit_core build config + Ruff
└── MANIFEST.in
```

## The 18 Planned module folders

Each module folder uses `snake_case` and currently contains only `__init__.py` and a
`doctype/__init__.py` placeholder. No DocTypes are defined.

See [modules/module-overview.md](../modules/module-overview.md) for the full list.

## Version source

`__version__` lives in `vidyqor/__init__.py` and is read dynamically by the flit_core build
backend (`[tool.flit.module]` + `[project] dynamic = ["version"]` in `pyproject.toml`).
