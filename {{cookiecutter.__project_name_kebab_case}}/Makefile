.PHONY: init clean check-style fix-style check-types test-unit test-integration \
	test check-version release-tag ci link build
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
	python -m build

check-version:
	./scripts/check-version.sh $(TAG)

release-tag:
	./scripts/release-tag.sh

ci: check-style check-types test

link:
	pip install --editable .
