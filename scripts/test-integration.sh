#!/usr/bin/env bash
set -e

source ./scripts/include/vars.sh

pytest tests/integration --junitxml=$REPORTS_FOLDER/integration.xml $(ARGS)
