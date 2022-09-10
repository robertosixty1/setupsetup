#!/bin/env python3

from os import getenv, listdir, chdir as cd
from subprocess import run

USER = listdir("/home")[0]
HOME = getenv("HOME")

if getenv("USER") == "root":
    run(["sudo", "-u", USER, "python", __file__])
    exit(0)

run(["git", "clone", "https://github.com/robertosixty1/nvim", f"{HOME}/.config/nvim"])


run(["git", "clone", "https://github.com/robertosixty1/programs", f"{HOME}/.config/programs"])
cd(f"{HOME}/.config/programs")
run(["python", f"{HOME}/.config/programs/install.py"])

run(["git", "clone", "https://github.com/robertosixty1/shells", f"{HOME}/.config/shells"])
cd(f"{HOME}/.config/shells")
run(["python", f"{HOME}/.config/shells/install.py"])

run(["sudo", "systemctl", "enable", "--now", "cups.service"])