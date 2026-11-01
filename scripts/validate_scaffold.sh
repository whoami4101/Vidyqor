#!/usr/bin/env bash
#
# validate_scaffold.sh — aggregate validation for the Vidyqor foundation scaffold.
#
# What it does (none of which requires a Frappe runtime):
#   1. Byte-compiles the vidyqor package (python3 -m compileall).
#   2. Parses every .yml / .yaml file with yaml.safe_load.
#   3. Parses every .json file with json.load, and .markdownlint-cli2.jsonc as JSONC.
#   4. Parses pyproject.toml with tomllib.
#   5. Verifies every local asset path referenced in README.md and docs/ exists.
#   6. Explicitly SKIPS Frappe tests (no Frappe environment — Option B) and says so.
#   7. Ends with `git status` (it never runs git add / commit / push).
#
# Exit code is 0 only when every check above passes.

set -uo pipefail

# Resolve the repository root (this script lives in scripts/).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

STATUS=0

pass() { printf '  [PASS] %s\n' "$1"; }
fail() { printf '  [FAIL] %s\n' "$1"; STATUS=1; }
section() { printf '\n==> %s\n' "$1"; }

PYTHON="$(command -v python3 || true)"
if [ -z "${PYTHON}" ]; then
	echo "python3 is required but was not found on PATH." >&2
	exit 1
fi

# ----------------------------------------------------------------------------
section "1. Byte-compiling the vidyqor package"
if "${PYTHON}" -m compileall -q vidyqor >/dev/null 2>&1; then
	pass "python3 -m compileall vidyqor"
else
	fail "python3 -m compileall vidyqor"
fi
# Clean up byte-compile artifacts so the working tree stays tidy.
find vidyqor -name '__pycache__' -type d -prune -exec rm -rf '{}' + 2>/dev/null || true

# ----------------------------------------------------------------------------
section "2. Parsing YAML files"
if "${PYTHON}" - <<'PY'
import glob
import sys

try:
	import yaml
except ImportError:
	print("    (PyYAML not installed — skipping YAML parse checks)")
	sys.exit(0)

files = sorted(set(glob.glob("**/*.yml", recursive=True) + glob.glob("**/*.yaml", recursive=True)))
failed = []
for f in files:
	if f.startswith(".git/"):
		continue
	try:
		with open(f, encoding="utf-8") as fh:
			list(yaml.safe_load_all(fh))
	except Exception as exc:  # noqa: BLE001
		failed.append(f"{f}: {exc}")

for f in files:
	print(f"    parsed {f}")
if failed:
	for item in failed:
		print(f"    ERROR {item}")
	sys.exit(1)
sys.exit(0)
PY
then
	pass "all YAML files parse"
else
	fail "YAML parsing"
fi

# ----------------------------------------------------------------------------
section "3. Parsing JSON and JSONC files"
if "${PYTHON}" - <<'PY'
import glob
import json
import re
import sys

failed = []

# Plain JSON files (exclude the JSONC file and vendored/VCS dirs).
for f in sorted(glob.glob("**/*.json", recursive=True)):
	if f.startswith((".git/", "node_modules/")):
		continue
	try:
		with open(f, encoding="utf-8") as fh:
			json.load(fh)
		print(f"    parsed {f}")
	except Exception as exc:  # noqa: BLE001
		failed.append(f"{f}: {exc}")

# JSONC: strip /* */ and // comments before json.loads.
jsonc = ".markdownlint-cli2.jsonc"
try:
	with open(jsonc, encoding="utf-8") as fh:
		s = fh.read()
	s = re.sub(r"/\*.*?\*/", "", s, flags=re.S)
	s = re.sub(r"(?m)//.*$", "", s)
	json.loads(s)
	print(f"    parsed {jsonc} (JSONC)")
except FileNotFoundError:
	failed.append(f"{jsonc}: file missing")
except Exception as exc:  # noqa: BLE001
	failed.append(f"{jsonc}: {exc}")

if failed:
	for item in failed:
		print(f"    ERROR {item}")
	sys.exit(1)
sys.exit(0)
PY
then
	pass "all JSON / JSONC files parse"
else
	fail "JSON / JSONC parsing"
fi

# ----------------------------------------------------------------------------
section "4. Parsing pyproject.toml"
if "${PYTHON}" - <<'PY'
import sys

try:
	import tomllib
except ModuleNotFoundError:
	try:
		import tomli as tomllib  # type: ignore
	except ModuleNotFoundError:
		print("    (no tomllib/tomli available — skipping TOML parse)")
		sys.exit(0)

with open("pyproject.toml", "rb") as fh:
	data = tomllib.load(fh)
assert data["project"]["name"] == "vidyqor", data["project"].get("name")
assert data["tool"]["flit"]["module"]["name"] == "vidyqor"
print("    parsed pyproject.toml (name=vidyqor, flit module=vidyqor)")
PY
then
	pass "pyproject.toml parses"
else
	fail "pyproject.toml parsing"
fi

# ----------------------------------------------------------------------------
section "5. Verifying referenced local asset paths exist"
if "${PYTHON}" - <<'PY'
import glob
import os
import re
import sys

# Collect README.md and all docs markdown.
sources = ["README.md"] + sorted(glob.glob("docs/**/*.md", recursive=True))
# Markdown image/link syntax: (path.ext) ; and HTML src="path.ext".
md_re = re.compile(r"\(([^)]+\.(?:svg|png|jpe?g|gif))\)")
html_re = re.compile(r"""src\s*=\s*["']([^"']+\.(?:svg|png|jpe?g|gif))["']""")
missing = []
checked = 0

for src in sources:
	if not os.path.exists(src):
		continue
	base = os.path.dirname(src)
	with open(src, encoding="utf-8") as fh:
		text = fh.read()
	refs = [m.group(1).strip() for m in md_re.finditer(text)]
	refs += [m.group(1).strip() for m in html_re.finditer(text)]
	for ref in refs:
		if ref.startswith(("http://", "https://", "#", "mailto:", "data:")):
			continue
		# Resolve relative to the file that references it.
		path = os.path.normpath(os.path.join(base, ref))
		checked += 1
		if os.path.exists(path):
			print(f"    ok  {src} -> {ref}")
		else:
			missing.append(f"{src} -> {ref} (resolved {path})")

if checked == 0:
	print("    (no local image assets referenced)")
if missing:
	for m in missing:
		print(f"    MISSING {m}")
	sys.exit(1)
sys.exit(0)
PY
then
	pass "all referenced local assets exist"
else
	fail "referenced local asset paths"
fi

# ----------------------------------------------------------------------------
section "6. Frappe tests"
echo "    SKIPPED: Frappe tests are NOT executed by this script."
echo "    No Frappe environment is assumed (Option B). Run them inside a bench with:"
echo "        bench --site <site> run-tests --app vidyqor"

# ----------------------------------------------------------------------------
section "Result"
if [ "${STATUS}" -eq 0 ]; then
	echo "  Scaffold validation PASSED (Frappe tests skipped)."
else
	echo "  Scaffold validation FAILED — see [FAIL] lines above."
fi

# ----------------------------------------------------------------------------
section "git status (no git add / commit / push is performed)"
git status

exit "${STATUS}"
