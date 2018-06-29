#!/bin/bash
#
# instal singularity from source

VERSION="2.5"

# prepare to install
apt-get install -y libarchive-dev

# download singularity
wget https://github.com/singularityware/singularity/releases/download/${VERSION}/singularity-${VERSION}.tar.gz

# unpack singularity
tar xvf singularity-${VERSION}.tar.gz

# configure singularity
./configure --prefix=/usr/local

# make singularity
make

# install singularity
make install

# remove singularity tarball
rm -f singularity-${VERSION}.tar.gz 