#!/usr/bin/env python
import utils

# TODO: Remove this block
# project_name_snake_case and project_name_kebab_case vairables while can be set by the
# user, they are not meant to. In later versions of cookiecutter we can add __ prefix
# to them in order to hide them from the user.
# In the meantime, we till throw an exception if they are different than the project name
project_name = "{{ cookiecutter.project_name_snake_case }}"
project_name_snake_case = "{{ cookiecutter.project_name_snake_case }}"
project_name_kebab_case = "{{ cookiecutter.project_name_kebab_case }}"

if utils.get_project_name_snake_case(project_name) != project_name_snake_case:
    raise Exception(
        "Error: project_name_snake_case cannot be set. This input will be removed in the future"
    )

if utils.get_project_name_kebab_case(project_name) != project_name_kebab_case:
    raise Exception(
        "Error: project_name_kebab_case cannot be set. This input will be removed in the future"
    )

# end block

if not utils.is_validate_project_name("{{ cookiecutter.project_name_snake_case }}"):
    project_name = "{{ cookiecutter.project_name_snake_case }}"
    raise Exception(f"Error: {project_name} is not a valid Python module name!")
