#!/bin/bash

USERID=`id -u`

if [ $USERID -ne 0 ]; then
    exec sudo bash $0
fi

md -p ~/.dotfiles

pacman -Sy git

git clone https://github.com/robertosixty1/nvim ~/.config/nvim
git clone https://github.com/robertosixty1/programs ~/.dotfiles/programs
git clone https://github.com/robertosixty1/shells ~/.dotfiles/shells

cd ~/.dotfiles/programs && bash ~/.dotfiles/programs/install.sh
cd ~/.dotfiles/shells && bash ~/.dotfiles/shells/install.sh