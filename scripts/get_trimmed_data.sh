#!/bin/bash

echo "Running the following commands:"
cat trimmed_data.dat | awk '{ print "wget "$2" -O "$1;}' 

eval `cat trimmed_data.dat | awk '{ print "wget "$2" -O "$1;}'`

