#!/usr/bin/env python

from pathlib import Path
import json
import shutil
import subprocess

import upgrade_utils

if __name__ == "__main__":
    generated_dir = Path().absolute()

    license = "{{ cookiecutter.license }}"

    if license == "Not open source":
        # TODO do this with OS
        subprocess.run("rm LICENSE", cwd=generated_dir, shell=True, check=True)

    replay_file_src = (
        Path().home().joinpath(".cookiecutter_replay", "cookiecutter-pyproject.json")
    )

    replay_file_dest = generated_dir.joinpath(".cookiecutterrc.json")

    # If replay_file_dest doesn't exist that means this is the first instantiation
    if not replay_file_dest.is_file():
        shutil.copyfile(
            replay_file_src,
            replay_file_dest,
        )
        subprocess.run("git init", cwd=generated_dir, shell=True, check=True)
    else:
        with open(replay_file_dest, "rw") as cookiecutterrc_file:
            cookiecutterrc = json.load(cookiecutterrc_file)
            updated_cookiecutterrc = upgrade_utils.post_gen_upgrade(
                cookiecutterrc, generated_dir
            )
            json.dump(updated_cookiecutterrc, cookiecutterrc_file, indent=2)
