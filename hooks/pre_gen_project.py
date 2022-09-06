#!/usr/bin/env python

import re


def is_validate_python_project_name(project_name_snake_case: str) -> bool:
    MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

    if re.match(MODULE_REGEX, project_name_snake_case):
        return True

    return False


if __name__ == "__main__":
    if not is_validate_python_project_name(
        "{{ cookiecutter.project_name_snake_case }}"
    ):
        project_name = "{{ cookiecutter.project_name_snake_case }}"
        raise Exception(f"Error: {project_name} is not a valid Python module name!")
