# Coding Standards

> **Project status:** foundation / scaffold only. The 18 functional modules are **Planned**.

Vidyqor follows Frappe conventions. Tooling configuration lives in `pyproject.toml` and
`.pre-commit-config.yaml`.

## Python

- **Indentation:** tabs (Frappe convention), not spaces.
- **Quotes:** double quotes.
- **Line length:** 110 characters.
- **Linting & formatting:** [Ruff](https://docs.astral.sh/ruff/).

```bash
ruff check .
ruff format --check .
```

Ruff lint rule families enabled: `F`, `E`, `W`, `I`, `UP`, `B`, `RUF` (see `pyproject.toml`
for the ignore list tuned for Frappe apps).

## JavaScript, CSS, Markdown, YAML

- Formatted with [Prettier](https://prettier.io).
- Markdown additionally checked with
  [markdownlint-cli2](https://github.com/DavidAnson/markdownlint-cli2) using
  `.markdownlint-cli2.jsonc`.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org):
`feat:`, `fix:`, `docs:`, `chore:`, `refactor:`, `test:`.

## Pre-commit

```bash
pre-commit install
pre-commit run --all-files
```

All hooks must pass before a pull request is merged.

## Documentation style

- Every doc states the current project status (foundation / scaffold).
- Describe Planned behavior as Planned; do not present it as implemented.
- Do not fabricate metrics, emails, or CI results.
