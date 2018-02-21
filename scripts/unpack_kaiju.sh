#!/bin/bash
# 
# Unpack the tgz files from/for kaiju steps

kaijudir="${PWD}/kaijudb"
tarfile="kaiju_index_nr_euk.tgz"

mkdir ${kaijudir}
curl -LO "http://kaiju.binf.ku.dk/database/${tarfile}"
tar xzf ${tarfile}
rm -f ${tarfile}

