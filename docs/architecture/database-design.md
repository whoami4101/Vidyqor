# Database Design

> **Project status:** foundation / scaffold only. **No DocTypes or tables exist yet.**
> The 18 functional modules are **Planned**, so this document describes intent only.

## Data model approach

Vidyqor will use Frappe's DocType system. Each DocType maps to a database table managed by
Frappe's ORM. The planned modules will own their DocTypes under
`vidyqor/<module>/doctype/`.

## Current state

- `vidyqor/<module>/doctype/` folders contain only `__init__.py` placeholders.
- No DocType JSON definitions exist.
- No migrations or patches are defined (`patches.txt` has a header only).

## Planned conventions

When DocTypes are added, they will follow Frappe norms:

- One folder per DocType under the owning module's `doctype/` directory.
- A DocType JSON definition plus a Python controller class.
- Links and child tables modeled with Frappe `Link` and `Table` field types.
- Naming series and permissions declared in the DocType definition.

## Entity relationships (planned, illustrative)

A likely high-level relationship set once modules land:

```text
Institution 1───* Department 1───* Faculty
Institution 1───* Program 1───* Course
Student *───* Course (via Enrollment)
Student 1───* FeeInvoice
```

This diagram is illustrative of intent and is **not** implemented.
