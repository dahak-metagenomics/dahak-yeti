#!/usr/bin/python3
# 
# If you have not made trimmed data,
# you can download it.
# 
# This gets the data from OSF using
# URLs and filenames in trimmed_data.dat.

import subprocess

def get_trimmed_data():
    with open('trimmed_data.dat','r') as f:
        for ln in f.readlines():
            line = ln.split()
            cmd = ["wget",line[1],"-O",line[0]]
            print("Calling command %s"%(" ".join(cmd)))
            subprocess.call(cmd)

if __name__=="__main__":
    get_trimmed_data()
