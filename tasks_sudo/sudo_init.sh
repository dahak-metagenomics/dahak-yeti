#!/bin/bash

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

if [[ "$#" -eq 1 ]]
then

    DOTFILES="$HOME/dotfiles"
    cd $DOTFILES/tasks_sudo

    ./set_time.sh
    ./install_packages.sh
    ## this line may break something
    #./install_netdata.sh
    ./fix_ssh.sh
    ./gen_ssh_keys.sh
    ./set_machine_name.sh $1
    ./get_docker.sh
    ./get_docker_compose.sh
    ./make_temp.sh
    ./install_singularity.sh &> /tmp/install_singularity_log

else

    echo "No machine name specified"
    exit 1;

fi
