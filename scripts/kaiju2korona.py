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


def main():
    suffixes = [".trim2.out",".trim30.out"]

    for suffix in suffixes:

        filename = glob.glob("*"+suffix)

        prefix = get_prefix(filename,suffix)

        # ------------------------
        # Kaiju to Korona

        koronaoutfile = prefix + ".kaiju.out.korona"

        if(os.path.isfile(koronaoutfile)):
            print("Skipping file %s, file exists."%(koronaoutfile))
        else:
            datadir = "/data"
            pwd = os.getcwd()

            cmd = ["docker","run"]
            cmd += ["-v","%s:%s"%(pwd,datadir)]
            cmd += ["quay.io/biocontainers/kaiju:1.6.1--pl5.22.0_0"]
            cmd += ["kaiju2korona"]
            cmd += ["-v"]
            cmd += ["-t","%s/%s/nodes.dmp"%(datadir,kaijudirname)]
            cmd += ["-n","%s/%s/names.dmp"%(datadir,kaijudirname)]
            cmd += ["-i","%s/%s"%(datadir, filename)]
            cmd += ["-o","%s/%s"%(datadir, koronaoutfile)]

            print("Running this docker command from dir %s:"%(pwd))
            print(" ".join(cmd))
            print()

            subprocess.call(cmd, cwd=pwd)


        # ------------------------
        # Kaiju Report

        reportoutfile = prefix + ".kaiju_out_korona.summary"

        if(os.path.isfile(reportoutfile)):
            print("Skipping file %s, file exists."%(reportoutfile))
        else:
            datadir = "/data"
            pwd = os.getcwd()

            cmd = ["docker","run"]
            cmd += ["-v","%s:%s"%(pwd,datadir)]
            cmd += ["quay.io/biocontainers/kaiju:1.6.1--pl5.22.0_0"]
            cmd += ["kaiju2korona"]
            cmd += ["-v"]
            cmd += ["-t","%s/%s/nodes.dmp"%(datadir,kaijudirname)]
            cmd += ["-n","%s/%s/names.dmp"%(datadir,kaijudirname)]
            cmd += ["-i","%s/%s"%(datadir, filename)]
            cmd += ["-r","genus"]
            cmd += ["-o","%s/%s"%(datadir, reportoutfile)]

            print("Running this docker command from dir %s:"%(pwd))
            print(" ".join(cmd))
            print()

            subprocess.call(cmd, cwd=pwd)

