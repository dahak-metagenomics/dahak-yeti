#!/usr/bin/env python3
import getpass
import os, sys
import subprocess

FNULL = open(os.devnull, 'w')

def install_singularity_the_slightly_easier_way():
    user = getpass.getuser()
    if(user!="root"):
        raise Exception("You are not root - this script requires root (apt-get commands).")
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

        tarcmd = ["tar","xvf","singularity-{version}.tar.gz".format(version=version)]
        subprocess.call(tarcmd)
        
        singularity_dir = "singularity-{version}".format(version=version)
        configurecmd = ["./configure","--prefix=/usr/local"]
        subprocess.call(configurecmd, cwd=singularity_dir)
        
        makecmd = ["make"]
        subprocess.call(makecmd, cwd=singularity_dir)
        
        makeinstallcmd = ["make","install"]
        subprocess.call(makeinstallcmd, cwd=singularity_dir)



def install_singularity():
    user = getpass.getuser()
    if(user!="root"):
        raise Exception("You are not root - this script requires root (apt-get commands).")
    else:

        print("Installing singularity...")

        # -----------------------
        # Parameters:

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
    install_singularity_the_slightly_easier_way()

