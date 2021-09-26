#!/usr/bin/env python

import os
import subprocess


if __name__ == "__main__":
    GENERATED_DIR = os.path.abspath(os.path.curdir)
    subprocess.run("git init", cwd=GENERATED_DIR, shell=True, check=True)
