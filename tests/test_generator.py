import datetime
import os
import toml


def run_generated_project_assertions(generated_project, **kwargs):
    # These are the default values if no kwargs are given
    project_name_raw = "Sample project"
    project_name = "sample-project"
    project_name_snake_case = "sample_project"
    project_description = "Generated sample project from cookiecutter-pyproject"
    author_full_name = "Jane Doe"
    author_email = "jane.doe@example.com"
    github_organization = "janeDoe"
    project_repo = "https://github.com/janeDoe/sample-project"
    license = "MIT License"

    # Replace these variables if an override is given
    if "project_name_raw" in kwargs:
        project_name_raw = kwargs["project_name_raw"]

    if "project_name" in kwargs:
        project_name = kwargs["project_name"]

    if "project_name_snake_case" in kwargs:
        project_name_snake_case = kwargs["project_name_snake_case"]

    if "project_description" in kwargs:
        project_description = kwargs["project_description"]

    if "author_full_name" in kwargs:
        author_full_name = kwargs["author_full_name"]

    if "author_email" in kwargs:
        author_email = kwargs["author_email"]

    if "github_organization" in kwargs:
        github_organization = kwargs["github_organization"]

    if "project_repo" in kwargs:
        project_repo = kwargs["project_repo"]

    if "license" in kwargs:
        license = kwargs["license"]

    # Make sure correct context was passed to cookiecutter
    assert generated_project.context["project_name"] == project_name_raw
    assert (
        generated_project.context["project_name_snake_case"] == project_name_snake_case
    )
    assert generated_project.context["project_description"] == project_description
    assert generated_project.context["author_full_name"] == author_full_name
    assert generated_project.context["author_email"] == author_email
    assert generated_project.context["github_organization"] == github_organization
    assert generated_project.context["project_repo"] == project_repo
    assert generated_project.context["license"] == license
    # This is so when new variables are added/removed we know to add tests for them :)
    assert len(generated_project.context) == 8

    # make sure the project was generated correctly
    assert generated_project.exit_code == 0
    assert generated_project.exception is None
    assert generated_project.project_path.name == project_name
    assert generated_project.project_path.is_dir()

    project_path = generated_project.project_path

    # Check for top level files/folders to be present
    toplevel_files = os.listdir(project_path)

    assert ".flake8" in toplevel_files
    assert "LICENSE" in toplevel_files
    assert "requirements.txt" in toplevel_files
    assert "CHANGELOG.md" in toplevel_files
    assert "Makefile" in toplevel_files
    assert "pyproject.toml" in toplevel_files
    assert "tests" in toplevel_files
    assert "docs" in toplevel_files
    assert ".editorconfig" in toplevel_files
    assert "README.md" in toplevel_files
    assert "setup.py" in toplevel_files
    assert ".gitignore" in toplevel_files
    assert "scripts" in toplevel_files
    assert ".github" in toplevel_files
    assert ".git" in toplevel_files
    assert ".vscode" in toplevel_files
    assert project_name_snake_case in toplevel_files

    # Check files in project_name_snake_case

    # TODO: Check files in test folder

    # Check readme
    with open(os.path.join(project_path, "README.md"), "r") as readme_file:
        readme_content = readme_file.read()
        assert project_name in readme_content
        assert project_description in readme_content
        assert f"{project_repo}/actions/workflows/tests.yml/badge.svg" in readme_content

    # Project.toml file assertions
    with open(os.path.join(project_path, "pyproject.toml"), "r") as pyproj_file:
        project_metadata = toml.load(pyproj_file)

        assert project_name == project_metadata["project"]["name"]
        assert project_description == project_metadata["project"]["description"]
        assert author_full_name == project_metadata["project"]["authors"][0]["name"]
        assert author_email == project_metadata["project"]["authors"][0]["email"]
        assert author_full_name == project_metadata["project"]["maintainers"][0]["name"]
        assert author_email == project_metadata["project"]["maintainers"][0]["email"]

        assert project_repo == project_metadata["project"]["urls"]["homepage"]
        assert (
            f"{project_repo}/blob/master/CHANGELOG.md"
            == project_metadata["project"]["urls"]["changelog"]
        )
        assert (
            f"{project_repo}/blob/master/README.md"
            == project_metadata["project"]["urls"]["documentation"]
        )

        assert "LICENSE" == project_metadata["project"]["license"]["file"]
        # TODO check for OSI license in project_metadata["project"]["classifiers"]

        assert project_name in project_metadata["project"]["entry-points"]
        assert (
            f"{project_name_snake_case}.cli.entrypoint:main"
            == project_metadata["project"]["entry-points"][project_name]
        )

    # License file assertions
    with open(os.path.join(project_path, "LICENSE"), "r") as license_file:
        license_content = license_file.read()
        # first line must be the license name
        assert license_content.split(os.linesep)[0].strip() == license
        # Make sure the correct year is added to the license file
        assert str(datetime.datetime.now().year) in license_content
        assert author_full_name in license_content


def test_bake_project_with_defaults(cookies):
    generated_project = cookies.bake()
    run_generated_project_assertions(generated_project)


def test_bake_project_with_custom_raw_name(cookies):
    project_name_raw = "some Kool_proJect"
    generated_project = cookies.bake(extra_context={"project_name": project_name_raw})
    run_generated_project_assertions(
        generated_project,
        project_name_raw=project_name_raw,
        project_name="some-kool-project",
        project_name_snake_case="some_kool_project",
        project_repo="https://github.com/janeDoe/some-kool-project",
    )
