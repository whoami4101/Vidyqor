# Architecture Overview

> **Project status:** foundation / scaffold only. The 18 functional modules are **Planned**.
> This document describes the intended architecture, not shipped functionality.

Vidyqor is a single, self-contained [Frappe Framework](https://frappeframework.com) app.
It does not depend on ERPNext or other Frappe apps (`required_apps = []`).

## High-level design

Vidyqor follows the standard Frappe app architecture:

- **App package** (`vidyqor/`) — Python package registered with Frappe via `hooks.py`.
- **Modules** — 18 Planned functional areas, each a folder under the app with a
  `doctype/` subfolder (currently placeholders).
- **Support subpackages** — `config`, `api`, `services`, `utils`, `templates`, `www`.
- **Tests** — `vidyqor/tests/` using `FrappeTestCase`.

## Layered responsibilities (planned)

| Layer | Responsibility | Location |
| ----- | -------------- | -------- |
| Data model | DocTypes and their controllers | `vidyqor/<module>/doctype/` _(Planned)_ |
| Services | Reusable domain logic | `vidyqor/services/` |
| API | Whitelisted endpoints | `vidyqor/api/` |
| Utilities | Shared helpers | `vidyqor/utils/` |
| Presentation | Web templates and portal pages | `vidyqor/templates/`, `vidyqor/www/` |

## How the app sits in Frappe

```text
Frappe Bench
└── sites/<site>
    └── apps
        ├── frappe        (framework)
        └── vidyqor       (this app)
```

## Related documents

- [Application structure](application-structure.md)
- [Database design](database-design.md)
- [Permissions](permissions.md)
