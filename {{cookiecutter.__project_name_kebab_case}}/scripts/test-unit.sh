#!/usr/bin/env bash
set -e

source ./scripts/include/vars.sh

pytest tests/unit --junitxml=$REPORTS_FOLDER/unit.xml --cov={{ cookiecutter.__project_name_snake_case }} --cov-report=term-missing $ARGS
