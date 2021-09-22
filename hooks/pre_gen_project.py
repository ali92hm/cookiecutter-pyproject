#!/usr/bin/env python

import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"

project_name_snake_case = "{{ cookiecutter.project_name_snake_case }}"

if not re.match(MODULE_REGEX, project_name_snake_case):
    print(f"ERROR: {project_name_snake_case} is not a valid Python module name!")
    sys.exit(1)
