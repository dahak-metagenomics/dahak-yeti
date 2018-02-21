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


def filter_taxa():
    """
    Filter taxa
    """
    kaijudirname = "kaijudb"
    suffixes = [".trim2.out",".trim30.out"]

    for suffix in suffixes:

        filenames = glob.glob("*"+suffix)

        for filename in filenames:

            prefix = get_prefix(filename,suffix)

            # ------------------------
            # Kaiju report,
            # filtering taxa

            reportoutfile = prefix + ".kaiju_out_krona.1percenttotal.summary"
            classifiedreportoutfile = prefix + ".kaiju_out_krona.1percentclassified.summary"

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
                cmd += ["-m","1"]
                cmd += ["-o","%s/%s"%(datadir, reportoutfile)]

                print("Running this docker command from dir %s:"%(pwd))
                print(" ".join(cmd))
                print()

                subprocess.call(cmd, cwd=pwd)


                cmd = ["docker","run"]
                cmd += ["-v","%s:%s"%(pwd,datadir)]
                cmd += ["quay.io/biocontainers/kaiju:1.6.1--pl5.22.0_0"]
                cmd += ["kaijuReport"]
                cmd += ["-v"]
                cmd += ["-t","%s/%s/nodes.dmp"%(datadir,kaijudirname)]
                cmd += ["-n","%s/%s/names.dmp"%(datadir,kaijudirname)]
                cmd += ["-i","%s/%s"%(datadir, filename)]
                cmd += ["-r","genus"]
                cmd += ["-m","1"]
                cmd += ["-u"]
                cmd += ["-o","%s/%s"%(datadir, reportoutfile)]

                print("Running this docker command from dir %s:"%(pwd))
                print(" ".join(cmd))
                print()

                subprocess.call(cmd, cwd=pwd)



if __name__=="__main__":
    filter_taxa()

