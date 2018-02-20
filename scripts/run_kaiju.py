#!/usr/bin/python3
import glob, os, re
import subprocess


def get_prefix(filename,suffix):
    """
    Strip the suffix from a filename
    """
    s = re.search("^(.*)%s"%(suffix),filename)
    prefix = s.group(1)
    return prefix


def run_kaiju():
    """
    Run kaiju on the sourmash signatures
    """
    kaijudirname = "kaijudb"

    suffixes = [("_1.trim2.fq.gz", "_2.trim2.fq.gz", ".kaiju_output.trim2.out"),
                ("_1.trim30.fq.gz","_2.trim30.fq.gz",".kaiju_output.trim30.out")]

    for (suffix1, suffix2, kaijusuffix) in suffixes:

        for filename in glob.glob("*"+suffix1):
            prefix = get_prefix(filename,suffix1)
            targetfile = prefix+kaijusuffix
            if(os.path.isfile(targetfile)):
                print("Skipping file %s, file exists."%(targetfile))
            else:
                datadir = "/data"
                pwd = os.getcwd()

                cmd = ["docker","run"]
                cmd += ["-v","%s:%s"%(pwd,datadir)]
                cmd += ["quay.io/biocontainers/kaiju:1.6.1--pl5.22.0_0"]
                cmd += ["kaiju"]
                cmd += ["-x","-v"]
                cmd += ["-t","%s/%s/nodes.dmp"%(datadir,kaijudirname)]
                cmd += ["-f","%s/%s/kaiju_db_nr_euk.fmi"%(datadir,kaijudirname)]
                cmd += ["-i","%s/%s%s"%(datadir,prefix,suffix1)]
                cmd += ["-j","%s/%s%s"%(datadir,prefix,suffix2)]
                cmd += ["-o","%s/%s"%(datadir,targetfile)]

                print("Running this docker command from dir %s:"%(pwd))
                print(" ".join(cmd))
                print()

                subprocess.call(cmd, cwd=pwd)


if __name__=="__main__":
    run_kaiju()

