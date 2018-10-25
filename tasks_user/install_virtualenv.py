#!/usr/bin/env python3
import os, sys
import getpass
import tempfile
import subprocess

"""
Install Virtualenv
"""

def install_venv():
    user = getpass.getuser()

    if(user=="root"):
        raise Exception("You are root - you should run this script as a normal user.")
    else:

        print("Installing snakemake...")

        pyenvbin = os.environ['HOME']
        condabin = pyenvbin+"/.pyenv/shims/conda"
        pipbin = pyenvbin+"/.pyenv/shims/pip"

        print(" - Installing virtualenv")
        rc = subprocess.call([pipbin,"install","virtualenv"])
        if(rc != 0):
            raise Exception()


        print("     ~~*~~ ~~*~~ ~~*~~ SUCCESS! ~~*~~ ~~*~~ ~~*~~\n")
        print("     Snakemake is now installed.")
        print("     Test that snakemake is working using the following one-liner:\n")
        print("         virtualenv vp && rm -fr vp")
        print()


if __name__=="__main__":
    install_venv()

