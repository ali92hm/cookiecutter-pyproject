#!/usr/bin/env bash
set -e

source ./scripts/include/vars.sh

black .
isort .
