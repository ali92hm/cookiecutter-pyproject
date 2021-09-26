#!/usr/bin/env python

import re


def get_project_name_kebab_case(project_name: str) -> str:
    return project_name.lower().replace(" ", "-").replace("_", "-")


def get_project_name_snake_case(project_name: str) -> str:
    return project_name.lower().replace(" ", "_").replace("-", "_")


def is_validate_python_project_name(project_name_snake_case: str) -> bool:
    MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

    if re.match(MODULE_REGEX, project_name_snake_case):
        return True

    return False


if __name__ == "__main__":
    # TODO: Remove this block
    # project_name_snake_case and project_name_kebab_case vairables while can be set by the
    # user, they are not meant to. In later versions of cookiecutter we can add __ prefix
    # to them in order to hide them from the user.
    # In the meantime, we till throw an exception if they are different than the project name
    project_name = "{{ cookiecutter.project_name_snake_case }}"
    project_name_snake_case = "{{ cookiecutter.project_name_snake_case }}"
    project_name_kebab_case = "{{ cookiecutter.project_name_kebab_case }}"

    if get_project_name_snake_case(project_name) != project_name_snake_case:
        raise Exception(
            "Error: project_name_snake_case cannot be set. This input will be removed in the future"
        )

    if get_project_name_kebab_case(project_name) != project_name_kebab_case:
        raise Exception(
            "Error: project_name_kebab_case cannot be set. This input will be removed in the future"
        )

    # end block

    if not is_validate_python_project_name(
        "{{ cookiecutter.project_name_snake_case }}"
    ):
        project_name = "{{ cookiecutter.project_name_snake_case }}"
        raise Exception(f"Error: {project_name} is not a valid Python module name!")
