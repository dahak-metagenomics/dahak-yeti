#!/bin/bash
# 
# install some essential packages
#
# also see
# https://github.com/pyenv/pyenv/wiki/Common-build-problems

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

apt-get update
apt-get install -y git 
apt-get install -y vim
apt-get install -y screen
apt-get install -y aptitude
apt-get install -y build-essential
apt-get install -y curl
apt-get install -y wget
apt-get install -y graphviz
apt-get install -y awscli

apt -y autoremove
