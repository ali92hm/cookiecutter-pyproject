#!/usr/bin/env bash
set -e

source ./scripts/include/vars.sh

VERSION=$(python -c "import {{ cookiecutter.__project_name_snake_case }}; print({{ cookiecutter.__project_name_snake_case }}.__version__)")
TAG="v$VERSION"

if [ -n "$(git status --porcelain)" ]; then
  echo "Error: the working tree is not clean. Commit or stash your changes first." >&2
  exit 1
fi

if git rev-parse --verify --quiet "refs/tags/$TAG" >/dev/null; then
  echo "Error: tag '$TAG' already exists." >&2
  echo "Bump __version__ in {{ cookiecutter.__project_name_snake_case }}/__init__.py before cutting a new release." >&2
  exit 1
fi

git tag --annotate "$TAG" --message "Release $TAG"

echo "Created tag $TAG. Push it to start the release workflow:"
echo
echo "    git push origin $TAG"
