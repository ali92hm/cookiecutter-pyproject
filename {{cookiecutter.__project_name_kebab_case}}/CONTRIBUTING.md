# Contributing to {{ cookiecutter.project_name }}

Thanks for taking the time to contribute!

## Before you start

-   Read the [development instructions] to get your environment set up.
-   For anything beyond a small fix, please open an issue first to discuss what you'd
    like to change. This avoids spending time on a pull request that doesn't get merged.
-   By participating in this project you agree to abide by the [Code of Conduct].

## Making a change

1.  Fork the repository and create a branch off `master`.
2.  Make your change, adding or updating tests under `tests/unit` and
    `tests/integration` and updating the relevant docs.
3.  Run `make ci` locally and make sure it passes before opening a pull request; this is
    the same check that runs in CI.
4.  Add an entry under `## [Unreleased]` in `CHANGELOG.md` describing your change.
5.  Open a pull request using the provided template.

[development instructions]: ./docs/development-instructions.md
[code of conduct]: ./CODE_OF_CONDUCT.md
