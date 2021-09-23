import setuptools
import toml

# While setuptools is in the process of add support for reading project metadata from
# pyproject.toml according to https://github.com/pypa/setuptools/issues/1688 the code
# below is a stop gap to read such metadata from the pyproject.toml and pass it to the
# setup function. Hopefully in the future we can remove this file entirely or just
# replace it with setuptools.setup()

with open("./pyproject.toml") as pyproj_file:
    project_metadata = toml.load(pyproj_file)

with open(project_metadata["project"]["readme"]) as readme_file:
    readme_content = readme_file.read()

with open(project_metadata["project"]["license"]["file"]) as license_file:
    license = license_file.readline().strip()

src_folder = project_metadata["project"]["name"].replace("-", "_")
packages = setuptools.find_packages(include=[src_folder, f"{src_folder}.*"])

console_scripts = list()
if "entry-points" in project_metadata["project"]:
    for script_name, script_path in project_metadata["project"]["entry-points"].items():
        console_scripts.append(f"{script_name}={script_path}")

gui_scripts = list()
if "gui-scripts" in project_metadata["project"]:
    for script_name, script_path in project_metadata["project"]["gui-scripts"].items():
        gui_scripts.append(f"{script_name}={script_path}")

setup_args = dict(
    name=project_metadata["project"]["name"],
    author=project_metadata["project"]["authors"][0]["name"],
    author_email=project_metadata["project"]["authors"][0]["email"],
    maintainer=project_metadata["project"]["maintainers"][0]["name"],
    maintainer_email=project_metadata["project"]["maintainers"][0]["email"],
    url=project_metadata["project"]["urls"]["homepage"],
    description=project_metadata["project"]["description"],
    long_description=readme_content,
    long_description_content_type="text/markdown",
    packages=packages,
    classifiers=project_metadata["project"]["classifiers"],
    license=license,
    license_files=[project_metadata["project"]["license"]["file"]],
    python_requires=project_metadata["project"]["requires-python"],
    keywords=project_metadata["project"]["keywords"],
    install_requires=project_metadata["project"]["dependencies"],
    entry_points={"console_scripts": console_scripts, "gui_scripts": gui_scripts},
    zip_safe=False,
    version=project_metadata["project"]["version"],
)

setuptools.setup(**setup_args)
