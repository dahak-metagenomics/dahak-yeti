#!/bin/sh

# Actually make the swap directory vim is going to use
mkdir -p ~/.vim/swap
mkdir -p ~/.vim/undo
mkdir -p ~/.vim/backups

# Change shell to bash
BASH="/bin/bash"
echo "About to set shell to ${BASH}"
chsh -s ${BASH}


