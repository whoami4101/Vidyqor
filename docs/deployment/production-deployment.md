# Production Deployment

> **Project status:** foundation / scaffold only. The 18 functional modules are **Planned**.
> There is no application functionality to deploy in production yet. This document describes
> the intended process.

Vidyqor deploys like any other Frappe app: as part of a Frappe Bench production setup.

## Planned deployment outline

1. **Provision a server** following the
   [Frappe production setup](https://docs.frappe.io/framework/user/en/bench/guides/setup-production).
2. **Set up bench** with a production configuration (supervisor, nginx).
3. **Create a site** for your institution.
4. **Install Vidyqor:**

   ```bash
   bench get-app https://github.com/whoami4101/Vidyqor
   bench --site your-site install-app vidyqor
   bench --site your-site migrate
   ```

5. **Build assets and restart:**

   ```bash
   bench build
   bench restart
   ```

## Current reality

Because no modules are implemented, a production install only registers the scaffold.
Wait for a tagged release before planning a production rollout — no version has been
released yet (see [CHANGELOG.md](../../CHANGELOG.md)).

## Security

Review [security/security-guidelines.md](../security/security-guidelines.md) and
[SECURITY.md](../../SECURITY.md) before any internet-facing deployment.
