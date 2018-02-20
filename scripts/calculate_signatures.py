#!/usr/bin/python3
import glob, os, re


def get_prefix(filename,suffix):
    """
    Strip the suffix from a filename
    """
    s = re.search("^(.*)%s"%(suffix1),filename)
    prefix = s.group(1)
    return prefix


def calc_signatures():
    """
    Calculate signatures using sourmash
    """
    suffix1 = "_1.trim2.fq.gz"
    #suffix2 = "_2.trim2.fq.gz"
    sigsuffix = ".trim2.scaled10k.k21_31_51.sig"
    for filename in glob.glob("*"+suffix1):
        prefix = get_prefix(filename,suffix1)
        targetfile = prefix+sigsuffix 
        if(os.path.isfile(targetfile)):
            print("Skipping file %s, file exists."%(targetfile))
        else:
            datadir = "/data"
            pwd = os.getcwd()

            cmd = ["docker","run"]
            cmd += ["-v","%s:%s"%(pwd,datadir)]
            cmd += ["quay.io/biocontainers/sourmash:2.0.0a3--py36_0"]
            cmd += ["sourmash","compute"]
            cmd += ["--merge","%s/%s.trim2.fq.gz"%(datadir,prefix)]
            cmd += ["--track-abundance"]
            cmd += ["--scaled 10000"]
            cmd += ["-k","21,31,,51"]
            cmd += ["%s/%s_%d.trim2.fq.gz"%(datadir,prefix,i+1) for i in range(2)]
            cmd += ["-o","%s/%s"%(datadir, targetfile)]

            print("Running this docker command from dir %s:"%(pwd))
            print(cmd)
            print()
    
            subprocess.call(cmd, cwd=pwd)

if __name__=="__main__":
    calc_signatures()

