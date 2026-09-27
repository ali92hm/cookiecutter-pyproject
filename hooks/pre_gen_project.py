#!/usr/bin/env python

import keyword


def get_project_name_kebab_case(project_name: str) -> str:
    return project_name.lower().replace(" ", "-").replace("_", "-")


def get_project_name_snake_case(project_name: str) -> str:
    return project_name.lower().replace(" ", "_").replace("-", "_")


def is_validate_python_project_name(project_name_snake_case: str) -> bool:
    return project_name_snake_case.isidentifier() and not keyword.iskeyword(
        project_name_snake_case
    )


if __name__ == "__main__":
    if not is_validate_python_project_name(
        "{{ cookiecutter.__project_name_snake_case }}"
    ):
        project_name = "{{ cookiecutter.__project_name_snake_case }}"
        raise Exception(f"Error: {project_name} is not a valid Python module name!")
