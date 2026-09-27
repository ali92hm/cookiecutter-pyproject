#!/usr/bin/env bash
set -e

source ./scripts/include/vars.sh

TAG="${1:-}"

if [ -z "$TAG" ]; then
  echo "Usage: $0 <tag>" >&2
  echo "Example: $0 v1.2.3" >&2
  exit 1
fi

VERSION=$(cat VERSION)

if [ "$TAG" != "v$VERSION" ]; then
  echo "Error: tag '$TAG' does not match the package version '$VERSION'." >&2
  echo "Either bump the VERSION file, or tag 'v$VERSION' instead." >&2
  exit 1
fi

echo "Tag '$TAG' matches the package version '$VERSION'"
