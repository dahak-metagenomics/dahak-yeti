#!/bin/bash
#
# boot-to-dahak-yeti script
# 
# This script is intended to get you from
# bare metal to a machine ready to run
# dahak workflows (including dotfiles, scripts,
# python, snakemake, and singularity.)
#
# Run as a one-shot installer:
# bash <( curl http://url-of-raw-script-file )
set -x

USER="ubuntu"

# first things first
apt-get update
apt-get install -y git

# get copy of dotfiles for root user
DOTFILES="$HOME/dotfiles"
git clone https://github.com/charlesreid1/dahak-yeti $DOTFILES

# run root init script
$DOTFILES/tasks_sudo/sudo_init.sh dahak-yeti

# copy the user init script
cp $DOTFILES/tasks_user/user_init.sh /home/$USER/.
chown $USER:$USER /home/$USER/user_init.sh
sudo -H -i -u $USER /home/$USER/user_init.sh
