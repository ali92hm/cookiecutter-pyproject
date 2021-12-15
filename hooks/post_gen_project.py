#!/usr/bin/env python

import os
import subprocess

if __name__ == "__main__":
    GENERATED_DIR = os.path.abspath(os.path.curdir)

    license = "{{ cookiecutter.license }}"

    if license == "Not open source":
        subprocess.run("rm LICENSE", cwd=GENERATED_DIR, shell=True, check=True)

    subprocess.run("git init", cwd=GENERATED_DIR, shell=True, check=True)
