import datetime
import json
import os
from pathlib import Path

import pytest
import tomli

from hooks import pre_gen_project


def get_cookiecutter_defaults():
    root = Path(__file__).resolve().parent.parent.parent
    with open(os.path.join(root, "cookiecutter.json"), "r") as cookie_cutter_file:
        return json.load(cookie_cutter_file)


def run_generated_project_assertions(generated_project, **kwargs):
    # These are the default values if no kwargs are given
    cookie_cutter_file = get_cookiecutter_defaults()
    project_name = cookie_cutter_file["project_name"]
    project_description = cookie_cutter_file["project_description"]
    author_full_name = cookie_cutter_file["author_full_name"]
    author_email = cookie_cutter_file["author_email"]
    github_organization = cookie_cutter_file["github_organization"]
    project_repo = (
        f"https://github.com/{github_organization}/"
        + f"{pre_gen_project.get_project_name_kebab_case(project_name)}"
    )
    license = cookie_cutter_file["license"][0]

    # Replace these variables if an override is given
    if "project_name" in kwargs:
        project_name = kwargs["project_name"]

    project_name_snake_case = pre_gen_project.get_project_name_snake_case(project_name)
    project_name_kebab_case = pre_gen_project.get_project_name_kebab_case(project_name)

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
    if license != "Not open source":
        assert "LICENSE" in toplevel_files
    else:
        assert "LICENSE" not in toplevel_files
    assert "requirements.txt" in toplevel_files
    assert "CHANGELOG.md" in toplevel_files
    assert "Makefile" in toplevel_files
    assert "pyproject.toml" in toplevel_files
    assert "tests" in toplevel_files
    assert "docs" in toplevel_files
    assert ".editorconfig" in toplevel_files
    assert "README.md" in toplevel_files
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
    top_level_test_files = os.listdir(os.path.join(project_path, "tests"))
    assert "__init__.py" in top_level_test_files
    assert "unit" in top_level_test_files
    assert "integration" in top_level_test_files

    unit_test_files = os.listdir(os.path.join(project_path, "tests", "unit"))
    assert "__init__.py" in unit_test_files
    assert f"test_{project_name_snake_case}.py" in unit_test_files

    integration_test_files = os.listdir(
        os.path.join(project_path, "tests", "integration")
    )
    assert "__init__.py" in integration_test_files
    assert f"test_{project_name_snake_case}.py" in integration_test_files

    # Check readme
    with open(os.path.join(project_path, "README.md"), "r") as readme_file:
        readme_content = readme_file.read()
        assert project_name in readme_content
        assert project_description in readme_content
        assert f"{project_repo}/actions/workflows/tests.yml/badge.svg" in readme_content

    # Project.toml file assertions
    with open(os.path.join(project_path, "pyproject.toml"), "rb") as pyproj_file:
        project_metadata = tomli.load(pyproj_file)

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

        if license == "Not open source":
            assert "license" not in project_metadata["project"]
        else:
            assert project_metadata["project"]["license"]["file"] == "LICENSE"

        # TODO: Move this map as a private variable to cookiecutter.json when this
        # https://github.com/cookiecutter/cookiecutter/issues/1582 is resolved
        pypi_license_map = {
            "MIT License": "License :: OSI Approved :: MIT License",
            "BSD 2-Clause License": "License :: OSI Approved :: BSD License",
            "BSD 3-Clause License": "License :: OSI Approved :: BSD License",
            "ISC License": "License :: OSI Approved :: ISC License (ISCL)",
            "Apache License Version 2.0": "License :: OSI Approved :: Apache Software License",
            "GNU General Public License Version 3": "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Unlicense": "License :: OSI Approved :: The Unlicense (Unlicense)",
            "Not open source": "",
        }

        if license != "Not open source":
            assert (
                pypi_license_map[license] in project_metadata["project"]["classifiers"]
            )
        else:
            for _, value in pypi_license_map.items():
                # None of these items should be in the array
                assert value not in project_metadata["project"]["classifiers"]

        assert project_name_kebab_case in project_metadata["project"]["scripts"]
        assert (
            project_metadata["project"]["scripts"][project_name_kebab_case]
            == f"{project_name_snake_case}.cli.entrypoint:main"
        )

    # License file assertions
    if license != "Not open source":
        with open(os.path.join(project_path, "LICENSE"), "r") as license_file:
            license_content = license_file.read()
            # first line must be the license name
            assert license_content.splitlines()[0].strip().lower() == license.lower()
            # Make sure the correct year is added to the license file
            if license != "Unlicense":
                assert str(datetime.datetime.now().year) in license_content
                assert author_full_name in license_content


def test_bake_project_with_defaults_should_succeed(cookies):
    generated_project = cookies.bake()
    run_generated_project_assertions(generated_project)


def test_bake_project_with_custom_project_name_should_succeed(cookies):
    project_name = "s0me Kool2_proJect"
    generated_project = cookies.bake(extra_context={"project_name": project_name})
    run_generated_project_assertions(
        generated_project,
        project_name=project_name,
        project_repo="https://github.com/janeDoe/s0me-kool2-project",
    )


@pytest.mark.parametrize(
    "project_name",
    ["my&project", "$$project", "[sdf]23", "1234", "1sdf", "cool^project"],
)
def test_bake_with_not_valid_project_name_should_fail(project_name, cookies):
    generated_project = cookies.bake(
        extra_context={
            "project_name": project_name,
        }
    )

    assert generated_project.exception is not None
    assert generated_project.exit_code == -1


# TODO: Delete this after migration to cookiecutter 2.0
def test_bake_project_with_custom_snake_case_name_should_fail(cookies):
    generated_project = cookies.bake(
        extra_context={
            "project_name": "my project",
            "project_name_snake_case": "my_project_2",
        }
    )

    assert generated_project.exception is not None
    assert generated_project.exit_code == -1


# TODO: Delete this after migration to cookiecutter 2.0
def test_bake_project_with_custom_kebab_case_name_should_fail(cookies):
    generated_project = cookies.bake(
        extra_context={
            "project_name": "my project",
            "project_name_kebab_case": "my-cool-project",
        }
    )

    assert generated_project.exception is not None
    assert generated_project.exit_code == -1


def test_bake_with_custom_metadata_should_succeed(cookies):
    input_data = {
        "project_name": "advanced calculator",
        "project_description": "This calculator can be used in a rocket ship",
        "author_full_name": "Bruce wayne",
        "author_email": "bruce@wayneenterprises.com",
        "github_organization": "theDarkKight",
        "project_repo": "https://onprem.com/wayneenterprises/bruce-advance-calc",
    }

    generated_project = cookies.bake(extra_context=input_data)

    run_generated_project_assertions(generated_project, **input_data)


def test_bake_with_auto_generated_project_repo_should_succeed(cookies):
    project_name = "Mission controller"
    github_organization = "nasa"
    generated_project = cookies.bake(
        extra_context={
            "project_name": project_name,
            "github_organization": github_organization,
        }
    )

    run_generated_project_assertions(
        generated_project,
        project_name=project_name,
        github_organization=github_organization,
        project_repo="https://github.com/nasa/mission-controller",
    )


@pytest.mark.parametrize("license", get_cookiecutter_defaults()["license"])
def test_bake_with_different_licesens_should_succeed(license, cookies):
    generated_project = cookies.bake(extra_context={"license": license})

    run_generated_project_assertions(generated_project, license=license)
