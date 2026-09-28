# Project structure

```
{{cookiecutter.__project_name_kebab_case}}
.
├── .editorconfig - Universal editor configuration
├── .gitignore - Gitignore file
├── CHANGELOG.md - CHANGELOG file containing the changes to the project
├── CODE_OF_CONDUCT.md - CODE_OF_CONDUCT file for interacting with this repo
├── CONTRIBUTING.md - Instructions for contributing to this project
├── pyproject.toml - Contains the metadata for this python project as well as configuration for some of the tools
├── requirements.txt - List of external python libraries that this project depends on
├── LICENSE - License file (only for open source projects)
├── Makefile - Makefile containing the common commands for the project
├── README.md - README file
├── .reports - Contains the result of test runs in JUnit format, safe to delete
├── .github - Folder containing github settings and files
│ ├── ISSUE_TEMPLATE - Contains issue templates for bug report and questions
│ ├── workflows - Github Actions workflows
│ │ ├── tests.yml - Runs style checks, type checks and tests on push/PR
│ │ └── release.yml - Cuts a release when a v* tag is pushed
│ └── PULL_REQUEST_TEMPLATE.md - Pull request template
├── .vscode - Folder containing VSCode settings
│ ├── extensions.json - Suggested VSCode extensions for this project
│ └── settings.json - VSCode settings for the project
├── {{cookiecutter.__project_name_snake_case}} - The folder containing the source code for the project
│ ├── cli - The submodule for the client code
│ ├── __init__.py - The __init__ file for the parent project, holds __version__
│ ├── __main__.py - The __main__ file for the parent project
│ └── {{cookiecutter.__project_name_snake_case}}.py - The dummy generated file
├── docs - Documents for the project
│ ├── development-instructions.md - Instructions for setting up the development environment to work on this project
│ ├── first-time-setup.md - Instructions for a completing the setup of a newly created project
│ └── project-structure.md - Structure of the project and an explanation of the files and folders
├── tests - Contains the tests for the project
│ ├── integration - Contains the integration test files and data
│ └── unit - Contains the unit test files for the project
└── scripts - Contains utility bash files for checking, testing and releasing the project
  ├── check-style.sh - Runs ruff check and ruff format --check
  ├── fix-style.sh - Applies ruff check --fix and ruff format
  ├── test-unit.sh - Runs the unit test suite
  ├── test-integration.sh - Runs the integration test suite
  ├── check-version.sh - Asserts a given tag matches __version__ (used by the release workflow)
  ├── release-tag.sh - Creates the v<version> release tag for the current __version__
  └── clean.sh - Removes generated files and folders
```
