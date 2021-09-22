import datetime
import os
import toml


def run_generated_project_assertions(generated_project, **kwargs):
    # These are the default values if no kwargs are given
    project_name = "Sample project"
    project_description = "Generated sample project from cookiecutter-pyproject"
    author_full_name = "Jane Doe"
    author_email = "jane.doe@example.com"
    github_organization = "janeDoe"
    project_repo = "https://github.com/janeDoe/sample-project"
    license = "MIT License"

    # Replace these variables if an override is given
    if "project_name" in kwargs:
        project_name = kwargs["project_name"]

    project_name_snake_case = project_name.lower().replace(" ", "_").replace("-", "_")
    project_name_kebab_case = project_name.lower().replace(" ", "-").replace("_", "-")

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
    assert generated_project.context["project_name"] == project_name
    assert (
        generated_project.context["project_name_snake_case"] == project_name_snake_case
    )
    assert (
        generated_project.context["project_name_kebab_case"] == project_name_kebab_case
    )
    assert generated_project.context["project_description"] == project_description
    assert generated_project.context["author_full_name"] == author_full_name
    assert generated_project.context["author_email"] == author_email
    assert generated_project.context["github_organization"] == github_organization
    assert generated_project.context["project_repo"] == project_repo
    assert generated_project.context["license"] == license
    # This is so when new variables are added/removed we know to add tests for them :)
    assert len(generated_project.context) == 9

    # make sure the project was generated correctly
    assert generated_project.exit_code == 0
    assert generated_project.exception is None
    assert generated_project.project_path.name == project_name_kebab_case
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

    # Check files in source project files
    src_files = os.listdir(os.path.join(project_path, project_name_snake_case))
    assert "cli" in src_files
    assert "__init__.py" in src_files
    assert "__main__.py" in src_files
    assert f"{project_name_snake_case}.py" in src_files

    # Check files in test folder
    test_files = os.listdir(os.path.join(project_path, "tests"))
    assert "__init__.py" in test_files
    assert f"test_{project_name_snake_case}.py" in test_files

    # Check readme
    with open(os.path.join(project_path, "README.md"), "r") as readme_file:
        readme_content = readme_file.read()
        assert project_name in readme_content
        assert project_description in readme_content
        assert f"{project_repo}/actions/workflows/tests.yml/badge.svg" in readme_content

    # Project.toml file assertions
    with open(os.path.join(project_path, "pyproject.toml"), "r") as pyproj_file:
        project_metadata = toml.load(pyproj_file)

        assert project_metadata["project"]["name"] == project_name_snake_case.replace(
            "_", "-"
        )
        assert project_metadata["project"]["description"] == project_description
        assert project_metadata["project"]["authors"][0]["name"] == author_full_name
        assert project_metadata["project"]["authors"][0]["email"] == author_email
        assert project_metadata["project"]["maintainers"][0]["name"] == author_full_name
        assert project_metadata["project"]["maintainers"][0]["email"] == author_email

        assert project_metadata["project"]["urls"]["homepage"] == project_repo
        assert (
            project_metadata["project"]["urls"]["changelog"]
            == f"{project_repo}/blob/master/CHANGELOG.md"
        )
        assert (
            project_metadata["project"]["urls"]["documentation"]
            == f"{project_repo}/blob/master/README.md"
        )

        assert project_metadata["project"]["license"]["file"] == "LICENSE"
        # TODO check for OSI license in project_metadata["project"]["classifiers"]

        assert project_name_kebab_case in project_metadata["project"]["entry-points"]
        assert (
            project_metadata["project"]["entry-points"][project_name_kebab_case]
            == f"{project_name_snake_case}.cli.entrypoint:main"
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
    project_name = "some Kool_proJect"
    generated_project = cookies.bake(extra_context={"project_name": project_name})
    run_generated_project_assertions(
        generated_project,
        project_name=project_name,
        project_repo="https://github.com/janeDoe/some-kool-project",
    )


# def test_bake_project_with_custom_snake_case_name(cookies):
#     project_name_input = "my project"
#     project_snake_case = "my_project_2"
#     generated_project = cookies.bake(
#         extra_context={
#             "project_name": project_name_input,
#             "project_name_snake_case": project_snake_case,
#         }
#     )
#     run_generated_project_assertions(
#         generated_project,
#         project_name_input=project_name_input,
#         project_name="my-project",
#         project_name_snake_case=project_snake_case,
#         project_repo="https://github.com/janeDoe/my-project",
#     )
