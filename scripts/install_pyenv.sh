#!/bin/bash

if [ "$(id -u)" == "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as a normal user."
    echo ""
    echo ""
    exit 1;
fi

# Install pyenv 
curl -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash

## This should already be in ~/.bash_profile
#echo 'export PATH="~/.pyenv/bin:$PATH"' >> ~/.bash_profile

