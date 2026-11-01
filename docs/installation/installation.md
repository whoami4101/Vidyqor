# Installation

> **Project status:** foundation / scaffold only. Installing the app registers the scaffold;
> the 18 functional modules are **Planned** and provide no functionality yet.

## Install into a Frappe bench

Make sure you have a working [Frappe Bench](https://docs.frappe.io/framework/user/en/installation)
and a site.

```bash
# 1. Fetch the app into your bench
bench get-app https://github.com/whoami4101/Vidyqor

# 2. Install it onto a site (replace SITE_NAME with your site)
bench --site SITE_NAME install-app vidyqor
```

To install a specific branch:

```bash
bench get-app --branch main https://github.com/whoami4101/Vidyqor
```

## Verify the installation

```bash
bench --site SITE_NAME list-apps
# vidyqor should appear in the list
```

## Uninstall

```bash
bench --site SITE_NAME uninstall-app vidyqor
```

## Validate the scaffold without Frappe

If you only want to check out the repository structure:

```bash
python3 -m compileall vidyqor
bash scripts/validate_scaffold.sh
```

## Next

See [configuration/institution-setup.md](../configuration/institution-setup.md) for the
intended post-install configuration (Planned).
