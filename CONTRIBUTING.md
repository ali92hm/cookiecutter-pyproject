# Contributing to Cookiecutter-PyProject

Thanks for taking the time to contribute!

## Before you start

-   Read the [development instructions] to get your environment set up.
-   For anything beyond a small fix, please open an issue first to discuss what you'd
    like to change. This avoids spending time on a pull request that doesn't get merged.
-   By participating in this project you agree to abide by the [Code of Conduct].

## Making a change

1.  Fork the repository and create a branch off `master`.
2.  Make your change. If you're fixing a bug or adding a feature, add or update tests
    under `tests/` (or, if the change affects the generated project, under
    `{{cookiecutter.__project_name_kebab_case}}/tests/`) and update the relevant docs.
3.  Run `make ci` locally and make sure it passes before opening a pull request; this is
    the same check that runs in CI.
4.  Add an entry under `## [Unreleased]` in `CHANGELOG.md` describing your change.
5.  Open a pull request using the provided template.

## Reporting bugs and requesting features

Please use the issue templates in `.github/ISSUE_TEMPLATE` to file a bug report, feature
request, or question.

[development instructions]: ./docs/development-instructions.md
[code of conduct]: ./CODE_OF_CONDUCT.md
