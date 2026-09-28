.PHONY: init clean check-style fix-style check-types test-unit test-integration \
	test-e2e test build check-version release-tag ci generate
.DEFAULT_GOAL:= init

init:
	pip install --group dev

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
	python -m build

check-version:
	./scripts/check-version.sh $(TAG)

release-tag:
	./scripts/release-tag.sh

ci: check-style check-types test

generate:
	./scripts/generate.sh
