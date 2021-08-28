.PHONY: clean install
.DEFAULT_GOAL:= install

init: install

install:
	pip install -r requirements_dev.txt

clean:
	rm -rf .generated
	rm -rf .mypy_cache
	rm -rf .pytest_cache
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

ci: check-style check-types test