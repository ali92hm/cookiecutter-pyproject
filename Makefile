.PHONY: clean install
.DEFAULT_GOAL:= install

init: clean init/poetry install

init/poetry:
	poetry env use python

install: clean
	poetry install

clean:
	rm -rf .generated
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

check-style:
	poetry run flake8 .

fix-style:
	poetry run black .

check-types:
	poetry run mypy .

test:
	poetry run pytest

ci: check-style check-types test