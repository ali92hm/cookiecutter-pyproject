#!/usr/bin/env python

import re

# TODO: Remove this block
# project_name_snake_case and project_name_kebab_case vairables while can be set by the
# user, they are not meant to. In later versions of cookiecutter we can add __ prefix
# to them in order to hide them from the user.
# In the meantime, we till throw an exception if they are different than the project name
project_name = "{{ cookiecutter.project_name_snake_case }}"
project_name_snake_case = "{{ cookiecutter.project_name_snake_case }}"
project_name_kebab_case = "{{ cookiecutter.project_name_kebab_case }}"

if project_name.lower().replace(" ", "_").replace("-", "_") != project_name_snake_case:
    raise Exception(
        "Error: project_name_snake_case cannot be set. This input will be removed in the future"
    )

if project_name.lower().replace(" ", "-").replace("_", "-") != project_name_kebab_case:
    raise Exception(
        "Error: project_name_kebab_case cannot be set. This input will be removed in the future"
    )

# end block

MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"
project_name = "{{ cookiecutter.project_name_snake_case }}"
project_name_snake_case = "{{ cookiecutter.project_name_snake_case }}"

if not re.match(MODULE_REGEX, project_name_snake_case):
    raise Exception(f"Error: {project_name} is not a valid Python module name!")
