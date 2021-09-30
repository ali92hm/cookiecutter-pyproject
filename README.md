# Cookiecutter PyProject

![CI Tests] ![black badge]

A [cookiecutter] for generating a ~semi-opinionated~ scaffolding for python projects as well as python packages.

## Features

-   Complete structure for a python project
-   Ready for publishing to [PyPI]
-   Full Github integration (github actions, issue template, pr templates etc)
-   Code linter using [flake8], [isort], and [black]
-   Code formatting using [isort] and [black]
-   [Pytest] integration for testing
-   Type checking using [mypy]
-   Using the `pyproject.toml` for most tool configuration,
    project metadata according to [pep 621], and minimum build system requirements according to [pep 518]
-   More goodies coming soon

## Getting started

### System requirements

-   [python] >= 3.6 (comes with pip)
-   [cookiecutter] >= 1.7.3

### Generating your first project

In order to generate your first project run:

```
cookiecutter https://github.com/ali92hm/cookiecutter-pyproject
```

Cookiecutter will prompt you for the following inputs:

Please ignore `project_name_snake_case` and `project_name_kebab_case` variables and leave them as default. These variable will be removed once cookiecutter supports private templated variables

```no-highlight
project_name [Sample project]: The name for your project (Please don't use special characters, space is file)
project_name_snake_case []: Just press enter
project_name_kebab_case []: Just press enter
project_description [Generated sample project from cookiecutter-pyproject]: Short description of your project
author_full_name [Jane Doe]: Your full name
author_email [jane.doe@example.com]: Your email address
github_organization [janeDoe]: The name of the github organization this code will be hosted. You can use your own github organization
project_repo []: This is the url to your repository, you can change it if you want
license:
1 - MIT License
2 - BSD 2-Clause License
3 - BSD 3-Clause License
4 - ISC License
5 - Apache License Version 2.0
6 - GNU General Public License Version 3
7 - Unlicense
8 - "Not open source"
Choose from 1, 2, 3, 4, 5, 6, 7 8 [1]: Pick the license you want to use
```

## Resources and documentation

-   [Development instructions]
-   [Tool choices and design considerations]
-   [Project structure]

## Issues or questions

If you encounter any problems or have any question, please [file an issue].

## Contributing

We welcome contributions to this project. Please refer to the [CONTRIBUTING] to get started.

## Code of Conduct

Everyone interacting in this project's codebases, issue trackers,
chat rooms, and mailing lists is expected to follow the [CODE_OF_CONDUCT]

## License

[MIT License]

[![OSI certified][osi_certified]][mit license]

[ci tests]: https://github.com/ali92hm/cookiecutter-pyproject/actions/workflows/tests.yml/badge.svg
[black badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[cookiecutter]: https://github.com/cookiecutter/cookiecutter
[file an issue]: https://github.com/ali92hm/cookiecutter-pyproject/issues
[contributing]: ./CONTRIBUTING.md
[development instructions]: ./docs/development-instructions
[tool choices and design considerations]: ./docs/tool-choices
[project structure]: ./docs/project-structure
[code_of_conduct]: ./CODE_OF_CONDUCT.md
[mit license]: http://opensource.org/licenses/MIT
[osi_certified]: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
[python]: https://www.python.org/downloads/
[pypi]: https://pypi.org/
[isort]: https://pycqa.github.io/isort/
[black]: https://black.readthedocs.io/en/stable/
[flake8]: https://flake8.pycqa.org/en/latest/
[mypy]: https://mypy.readthedocs.io/en/stable/
[pytest]: https://docs.pytest.org/en/6.2.x/
[pep 518]: https://www.python.org/dev/peps/pep-0518/
[pep 621]: https://www.python.org/dev/peps/pep-0621/
