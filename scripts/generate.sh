#!/usr/bin/env bash
set -e

source ./scripts/include/vars.sh

rm -rf $GENERATED_PROJECTS_FOLDER/manual

cookiecutter --output-dir $GENERATED_PROJECTS_FOLDER/manual .
