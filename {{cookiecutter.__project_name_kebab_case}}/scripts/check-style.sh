#!/usr/bin/env bash
set -e

source ./scripts/include/vars.sh

flake8 .
isort --check-only .
black --check .
