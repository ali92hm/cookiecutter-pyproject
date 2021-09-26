import pytest

from hooks import pre_gen_project


@pytest.mark.parametrize(
    "name_input,expected",
    [
        ("a34akfi5", "a34akfi5"),
        ("TeST proJect", "test-project"),
        ("123TeST proJect123", "123test-project123"),
        ("Test^&Project", "test^&project"),
        ("Te_st-Pro_-jct", "te-st-pro--jct"),
    ],
)
def test_get_project_name_kebab_case(name_input, expected):
    assert pre_gen_project.get_project_name_kebab_case(name_input) == expected


@pytest.mark.parametrize(
    "name_input,expected",
    [
        ("a34akfi5", "a34akfi5"),
        ("TeST proJect", "test_project"),
        ("123TeST proJect123", "123test_project123"),
        ("Test^&Project", "test^&project"),
        ("Te_st-Pro_-jct", "te_st_pro__jct"),
    ],
)
def test_get_project_name_snake_case(name_input, expected):
    assert pre_gen_project.get_project_name_snake_case(name_input) == expected


@pytest.mark.parametrize(
    "name_input,expected",
    [
        ("a34akfi5", True),
        ("TeST proJect", False),
        ("123TeST proJect", False),
        ("TeST proJect134", False),
        ("Test^&Project", False),
        ("Te_st-Pro_-jct", False),
    ],
)
def test_is_validate_python_project_name(name_input, expected):
    assert pre_gen_project.is_validate_python_project_name(name_input) == expected
