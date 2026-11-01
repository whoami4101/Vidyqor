# Permissions

> **Project status:** foundation / scaffold only. The 18 functional modules are **Planned**.
> No roles, permission rules, or DocTypes exist yet. This document describes intent.

Vidyqor will rely on Frappe's built-in role-based permission system. Permissions are declared
per DocType and enforced by the framework.

## Planned permission model

- **Roles** — role definitions such as Administrator, Faculty, Student, Accountant, and
  Librarian will be introduced alongside the modules that need them. _(Planned.)_
- **Role permissions** — read/write/create/delete/submit rights set per DocType.
- **User permissions** — scope records to a specific institution, department, or program.
- **Field-level permissions** — hide or protect sensitive fields by role.
- **Document-level sharing** — Frappe's share mechanism for ad hoc access.

## Current state

No roles or permission rules are defined. Installing the scaffold adds no custom roles.

## Guidance for contributors

When implementing a module, declare permissions in the DocType definition and document any
custom role in the module's documentation. Avoid granting broad `System Manager` rights for
day-to-day operations.
