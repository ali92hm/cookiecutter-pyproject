import subprocess


def install_dep_and_run_ci(generated_project):
    project_path = generated_project.project_path

    subprocess.run("make init", cwd=project_path, shell=True, check=True)
    subprocess.run("make ci", cwd=project_path, shell=True, check=True)
    subprocess.run("make build", cwd=project_path, shell=True, check=True)
    subprocess.run("make clean", cwd=project_path, shell=True, check=True)


def test_e2e_defaults(cookies):
    generated_project = cookies.bake()
    install_dep_and_run_ci(generated_project)


def test_e2e_no_license(cookies):
    generated_project = cookies.bake(extra_context={"license": "Not open source"})
    install_dep_and_run_ci(generated_project)
