#!/usr/bin/env python3
import getpass
import os, sys
import subprocess

FNULL = open(os.devnull, 'w')

def install_singularity():
    user = getpass.getuser()
    if(user!="root"):
        raise Exception("You are not root - this script requires root (apt-get commands).")
    else:

        print("Installing singularity...")
        print("Make sure you run the install_docker.py script first.")

        # -----------------------
        # Parameters:

        # User to add to the docker group
        user = "ubuntu"

        # -----------------------
        # Install singularity:
        print(" - installing singularity aptitude sources")
        wgetproc = subprocess.call(["wget","http://neuro.debian.net/lists/xenial.us-ca.full","-O","/etc/apt/sources.list.d/neurodebian.sources.list"])

        print(" - installing singularity aptitude key")
        keyupdatecmd = ["apt-key","adv","--recv-keys","--keyserver","hkp://pool.sks-keyservers.net:80","0xA5D32F012649A5A9"]
        keyupdateproc = subprocess.call(keyupdatecmd)
        # this sometimes fails. :(
        # redirect output to string,
        # check string for "failed", 
        # retry if true

        print(" - updating aptitude repositories")
        aptupdatecmd = ["apt-get","-y","update"]
        subprocess.call(aptupdatecmd)

        print(" - installing singularity")
        aptinstallcmd = ["apt-get","-y","install"]
        subprocess.Popen(aptinstallcmd+["singularity-container"])
        # this sometimes complains
        # E: Setting in Stop via TCSAFLUSH for stdin failed! - tcsetattr (5: Input/output error)
        # E: Setting in Stop via TCSAFLUSH for stdin failed! - tcsetattr (5: Input/output error)
        
        print("     ~~*~~ ~~*~~ ~~*~~ SUCCESS! ~~*~~ ~~*~~ ~~*~~\n")
        print("     Singularity is now installed.")
        print()

if __name__=="__main__":
    install_singularity()

