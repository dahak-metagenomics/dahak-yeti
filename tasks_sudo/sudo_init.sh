#!/bin/bash

if [[ "$#" -eq 1 ]]
then

    DOTFILES="$HOME/dotfiles"
    cd $DOTFILES/tasks_sudo

    ./set_time.sh
    ./install_packages.sh
    ./fix_ssh.sh
    ./gen_ssh_keys.sh
    ./set_machine_name.sh $1
    ./get_docker.sh
    ./make_temp.sh
    ./install_singularity.sh &> /tmp/install_singularity_log

else

    echo "No machine name specified"
    exit 1;

fi
