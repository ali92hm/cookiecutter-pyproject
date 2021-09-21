.PHONY: clean
.DEFAULT_GOAL:= init

init:
	pip install -r requirements_dev.txt

clean:
	rm -rf .generated
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -fr dist/
	rm -fr build/
	rm -rf *.egg-info/
	rm -rf *.egg
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

check-style:
	flake8 .

fix-style:
	black .

check-types:
	mypy .

test:
	pytest

build: clean
	python setup.py sdist bdist_wheel

ci: check-style check-types test

link:
	pip install -e .
