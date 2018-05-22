#!/usr/bin/env python3
import os, sys
import getpass
import tempfile
import subprocess

"""
Install Snakemake

This script runs the necessary commands to install Snakemake.
"""

def install_snakemake():
    user = getpass.getuser()
    if(user=="root"):
        raise Exception("You are root - you should run this script as a normal user.")
    else:

        print("Installing snakemake...")

        # ---------------------------
        # Install snakemake

        pyenvbin = os.environ['HOME']
        condabin = pyenvbin+"/.pyenv/shims/conda"

        print(" - Adding channels:")

        print("     - r")
        rc = subprocess.call([condabin,"config","--add","channels","r"])
        if(rc != 0):
            raise Exception()

        print("     - default")
        rc = subprocess.call([condabin,"config","--add","channels","defaults"])
        if(rc != 0):
            raise Exception()

        print("     - conda-forge")
        rc = subprocess.call([condabin,"config","--add","channels","conda-forge"])
        if(rc != 0):
            raise Exception()

        print("     - bioconda")
        rc = subprocess.call([condabin,"config","--add","channels","bioconda"])
        if(rc != 0):
            raise Exception()

        print(" - Installing snakemake")
        condacmd = [condabin,"install","-y","-c","bioconda","-c","conda-forge","snakemake"]
        rc = subprocess.call(condacmd)
        if(rc != 0):
            raise Exception()

        pyenvbin = os.environ['HOME']
        pipbin = pyenvbin+"/.pyenv/shims/pip"

        print(" - Upgrading pip")
        rc = subprocess.call([pipbin,"install","--upgrade","pip"])
        if(rc != 0):
            raise Exception()

        print("     ~~*~~ ~~*~~ ~~*~~ SUCCESS! ~~*~~ ~~*~~ ~~*~~\n")
        print("     Snakemake is now installed.")
        print("     Test that snakemake is working using the following one-liner:\n")
        print("         python -c 'import snakemake'")
        print()


if __name__=="__main__":
    install_snakemake()

