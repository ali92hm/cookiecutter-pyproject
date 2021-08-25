
init:
	clean
	poetry env use python
	install

install:
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

ci-test:
	check-style
	check-types
	test