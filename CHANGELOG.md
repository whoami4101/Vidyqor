# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Continued implementation of the remaining functional modules (currently **Planned**):
  Student, Admission, Faculty, Attendance, Examination, Finance & Fee, Library, Hostel,
  Transport, Placement, Human Resource, Communication, Document, Reports & Analytics,
  and System Configuration.

## [0.2.0] - Unreleased

> Phase 2: first functional DocTypes. **Institution Management** and **Academic
> Management** are now **In Development** — schema, validation, and passing tests are
> present, but no UI, dashboards, portals, or workflows yet. **Department Management**
> has a single minimal supporting DocType. The other 15 modules remain Planned. This
> version has not been tagged or published.

### Added

- Institution Management DocTypes: Institution, Campus, Building, Classroom,
  Academic Year — with field schemas, `validate()` rules (future established-year guard,
  classroom capacity > 0, academic-year end-after-start), and IntegrationTestCase tests.
- Academic Management DocTypes: Program, Course, Semester, Batch, Section — with field
  schemas, `validate()` rules (course credits ≥ 0, semester end-after-start, batch
  end-year ≥ start-year, section capacity > 0), and IntegrationTestCase tests.
- Department Management: minimal Department DocType (supporting Institution/Academic
  Management; full module still Planned).
- Bumped `__version__` to `0.2.0`.

## [0.1.0] - Unreleased

> Foundation / scaffold release. No functional application modules are implemented
> yet; this entry records the project foundation only. This version has not been
> tagged or published.

### Added

- Frappe app Python package layout (`vidyqor/`) with `hooks.py`, `modules.txt`,
  `patches.txt`, and `__version__ = "0.1.0"`.
- Support subpackages: `config`, `api`, `services`, `utils`, `templates`, `www`,
  and `tests` (with a `FrappeTestCase` smoke test that requires a Frappe environment
  to run).
- 18 Planned module folders, each with a `doctype/` placeholder (no DocTypes yet).
- Build configuration via `pyproject.toml` (flit_core backend, dynamic version,
  Ruff settings) and `MANIFEST.in`.
- Repository dotfiles: `.gitignore`, `.editorconfig`, `.gitattributes`,
  `.pre-commit-config.yaml`, `.markdownlint-cli2.jsonc`.
- Governance and meta documents: `LICENSE` (MIT), `CODE_OF_CONDUCT.md`,
  `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, this `CHANGELOG.md`.
- GitHub automation: issue forms, PR template, funding/dependabot config, and
  CI, lint, and release workflows.
- Documentation tree under `docs/` describing the foundation and the planned modules.
- Helper script `scripts/validate_scaffold.sh` and a project logo asset.

[Unreleased]: https://github.com/whoami4101/Vidyqor/compare/main...HEAD
[0.2.0]: https://github.com/whoami4101/Vidyqor/compare/v0.1.0...main
[0.1.0]: https://github.com/whoami4101/Vidyqor/releases/tag/v0.1.0
