#!/usr/bin/env python3
import getpass
import os, sys
import subprocess


def install_singularity_the_slightly_easier_way():
    user = getpass.getuser()
    if(user!="root"):
        raise Exception("You are not root - this script requires root (or write access to /usr/local).")
    else:

        print("Installing singularity...")
        

        #############################
        # Prerequisites
        
        print(" - installing libarchive-devel")
        aptlibarchive = ["apt-get","install","-y","libarchive-dev"]
        keyupdateproc = subprocess.call(aptlibarchive)
        

        #############################
        # Singularity
        
        version = "2.5.1"
        
        print(" - downloading singularity")
        tarurl = "https://github.com/singularityware/singularity/releases/download/{version}/singularity-{version}.tar.gz".format(version=version)
        wgetcmd = ["wget",tarurl]
        subprocess.call(wgetcmd)

        print(" - unpacking singularity")
        tarcmd = ["tar","xvf","singularity-{version}.tar.gz".format(version=version)]
        subprocess.call(tarcmd)
        
        print(" - configuring singularity")
        singularity_dir = "singularity-{version}".format(version=version)
        configurecmd = ["./configure","--prefix=/usr/local"]
        subprocess.call(configurecmd, cwd=singularity_dir)
        
        print(" - making singularity")
        makecmd = ["make"]
        subprocess.call(makecmd, cwd=singularity_dir)

        print(" - installing singularity")
        makeinstallcmd = ["make","install"]
        subprocess.call(makeinstallcmd, cwd=singularity_dir)

        print(" - removing singularity")
        rmtar = ["rm","-rf","singularity-{version}.tar.gz".format(version=version)]
        subprocess.call(rmtar)
        rmdir = ["rm","-rf","singularity-{version}".format(version=version)]
        subprocess.call(rmdir)

        print("     ~~*~~ ~~*~~ ~~*~~ SUCCESS! ~~*~~ ~~*~~ ~~*~~\n")
        print("     Singularity is now installed.")
        print()

if __name__=="__main__":
    install_singularity_the_slightly_easier_way()

