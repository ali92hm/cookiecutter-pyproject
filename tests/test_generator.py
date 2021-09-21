def test_bake_project_with_defaults(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "sample-project"
    assert result.project_path.is_dir()


def test_bake_project_with_custom_input(cookies):
    result = cookies.bake(extra_context={"project_name": "some Kool_project"})

    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.name == "some-kool-project"
    assert result.project_path.is_dir()
