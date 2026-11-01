# Introduction

> **Project status:** Vidyqor is at the **foundation / scaffold** stage. The repository
> structure, build configuration, and documentation exist, but the 18 functional modules
> are **Planned** and not yet implemented. Nothing in this document describes shipped
> functionality.

Vidyqor is an open source **Education ERP** built on the
[Frappe Framework](https://frappeframework.com). Its goal is to provide a single platform
that institutions — schools, colleges, universities, and training centers — can use to run
administration end to end.

**Tagline:** _One Platform. Every Institution._

## What exists today

- A Frappe app package (`vidyqor/`) with the standard layout and 18 Planned module folders.
- Build configuration (`pyproject.toml` with the flit_core backend), tooling, and CI/lint/release workflows.
- Documentation (these files) describing the intended design.

## What does not exist yet

- Any DocTypes, business logic, UI, or workflows.
- Any released build. No version has been tagged or published.
- Any CI run. The workflows are defined but have not executed on this repository.

## The planned modules

All 18 modules are **Planned**. See
[modules/module-overview.md](../modules/module-overview.md) for the full list and short
descriptions.

## Next steps

- New to the project? Read the [Quick Start](quick-start.md).
- Want to set up a dev environment? See
  [development/development-environment.md](../development/development-environment.md).
- Curious about the design? Start with
  [architecture/overview.md](../architecture/overview.md).
