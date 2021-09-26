.PHONY: clean
.DEFAULT_GOAL:= init

init:
	pip install -r requirements.txt

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

test: test-unit test-integration

build: clean
	python setup.py sdist bdist_wheel --universal

ci: check-style check-types test

link:
	pip install -e .
