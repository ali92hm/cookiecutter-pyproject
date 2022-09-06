#!/usr/bin/env bash
set -e

source ./scripts/include/vars.sh

rm -rf .mypy_cache
rm -rf .pytest_cache
rm -fr dist/
rm -fr build/
rm -rf *.egg-info/
rm -rf *.egg
rm -rf $REPORTS_FOLDER
find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +
find . -name '__pycache__' -exec rm -fr {} +
