#!/usr/bin/python3
import glob, os
import subprocess
from get_prefix import get_prefix


def kaiju2krona():
    """
    Convert kaiju results to krona results, 
    and generate a report.
    """
    kaijudirname = "kaijudb"
    suffixes = [".trim2.out",".trim30.out"]

    for suffix in suffixes:

        filenames = glob.glob("*"+suffix)

        for filename in filenames:

            prefix = get_prefix(filename,suffix)


            # ------------------------
            # Kaiju to krona

            #kronaoutfile = prefix + ".kaiju.out.krona"
            kronaoutfile = prefix + ".kaiju2krona.out"

            if(os.path.isfile(kronaoutfile)):
                print("Skipping file %s, file exists."%(kronaoutfile))
            else:
                datadir = "/data"
                pwd = os.getcwd()

                cmd = ["docker","run"]
                cmd += ["-v","%s:%s"%(pwd,datadir)]
                cmd += ["quay.io/biocontainers/kaiju:1.6.1--pl5.22.0_0"]
                cmd += ["kaiju2krona"]
                cmd += ["-v"]
                cmd += ["-i","%s/%s"%(datadir, filename)]
                cmd += ["-o","%s/%s"%(datadir, kronaoutfile)]
                cmd += ["-t","%s/%s/nodes.dmp"%(datadir,kaijudirname)]
                cmd += ["-n","%s/%s/names.dmp"%(datadir,kaijudirname)]

                print("Running this docker command from dir %s:"%(pwd))
                print(" ".join(cmd))
                print()

                subprocess.call(cmd, cwd=pwd)


            # ------------------------
            # Kaiju Report

            #reportoutfile = prefix + ".kaiju_out_krona.summary"
            reportutfile = prefix + ".kaiju2krona.summary"

            if(os.path.isfile(reportoutfile)):
                print("Skipping file %s, file exists."%(reportoutfile))
            else:
                datadir = "/data"
                pwd = os.getcwd()

                cmd = ["docker","run"]
                cmd += ["-v","%s:%s"%(pwd,datadir)]
                cmd += ["quay.io/biocontainers/kaiju:1.6.1--pl5.22.0_0"]
                cmd += ["kaijuReport"]
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

if __name__=="__main__":
    kaiju2krona()
