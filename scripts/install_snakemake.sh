#!/bin/bash

if [ "$(id -u)" == "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as a normal user."
    echo ""
    echo ""
    exit 1;
fi


# ================================
# Install Snakemake:

CONDA="miniconda3-4.3.30"

# Use pyenv to install conda 
pyenv install $CONDA

# Set that as the distro of choice
pyenv global $CONDA

# This sets the $PATH shims so condaa is the pyenv conda
eval "$(pyenv init -)"

conda update
conda config --add channels r
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda

conda install -c bioconda snakemake


# ===============================
# Install OSF CLI client

pip install --upgrade pip
pip install --user osfclient

