# Project structure

```
cookiecutter-pyproject
.
├── .editorconfig - Universal editor configuration
├── .gitignore - Gitignore file
├── CHANGELOG.md - CHANGELOG file containing the changes to the project
├── CODE_OF_CONDUCT.md - CODE_OF_CONDUCT file for interacting with this repo
├── CONTRIBUTING.md - Instructions for contributing to this project
├── pyproject.toml - Contains the metadata for this python project as well as configuration for some of the tools
├── requirements.txt - List of external python libraries that this project depends on
├── VERSION - The current version of this project, read dynamically by pyproject.toml
├── LICENSE - License file for this repo
├── Makefile - Makefile containing the common commands for the project
├── README.md - README file
├── .generated - Contains the generated (baked) projects created during tests, safe to delete
├── .reports - Contains the result of test runs in JUnit format, safe to delete
├── .github - Folder containing github settings and files
│ ├── ISSUE_TEMPLATE - Contains issue templates for bug report and questions
│ ├── workflows - Github Actions workflows
│ │ ├── tests.yml - Runs style checks, type checks and tests on push/PR
│ │ └── release.yml - Cuts a GitHub release when a v* tag is pushed
│ ├── dependabot.yml - Keeps pip and GitHub Actions dependencies up to date
│ └── PULL_REQUEST_TEMPLATE.md - Pull request template
├── .vscode - Folder containing VSCode settings
│ ├── extensions.json - Suggested VSCode extensions for this project
│ └── settings.json - VSCode settings for the project
├── cookiecutter.json - Defines the cookiecutter variables for this template
├── {{cookiecutter.__project_name_kebab_case}} - The Jinja2-templated project tree that gets rendered on generation
│ ├── {{cookiecutter.__project_name_snake_case}} - The generated project's source package
│ ├── tests - Unit and integration tests for the generated project
│ ├── scripts - Utility bash files for the generated project
│ └── ... - pyproject.toml, Makefile, README.md, LICENSE, etc. for the generated project
├── hooks - Cookiecutter hooks
│ ├── pre_gen_project.py - Runs before generation; validates the project name is a legal Python identifier
│ └── post_gen_project.py - Runs after generation; removes LICENSE if "Not open source" and runs git init
├── docs - Documents for the project
│ ├── development-instructions.md - Instructions for setting up the development environment to work on this project
│ ├── tool-choices.md - A description of the tools used in this project
│ └── project-structure.md - Structure of the project and an explanation of the files and folders
├── tests - Tests that bake the template and assert the generated output is correct
│ ├── e2e - Bakes the template, then runs make init/ci/build/clean inside the generated project
│ ├── integration - Bakes the template with various inputs and asserts the generated files/content
│ └── unit - Unit tests for the helper functions in hooks/pre_gen_project.py
└── scripts - Contains utility bash files for building, testing, releasing and cleaning this repo
  ├── check-style.sh - Runs ruff check and ruff format --check
  ├── fix-style.sh - Applies ruff check --fix and ruff format
  ├── test-unit.sh - Runs the unit test suite
  ├── test-integration.sh - Runs the integration test suite
  ├── test-e2e.sh - Runs the end to end test suite
  ├── generate.sh - Bakes the template into .generated/manual for manual inspection
  ├── check-version.sh - Asserts a given tag matches the VERSION file (used by the release workflow)
  ├── release-tag.sh - Creates the v<version> release tag for the current VERSION
  └── clean.sh - Removes generated files and folders
```
