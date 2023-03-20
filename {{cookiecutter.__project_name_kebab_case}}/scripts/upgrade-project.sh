#!/usr/bin/env bash
set -e

# TODO make sure there are no uncommited changes

cookiecutter --overwrite-if-exists --replay-file ../.cookiecutterrc.json https://github.com/ali92hm/cookiecutter-pyproject
