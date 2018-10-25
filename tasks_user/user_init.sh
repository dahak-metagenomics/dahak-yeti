#!/bin/bash
#
# initialize all the dotfiles stuff for user 
set -x

YETI="$HOME/yeti"
git clone https://github.com/dahak-metagenomics/dahak-yeti $YETI

cd $YETI/tasks_user

./pre_bootstrap.sh
(
cd ../
./bootstrap.sh -f
)
. ~/.bash_profile
./prepare_vim.sh
./gen_ssh_keys.sh
./install_pyenv.py
. ~/.bash_profile
./activate_conda.py
./install_virtualenv.py
./install_snakemake.py
