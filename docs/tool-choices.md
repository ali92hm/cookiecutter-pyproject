# Tool choices and design considerations

This document explains the tools this project (and the projects it generates) is built
around, and why they were chosen.

## Packaging

-   [pyproject.toml] is used for project metadata ([PEP 621]) and build system
    requirements ([PEP 518]), instead of `setup.py`/`setup.cfg`. It's the direction the
    Python packaging ecosystem has standardized on, and keeps all tool configuration in
    one file.
-   [setuptools] is the build backend. It's the most widely supported backend and needs
    no extra configuration beyond `[tool.setuptools]` to work with the layout this
    template generates.
-   [build] is used as the PEP 517 build frontend (`python -m build`), rather than
    calling `setuptools` directly.

## Linting, formatting and typing

-   [ruff] lints and formats code. It replaces what used to be three separate tools
    (black, isort, flake8) with a single, much faster one, and it reads its
    configuration straight from `pyproject.toml` (`[tool.ruff]`), unlike flake8, which
    [still doesn't][flake8#234]. Its rule selection (`[tool.ruff.lint] select`) is
    intentionally scoped to what those three tools already checked, rather than ruff's
    broader default rule set.
-   [mypy] does static type checking. It's configured fairly strictly
    (`disallow_untyped_defs`, `disallow_any_generics`) to catch real bugs, while `tests.*`
    is exempted since test code doesn't need the same rigor.

## Testing

-   [pytest] runs the test suite; it's the de facto standard test runner and has broad
    plugin support.
-   [pytest-cov] wires `coverage.py` into pytest so `make test-unit` reports coverage.
-   This repo additionally uses [pytest-cookies] to bake the template with different
    inputs and assert the generated output, and [tomli] to parse the generated
    `pyproject.toml` in those assertions.

## CI/CD

-   GitHub Actions runs the test matrix (a `tests.yml` workflow, triggered on pushes to
    `master` and on pull requests) and cuts releases (`release.yml`, triggered by pushing
    a `v*` tag; see [development instructions] for the release process).
-   [Dependabot] keeps dependencies and GitHub Actions versions up to date.

## Project generation

-   [cookiecutter] does the actual templating. It's simple (Jinja2 templates plus a JSON
    context file), has no runtime dependency in the generated project, and is widely
    used, so most contributors will already be familiar with it.

[pyproject.toml]: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/
[pep 621]: https://peps.python.org/pep-0621/
[pep 518]: https://peps.python.org/pep-0518/
[setuptools]: https://setuptools.pypa.io/en/latest/
[build]: https://build.pypa.io/en/stable/
[ruff]: https://docs.astral.sh/ruff/
[flake8#234]: https://github.com/PyCQA/flake8/issues/234
[mypy]: https://mypy.readthedocs.io/en/stable/
[pytest]: https://docs.pytest.org/en/stable/
[pytest-cov]: https://pytest-cov.readthedocs.io/en/latest/
[pytest-cookies]: https://pytest-cookies.readthedocs.io/en/latest/
[tomli]: https://github.com/hukkin/tomli
[dependabot]: https://docs.github.com/en/code-security/dependabot
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[development instructions]: ./development-instructions.md
