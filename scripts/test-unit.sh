#!/usr/bin/env bash
set -e

source ./scripts/include/vars.sh

pytest tests/unit --junitxml=$REPORTS_FOLDER/unit.xml "$ARGS"
