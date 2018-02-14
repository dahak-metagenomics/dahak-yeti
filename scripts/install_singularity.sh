#!/bin/bash
#
# Prepare the workflow for Singularity

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi


# ================================
# Install Prerequisites:

# Update aptitude and install dependencies
apt-get -y update

apt-get -y install zlib1g-dev
apt-get -y install ncurses-dev

# Install Docker
wget -qO- https://get.docker.com/ | sh
usermod -aG docker ubuntu


# ================================
# Install Singularity:

wget -O- http://neuro.debian.net/lists/xenial.us-ca.full | tee /etc/apt/sources.list.d/neurodebian.sources.list
apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
apt-get update
apt-get install -y singularity-container
singularity --version

echo ""
echo ""
echo "Singularity is now installed. Log out and log back in for docker group to take effect."
echo ""
echo ""

