# First time setup

This document covers the manual steps that are needed once, after this project was
generated. Delete the steps that do not apply to you.

## Push the project to GitHub

The generator already ran `git init` for you, so all that is left is to make the first
commit and point the repository at its remote:

```bash
git add .
git commit -m "Initial commit"
git branch -M master
git remote add origin {{ cookiecutter.project_repo }}.git
git push -u origin master
```

## Fill in the placeholders

A few files are intentionally left incomplete:

-   `pyproject.toml` has `# fill me` markers under `dependencies` and `keywords`
-   `README.md` has `<!-- Add me -->` markers for the getting started sections

{% if cookiecutter.license != 'Not open source' -%}
## Set up publishing to PyPI

Releases publish to PyPI using [trusted publishing], which uses a short lived OpenID
Connect token instead of a long lived API token. There is no secret to create, store, or
rotate.

1.  Go to <https://pypi.org/manage/account/publishing/> and add a new pending publisher.
2.  Fill in the form:
    -   **PyPI Project Name**: `{{ cookiecutter.__project_name_kebab_case }}`
    -   **Owner**: `{{ cookiecutter.github_organization }}`
    -   **Repository name**: `{{ cookiecutter.__project_name_kebab_case }}`
    -   **Workflow name**: `release.yml`
    -   **Environment name**: leave empty
3.  Cut your first release by following the release process in the
    [development instructions].

The package name must still be available on PyPI. Check
<https://pypi.org/project/{{ cookiecutter.__project_name_kebab_case }}/> before you rely
on it, and rename the project if it is taken.

{% endif -%}
## Recommended repository settings

-   Protect `master` and require the `Tests` workflow to pass before merging, so that
    tagged commits have always been through CI
-   Enable "Automatically delete head branches" to keep the branch list tidy

{% if cookiecutter.license != 'Not open source' -%}
[trusted publishing]: https://docs.pypi.org/trusted-publishers/
{% endif -%}
[development instructions]: development-instructions.md
