# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog] and this project adheres to
[Semantic Versioning].

## [Unreleased]

### Added

-   `.github/dependabot.yml` to keep pip and GitHub Actions dependencies up to date
-   `docs/tool-choices.md` content, and `CONTRIBUTING.md` content (both repo and template)

### Changed

-   Generated projects now use [PEP 639](https://peps.python.org/pep-0639/)
    `license`/`license-files` fields instead of the deprecated `license = {file = ...}`
    table and `License ::` classifiers; `_pypi_license_map` was renamed to
    `_spdx_license_map` in `cookiecutter.json` accordingly
-   Bumped `actions/checkout` and `actions/setup-python` to v7 in all workflows
-   Bumped the minimum supported Python version to 3.11 and added 3.14 to the CI matrix
    (repo and template)
-   `make test-unit` now reports coverage (`--cov`) in both the repo and the template
-   `tests/e2e/test_e2e.py` now installs each generated project's dependencies into its
    own throwaway virtualenv instead of the ambient test environment

### Fixed

-   The generated project's wheel no longer packages a top-level `tests` module
    (`[tool.setuptools.packages.find]` was including everything under the project root)
-   `hooks/pre_gen_project.py` now rejects Python keywords (e.g. a project named `class`)
    and accepts single-character project names, instead of using a hand-rolled regex
-   Fixed broken `docs/*.md` links in the root `README.md` (missing `.md` extension)

## [0.1.0]

### Added

-   Initial release

[keep a changelog]: https://keepachangelog.com/en/1.1.0/
[semantic versioning]: https://semver.org/spec/v2.0.0.html
[unreleased]: https://github.com/ali92hm/cookiecutter-pyproject/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ali92hm/cookiecutter-pyproject/releases/tag/v0.1.0
