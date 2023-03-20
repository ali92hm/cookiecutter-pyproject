#!/usr/bin/env python

import re

import upgrade_utils


def get_project_name_kebab_case(project_name: str) -> str:
    return project_name.lower().replace(" ", "-").replace("_", "-")


def get_project_name_snake_case(project_name: str) -> str:
    return project_name.lower().replace(" ", "_").replace("-", "_")


def is_validate_python_project_name(project_name_snake_case: str) -> bool:
    MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

    return True if re.match(MODULE_REGEX, project_name_snake_case) else False


if __name__ == "__main__":
    project_name = "{{ cookiecutter.__project_name_snake_case }}"
    if not is_validate_python_project_name(project_name):
        raise Exception(f"Error: {project_name} is not a valid Python module name!")

    current_version = "{{ cookiecutter._template_version }}"
    if not upgrade_utils.is_upgradable(current_version):
        raise Exception(
            f"Error: Cannot upgrade from {current_version} to {upgrade_utils.get_latest_version()}"
        )
