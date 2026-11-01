# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Implementation of the 18 functional modules (all currently **Planned**):
  Institution, Student, Admission, Academic, Department, Faculty, Attendance,
  Examination, Finance & Fee, Library, Hostel, Transport, Placement, Human Resource,
  Communication, Document, Reports & Analytics, and System Configuration.

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
[0.1.0]: https://github.com/whoami4101/Vidyqor/releases/tag/v0.1.0
