#!/bin/bash
#
# Prepare the workflow for Snakemake and Singularity

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

# Update aptitude and install stuff
apt-get -y update

apt-get -y install zlib1g-dev
apt-get -y install ncurses-dev

# Update pip as normal user
su - ubuntu -c 'pip install --upgrade pip'

# Install Open Science Framework CLI client
su - ubuntu -c 'pip install osfclient'

# Install Docker
wget -qO- https://get.docker.com/ | sh
usermod -aG docker ubuntu



# ================================
# Install Snakemake:

CONDA="miniconda3-4.3.30"

# Use pyenv to install conda 
pyenv install $CONDA

# Set that as the distro of choice
pyenv global $CONDA

# This sets the $PATH shims so condaa is the pyenv conda
eval "$(pyenv init -)"

conda config --add channels r
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda

conda install -c bioconda snakemake



# ================================
# Install Singularity:

wget -O- http://neuro.debian.net/lists/xenial.us-ca.full | tee /etc/apt/sources.list.d/neurodebian.sources.list
apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
apt-get update
apt-get install -y singularity-container
singularity --version




