#!/usr/bin/env python

from pathlib import Path
import shutil
import subprocess

if __name__ == "__main__":
    generated_dir = Path().absolute()

    license = "{{ cookiecutter.license }}"

    if license == "Not open source":
        subprocess.run("rm LICENSE", cwd=generated_dir, shell=True, check=True)

    replay_file_src = (
        Path().home().joinpath(".cookiecutter_replay", "cookiecutter-pyproject.json")
    )

    replay_file_dest = generated_dir.joinpath(".cookiecutterrc.json")

    shutil.copyfile(
        replay_file_src,
        replay_file_dest,
    )
    subprocess.run("git init", cwd=generated_dir, shell=True, check=True)
