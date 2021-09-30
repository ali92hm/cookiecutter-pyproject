# {{ cookiecutter.project_name }}

![CI Tests] ![black badge]

{{ cookiecutter.project_description }}

## First time setup

If you just generated a new project follow the instructions in [first time setup]
to complete the manual steps required to set up a new project.

Read the [development instructions] to get started with development

## Getting started

<!-- Add me -->

### System requirements

-   [python] >= 3.7 (comes with pip)

<!-- Add me -->

## Resources and documentation

-   [Development instructions]
-   [Project structure]

## Issues or questions

If you encounter any problems or have any question, please [file an issue].

## Contributing

We welcome contributions to this project. Please refer to the [CONTRIBUTING] to get started.

## Code of Conduct

Everyone interacting in this project's codebases, issue trackers,
chat rooms, and mailing lists is expected to follow the [CODE_OF_CONDUCT]

{% if cookiecutter.license != 'Not open source' -%}

## License

[{{ cookiecutter.license }}]

[![OSI certified][osi_certified]][{{ cookiecutter.license }}]

{%- endif %}

[ci tests]: {{ cookiecutter.project_repo }}/actions/workflows/tests.yml/badge.svg
[black badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[file an issue]: {{ cookiecutter.project_repo }}/issues
[contributing]: ./CONTRIBUTING.md
[code_of_conduct]: ./CODE_OF_CONDUCT.md
[development instructions]: ./docs/development-instructions
[first time setup]: ./docs/first-time-setup
[project structure]: ./docs/project-structure
[MIT License]: http://opensource.org/licenses/MIT
[BSD 2-Clause License]: https://opensource.org/licenses/BSD-2-Clause
[BSD 3-Clause License]: https://opensource.org/licenses/BSD-3-Clause
[ISC License]: https://opensource.org/licenses/ISC
[Apache License Version 2.0]: https://opensource.org/licenses/Apache-2.0
[GNU General Public License Version 3]: https://opensource.org/licenses/GPL-3.0
[Unlicense]: https://opensource.org/licenses/unlicense
[osi_certified]: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
[python]: https://www.python.org/downloads/
