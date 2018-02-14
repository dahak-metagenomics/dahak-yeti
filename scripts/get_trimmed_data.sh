#!/bin/bash
#
# Runs a series of wget commands to download data from OSF

echo "Running the following commands:"
cat trimmed_data.dat | awk '{ print "wget "$2" -O "$1;}' 

eval `cat trimmed_data.dat | awk '{ print "wget "$2" -O "$1;}'`
