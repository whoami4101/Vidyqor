# Security Guidelines

> **Project status:** foundation / scaffold only. The 18 functional modules are **Planned**.
> There is no running application surface yet. These are forward-looking guidelines.

## Reporting vulnerabilities

Do not open public issues for security reports. Use GitHub's
[private vulnerability reporting](https://github.com/whoami4101/Vidyqor/security). See the
full policy in [SECURITY.md](../../SECURITY.md).

## Current attack surface

At the scaffold stage the relevant surface is the **supply chain**:

- CI/CD workflow configuration (`.github/workflows/`).
- Dependency pinning (`pyproject.toml`, `.pre-commit-config.yaml`, `dependabot.yml`).
- The documented installation process.

Dependabot is configured for `github-actions` and `pip` to keep dependencies current.

## Planned application-level guidance

When modules are implemented, contributors should:

- Rely on Frappe's role-based permission system; declare permissions per DocType.
- Validate and sanitize all user input; never build SQL by string concatenation — use
  Frappe's query builder and parameterized queries.
- Avoid logging secrets or personally identifiable information.
- Keep `required_apps` empty and avoid pulling in unvetted dependencies.
- Use Frappe's CSRF protection and whitelisting for API endpoints.

## Secrets and configuration

Never commit secrets. Site configuration (`sites/`) is excluded by `.gitignore`. Use
environment-specific site config for credentials.
