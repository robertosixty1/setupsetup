#!/bin/env python3

from os import getenv, listdir
from subprocess import run
from sys import argv

USER = listdir("/home")[0]
HOME = getenv("HOME")

if getenv("USER") == "root":
    run(["sudo", "-u", USER, "python", __file__] + argv[1:])
    exit(0)

run(["git", "clone", "https://github.com/robertosixty1/nvim", f"{HOME}/.config/nvim"])

run(["git", "clone", "https://github.com/robertosixty1/programs", f"{HOME}/.config/programs"])
if argv[1] == "arch":
    run(["python", f"{HOME}/.config/programs/install.py", "arch"], cwd=f"{HOME}/.config/programs")
elif argv[1] == "fedora":
    run(["python", f"{HOME}/.config/programs/install.py", "fedora"], cwd=f"{HOME}/.config/programs")
else:
    run(["python", f"{HOME}/.config/programs/install.py", "ubuntu"], cwd=f"{HOME}/.config/programs")

run(["git", "clone", "https://github.com/robertosixty1/shells", f"{HOME}/.config/shells"])
run(["python", f"{HOME}/.config/shells/install.py"], cwd=f"{HOME}/.config/shells")

run(["git", "clone", "https://github.com/robertosixty1/config", f"{HOME}/.config/config"])
run(["python", f"{HOME}/.config/config/install.py"], cwd=f"{HOME}/.config/config")

run(["sudo", "systemctl", "enable", "--now", "cups.service"])
