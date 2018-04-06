#!/usr/bin/env python3
import subprocess

print("")
print("Installing conda...")
mc = subprocess.call(["pyenv","install","miniconda3-4.3.30"])
print("Done installing conda.")
print("")
