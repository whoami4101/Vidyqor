# Contributing to Vidyqor

Thanks for your interest in contributing. Vidyqor is an open source Education ERP
built on the [Frappe Framework](https://frappeframework.com). The project is at the
**foundation / scaffold** stage: the repository structure, build configuration, and
documentation exist, while the 18 functional modules are **Planned**. Contributions
that help build out the foundation, documentation, and tooling are especially welcome.

By participating you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Ways to contribute

- Improve documentation under [`docs/`](docs/).
- Refine the scaffold, tooling, and CI/lint/release workflows.
- Discuss and design the Planned modules in
  [GitHub Discussions](https://github.com/whoami4101/Vidyqor/discussions).
- Report bugs or request features using the issue forms.

## Development setup

Vidyqor is a Frappe app. You need a working [Frappe Bench](https://docs.frappe.io/framework/user/en/installation)
environment (Python 3.10+, Node.js, MariaDB, Redis).

```bash
# Inside an existing bench
bench get-app https://github.com/whoami4101/Vidyqor
bench --site your-site.localhost install-app vidyqor
```

For Python-only checks that do not need a Frappe runtime:

```bash
# Byte-compile the package (proves importable syntax, no Frappe required)
python3 -m compileall vidyqor

# Run the aggregate scaffold validation (Frappe tests are skipped here)
bash scripts/validate_scaffold.sh
```

## Code style and quality

We use [Ruff](https://docs.astral.sh/ruff/) for linting and formatting, and
[Prettier](https://prettier.io) for JS/CSS/Markdown/YAML. Configuration lives in
`pyproject.toml` and `.pre-commit-config.yaml`.

```bash
pip install pre-commit
pre-commit install          # run hooks on every commit
pre-commit run --all-files  # run all hooks once
```

Key conventions (match the existing code):

- Python uses **tab** indentation (Frappe convention) and double quotes.
- Line length is 110 characters.
- Keep changes focused; do not refactor unrelated code.

## Testing

Functional tests use `FrappeTestCase` and live inside the app at `vidyqor/tests/`.
They require a Frappe environment to run:

```bash
bench run-tests --app vidyqor
```

The scaffold's `scripts/validate_scaffold.sh` validates structure, config parsing,
and asset paths, but **does not** run Frappe tests (no Frappe runtime is assumed).
See [`tests/README.md`](tests/README.md) for details.

## Pull request flow

1. Fork the repository and create a feature branch from `main`.
2. Make your change, keeping commits focused. Use
   [Conventional Commits](https://www.conventionalcommits.org) messages
   (e.g. `feat:`, `fix:`, `docs:`, `chore:`, `refactor:`).
3. Run `pre-commit run --all-files` and ensure it passes.
4. Open a pull request using the PR template. Describe what changed and how you
   verified it. Link any related issues.
5. A maintainer will review. CI (lint, and the Frappe server test) must pass before
   merge. Note: CI has not yet run on this repository.

## License

By contributing, you agree that your contributions will be licensed under the
[MIT License](LICENSE).
