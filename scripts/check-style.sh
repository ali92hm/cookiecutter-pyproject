#!/usr/bin/env bash
set -e

source ./scripts/include/vars.sh

ruff check .
ruff format --check .
