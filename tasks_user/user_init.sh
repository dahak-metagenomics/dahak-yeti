#!/bin/bash
#
# initialize all the dotfiles stuff for user 
set -x

DOTFILES="$HOME/dotfiles"
mkdir -p $DOTFILES

YETI="$DOTFILES/dahak-yeti"
git clone https://github.com/charlesreid1/dahak-yeti $YETI

cd $YETI/tasks_user

./pre_bootstrap.sh
(
cd ../
./bootstrap.sh -f
./gen_ssh_keys.sh
)
./install_netdata.sh
./install_pyenv.py
./install_snakemake.py
./install_singularity.py

