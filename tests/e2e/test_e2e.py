import os
import subprocess
import venv


def install_dep_and_run_ci(generated_project):
    project_path = generated_project.project_path

    # Install the generated project's own dependencies into a throwaway venv rather
    # than the environment running this test suite, so `make init` here can't leak
    # packages (or version conflicts) into it.
    venv_dir = project_path / ".venv"
    venv.create(venv_dir, with_pip=True)

    venv_bin = venv_dir / ("Scripts" if os.name == "nt" else "bin")
    env = os.environ.copy()
    env["PATH"] = os.pathsep.join([str(venv_bin), env.get("PATH", "")])
    env["VIRTUAL_ENV"] = str(venv_dir)
    env.pop("PYTHONHOME", None)

    # The pip bundled via ensurepip in a fresh venv can be far behind the pip that
    # provisioned this test environment (e.g. old enough to lack `--group`, PEP 735,
    # which `make init` relies on). Upgrade it before using it.
    python = venv_bin / ("python.exe" if os.name == "nt" else "python")
    subprocess.run(
        [str(python), "-m", "pip", "install", "--upgrade", "pip"],
        cwd=project_path,
        check=True,
        env=env,
    )

    subprocess.run("make init", cwd=project_path, shell=True, check=True, env=env)
    subprocess.run("make ci", cwd=project_path, shell=True, check=True, env=env)
    subprocess.run("make build", cwd=project_path, shell=True, check=True, env=env)
    subprocess.run("make clean", cwd=project_path, shell=True, check=True, env=env)


def test_e2e_defaults(cookies):
    generated_project = cookies.bake()
    install_dep_and_run_ci(generated_project)


def test_e2e_no_license(cookies):
    generated_project = cookies.bake(extra_context={"license": "Not open source"})
    install_dep_and_run_ci(generated_project)
