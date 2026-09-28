# Development instructions

This document will walk you though setting up this project for development.

## Setup

You can work on this project with only python3 installed, but it is strongly recommended to use some virtual environment tool. It's useful to have a clean environment for your development and it helps to prevent polluting the global python environment on your system.

Some virtual environment tools:

- [venv] ships with python > 3.3
- [pew] Python Env Wrapper
- [virtualenv]
- [pyenv-virtualenv]
- [pipenv]

After creating a virtual environment and **activating** it, you can run `make init` to install all the project dependencies that are needed for development.

## Commands

There are several useful commands in the `Makefile`, here is how to use them:

- `make init` installs the `dev` dependency group from `pyproject.toml` (needs
  pip >= 25.1, for [PEP 735] `--group` support)
- `make clean` removes all the generated files and folders
- `make check-style` runs the linter and will print all the linting errors
- `make fix-style` attempts to fix all the fixable linting and style errors
- `make check-types` runs the mypy static code analysis
- `make test-unit` runs the unit test suite
- `make test-integration` runs the integration test suite
- `make test` runs all of the test suites (unit and integration)
- `make build` builds the python wheel distribution
- `make ci` runs the all style checks and tests (used by CI)
- `make link` installs this project in the users python environment (for testing)
- `make check-version TAG=v1.2.3` checks that a tag matches `__version__` (used by CI)
- `make release-tag` creates the release tag for the current `__version__`

Any of the `test-*` targets accept extra pytest arguments through `ARGS`, for example
`make test-unit ARGS="-k test_add -v"`.

## Releasing

Releases are cut by pushing a version tag, so that you decide when a set of merged changes becomes a release.

To cut a release:

1.  Bump `__version__` in `{{ cookiecutter.__project_name_snake_case }}/__init__.py`
    following [semantic versioning].
2.  Move the entries under `## [Unreleased]` in `CHANGELOG.md` into a new section for
    the version you are releasing.
3.  Open a pull request with those changes and merge it once CI is green.
4.  Check out the merge commit on `master` and run `make release-tag`. This creates an
    annotated `v<version>` tag and prints the command to push it.
5.  Push the tag. The `Release` workflow then verifies that the tag matches
    `__version__`, runs the test suite,{% if cookiecutter.license != 'Not open source' %} publishes the package to PyPI,{% endif %}
    and creates a GitHub release with the build artifacts attached.

If the tag and `__version__` disagree, the release workflow fails before it publishes
anything.
{% if cookiecutter.license != 'Not open source' %}
A version that has been published to PyPI can never be replaced, only yanked, so prefer
bumping to a new version over retrying a failed release.
{% endif %}
[semantic versioning]: https://semver.org/spec/v2.0.0.html

[virtualenv]: https://virtualenv.pypa.io/en/latest/user_guide.html
[pew]: https://github.com/berdario/pew
[pipenv]: https://pipenv.pypa.io/en/latest/
[pyenv-virtualenv]: https://github.com/pyenv/pyenv-virtualenv
[venv]: https://docs.python.org/3/library/venv.html
[pep 735]: https://peps.python.org/pep-0735/
