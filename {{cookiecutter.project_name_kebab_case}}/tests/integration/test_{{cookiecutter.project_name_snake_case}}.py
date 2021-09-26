from {{ cookiecutter.project_name_snake_case }} import {{ cookiecutter.project_name_snake_case }}


def test_add_integration():
    res = {{ cookiecutter.project_name_snake_case }}.add(2, 3)
    assert res == 5
