# CLAUDE.md

## What this is

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) template that scaffolds new
Python projects. There is no library code to speak of — the deliverable is the *template*,
and the repo's own test suite exists to prove the template bakes correctly.

## Two parallel trees (the main thing to internalize)

```
.                                            <- the template repo itself
├── cookiecutter.json                        <- template variables
├── hooks/                                   <- pre/post generation hooks (the only real Python)
├── tests/{unit,integration,e2e}/            <- tests for the template
├── pyproject.toml, Makefile, scripts/, ...  <- tooling for THIS repo
└── {{cookiecutter.__project_name_kebab_case}}/   <- the template output, Jinja2-rendered
    ├── {{cookiecutter.__project_name_snake_case}}/   <- generated source package
    ├── tests/{unit,integration}/
    └── pyproject.toml, Makefile, scripts/, ...   <- tooling for GENERATED projects
```

Most files exist twice: once for this repo, once inside the template. They are **separate
files that must be kept in sync by hand**. When changing tooling, dependency pins, the
supported Python versions, CI actions, or docs, decide deliberately whether the change
belongs in the outer repo, the template, or both — usually both.

Known intentional divergences: the template's `Makefile` has `release`/`link` targets and no
`test-e2e`; the template's `requirements.txt` adds `pytest-mock`/`twine`/`wheel` and drops
`cookiecutter`/`pytest-cookies`/`tomli`; the template's `pyproject.toml` has
`[project.scripts]` and coverage config.

## Shell gotcha

The template directory name contains braces. Always quote it:

```bash
cat '{{cookiecutter.__project_name_kebab_case}}/pyproject.toml'
```

## Files in the template are Jinja2, not valid Python/TOML

Everything under `{{cookiecutter.__project_name_kebab_case}}/` is a Jinja2 template —
`{{ cookiecutter.x }}`, `{% if %}`, `{% now 'local', '%Y' %}`. This is why every linter in
the root `pyproject.toml` excludes that directory (ruff, mypy).
Consequence: **the template's own Python is never linted or type-checked in place.** It is
only validated by baking it — `make test-integration` (structure/content assertions) and
`make test-e2e` (runs the generated project's full `make ci`). Don't "fix" a template file
to satisfy a linter; verify by baking.

`LICENSE` in the template is one file holding all license texts behind `{% if %}` branches,
selected by the `license` variable.

## Commands

```bash
make init              # pip install -r requirements.txt
make check-style       # ruff check + ruff format --check
make fix-style         # ruff check --fix + ruff format
make check-types       # mypy .
make test-unit         # tests/unit
make test-integration  # tests/integration (bakes the template in-process)
make test-e2e          # bakes, then runs make init/ci/build/clean inside — slow, pip installs
make test              # all three
make ci                # check-style + check-types + test   <- what CI runs
make build             # python -m build
make generate          # interactive cookiecutter into .generated/manual/ for eyeballing output
make clean             # removes .generated, .reports, caches, dist, build
```

Baked projects land in `.generated/` (pytest `--basetemp=.generated --keep-baked-projects`),
JUnit XML in `.reports/`. Both are disposable; `make clean` removes them.

For a quick loop, prefer `make test-integration` over `make test-e2e`. Reach for e2e only
when the change could break the generated project's own tooling.

## Hooks

- `hooks/pre_gen_project.py` — rejects a `project_name` whose snake_case form isn't a legal
  Python identifier. Also holds `get_project_name_kebab_case` / `get_project_name_snake_case`,
  which the tests import directly to derive expectations.
- `hooks/post_gen_project.py` — deletes `LICENSE` when license is `Not open source`, then
  runs `git init` in the generated project (so `.git` is expected in a baked tree).

`hooks/` is the only package shipped by this repo's own wheel
(`[tool.setuptools.packages.find] include = ["hooks*"]`).

## Adding or renaming a cookiecutter variable

1. Add it to `cookiecutter.json`. Names prefixed `__` are computed/derived; `_` are private
   (e.g. `_spdx_license_map`, which maps a license choice to its SPDX identifier for the
   `license` field in the generated `pyproject.toml`).
2. Use it in the template tree.
3. Update `tests/integration/test_generator.py`:
   `run_generated_project_assertions` reads defaults straight from `cookiecutter.json`,
   accepts per-variable `kwargs` overrides, and asserts the context value. There is a
   deliberate tripwire — `assert len(generated_project.context) == 10` — that fails when the
   variable count changes, forcing tests to be updated. Bump it, don't delete it.

## Conventions

- Style: ruff (`[tool.ruff]`), one tool for lint + format + import sort. Formatter wraps
  at 88 (`line-length`); the linter's line-too-long check tolerates up to 120
  (`[tool.ruff.lint.pycodestyle] max-line-length`) for things like long URLs that
  can't be wrapped. `E203` is ignored (a known false positive against the formatter).
- mypy is strict-ish (`disallow_untyped_defs`, `disallow_any_generics`) but ignores `tests.*`.
- Version lives in `VERSION` (dynamic via setuptools) for this repo; generated projects use
  `__version__` in their package `__init__.py`.
- Dependencies are pinned exactly (`==`) in both `requirements.txt` files.
- Supported Python: >= 3.11; CI matrix is 3.11–3.14 across ubuntu/macOS/windows.
- Default branch is `master`.
