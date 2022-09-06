#!/usr/bin/env python

import re


def get_project_name_kebab_case(project_name: str) -> str:
    return project_name.lower().replace(" ", "-").replace("_", "-")


def get_project_name_snake_case(project_name: str) -> str:
    return project_name.lower().replace(" ", "_").replace("-", "_")


def is_validate_python_project_name(project_name_snake_case: str) -> bool:
    MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

    return True if re.match(MODULE_REGEX, project_name_snake_case) else False


if __name__ == "__main__":
    if not is_validate_python_project_name(
        "{{ cookiecutter.__project_name_snake_case }}"
    ):
        project_name = "{{ cookiecutter.__project_name_snake_case }}"
        raise Exception(f"Error: {project_name} is not a valid Python module name!")
