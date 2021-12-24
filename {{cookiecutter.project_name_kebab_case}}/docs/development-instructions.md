# Development instructions

This document will walk you though setting up this project for development.

## Setup

You can work on this project with only python3 installed, but it is strongly recommended to use some virtual environment tool. It's useful to have a clean environment for your development and it helps to prevent polluting the global python environment on your system.

Some virtual environment tools:

-   [venv] ships with python > 3.3
-   [pew] Python Env Wrapper
-   [virtualenv]
-   [pyenv-virtualenv]
-   [pipenv]

After creating a virtual environment and **activating** it, you can run `make init` to install all the project dependencies that are needed for development.

## Commands

There are several useful commands in the `Makefile`, here is how to use them:

-   `make init` installs all the dependencies in the `requirements.txt`
-   `make clean` removes all the generated files and folders
-   `make check-style` runs the linter and will print all the linting errors
-   `make fix-style` attempts to fix all the fixable linting and style errors
-   `make check-types` runs the mypy static code analysis
-   `make test-unit` runs the unit test suite
-   `make test-integration` runs the integration test suite
-   `make test` runs all of the test suites (unit and integration)
-   `make build` builds the python wheel distribution
-   `make release` pushes the build artifact to PyPi (used by CI)
-   `make ci` runs the all style checks and tests (used by CI)
-   `make link` installs this project in the users python environment (for testing)

[virtualenv]: https://virtualenv.pypa.io/en/latest/user_guide.html
[pew]: https://github.com/berdario/pew
[pipenv]: https://pipenv.pypa.io/en/latest/
[pyenv-virtualenv]: https://github.com/pyenv/pyenv-virtualenv
[venv]: https://docs.python.org/3/library/venv.html
