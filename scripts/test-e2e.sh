#!/usr/bin/env bash
set -e

source ./scripts/include/vars.sh

pytest tests/e2e --junitxml=$REPORTS_FOLDER/e2e.xml $(ARGS)
