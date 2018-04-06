#!/usr/bin/env python3
import subprocess

rc = 0 # returncode

print("")
print("Installing conda...")

rc = subprocess.call(["pyenv","install","miniconda3-4.3.30"])
if(rc!=0):
    raise Exception()

rc = subprocess.call(["pyenv","global","miniconda3-4.3.30"])
if(rc!=0):
    raise Exception()

print("Done installing conda.")
print("")
