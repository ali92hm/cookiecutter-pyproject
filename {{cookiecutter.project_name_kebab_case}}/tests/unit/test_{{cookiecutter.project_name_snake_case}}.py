import pytest

from {{ cookiecutter.project_name_snake_case }} import {{ cookiecutter.project_name_snake_case }}


class Test{{ cookiecutter.project_name_snake_case.capitalize().replace('_', '') }}:
    def test_add_unit(self):
        res = {{ cookiecutter.project_name_snake_case }}.add(2, 3)
        assert res == 5

    @pytest.mark.skip(reason="Test skiping test")
    def test_skip(self):
        assert False
