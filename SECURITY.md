# Security Policy

## Project status

Vidyqor is at the **foundation / scaffold** stage. The repository currently contains
the project structure, build configuration, and documentation. The 18 functional
modules are **Planned** and not yet implemented, so there is no running application
surface to attack yet. Even so, we take security seriously and welcome responsible
disclosure.

## Supported versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: (foundation / scaffold) |

Only the `0.1.x` foundation line exists. There are no released builds yet.

## Reporting a vulnerability

**Please do not report security vulnerabilities through public GitHub issues,
discussions, or pull requests.**

Instead, use GitHub's **private vulnerability reporting**:

1. Go to the [Security tab](https://github.com/whoami4101/Vidyqor/security) of the
   repository.
2. Choose **Report a vulnerability** to open a private advisory.
3. Provide a description of the issue, the affected area, reproduction steps, and the
   potential impact.

Private vulnerability reporting keeps the report confidential between you and the
maintainers until a fix is available. We do not publish a dedicated security email
address; GitHub Security Advisories are the single reporting channel.

If you are unsure whether something is a vulnerability, you may open a
[GitHub Discussion](https://github.com/whoami4101/Vidyqor/discussions) to ask without
disclosing sensitive details.

## What to expect

- We will acknowledge your report as soon as we are able to review it.
- We will investigate and keep you informed of progress through the private advisory.
- Once a fix is ready, we will coordinate disclosure and credit you if you wish.

## Scope

Because the application modules are not yet implemented, reports are most useful when
they concern the repository supply chain: CI/CD workflow configuration, dependency
pinning, build backend configuration, or the documented installation process.
