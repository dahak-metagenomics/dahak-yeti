#!/usr/bin/python
import subprocess

with open('trimmed_data.dat','r') as f:
    lines = f.readlines()

for ln in lines:
    line = ln.split()
    cmd = ["wget",line[1],"-O",line[0]]
    print("Calling command %s"%(" ".join(cmd)))
    subprocess.call(cmd)

