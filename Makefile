.PHONY: clean
.DEFAULT_GOAL:= init

init:
	pip install -r requirements_dev.txt

clean:
	./scripts/clean.sh

check-style:
	./scripts/check-style.sh

fix-style:
	./scripts/fix-style.sh

check-types:
	mypy .

test-unit:
	./scripts/test-unit.sh

test-integration:
	./scripts/test-integration.sh

test-e2e:
	./scripts/test-e2e.sh

test: test-unit test-integration test-e2e

build: clean
	python setup.py sdist bdist_wheel --universal

release:
	twine upload dist/*

ci: check-style check-types test

link:
	pip install -e .
