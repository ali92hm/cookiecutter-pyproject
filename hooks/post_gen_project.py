#!/usr/bin/env python

import os
import subprocess

GENERATED_DIR = os.path.abspath(os.path.curdir)


def remove_file(filepath: str) -> None:
    os.remove(os.path.join(GENERATED_DIR, filepath))


subprocess.run("git init", cwd=GENERATED_DIR, shell=True, check=True)
