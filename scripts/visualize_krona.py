#!/usr/bin/python3
import glob, os, re
import subprocess
from get_prefix import get_prefix


def pull_krona():
    # Download the krona image from quay.io so we can visualize the results from kaiju:
    kronaurl = "quay.io/biocontainers/krona:2.7--pl5.22.0_1"
    subprocess.call(["docker","pull",kronaurl])


def visualize_krona():
    kaijudirname = "kaijudb"
    cases = ["kaiju_out_krona",
             "kaiju_out_krona.1percenttotal",
             "kaiju_out_krona.1percentclassified"]

    for case in cases:

        suffix = case + ".summary"
        htmlsuffix = case + ".html"

        filenames = glob.glob("*"+suffix)

        for filename in filenames:

            prefix = get_prefix(filename,suffix)

            htmlname = prefix + htmlsuffix

            if(os.path.isfile(htmlname)):
                print("Skipping file %s, file exists."%(htmlname))
            else:

                datadir = "/data"
                pwd = os.getcwd()

                cmd =  ["docker","run"]
                cmd += ["-v","%s:%s"%(pwd,datadir)]
                cmd += ["quay.io/biocontainers/krona:2.7--pl5.22.0_1"]
                cmd += ["ktImportText"]
                cmd += ["-o","%s/%s"%(datadir,htmlname)]
                cmd += ["%s/%s"%(datadir,filename)]

                print("Running this docker command from dir %s:"%(pwd))
                print(" ".join(cmd))
                print()

                subprocess.call(cmd, cwd=pwd)


if __name__=="__main__":
    pull_krona()
    visualize_krona()

