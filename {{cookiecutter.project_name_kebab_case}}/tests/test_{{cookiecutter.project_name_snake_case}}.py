from {{ cookiecutter.project_name_snake_case }} import {{ cookiecutter.project_name_snake_case }}


def test_add():
    res = {{ cookiecutter.project_name_snake_case }}.add(2, 5)
    assert res == 5
