#!/usr/bin/env python3
import subprocess

print("")
print("Installing conda...")
mc = subprocess.Popen(["pyenv","install","miniconda3-4.3.30"], stdout=subprocess.PIPE)
print(mc.stdout().read())
print("Done installing conda.")
print("")
