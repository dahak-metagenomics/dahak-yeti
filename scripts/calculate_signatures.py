#!/usr/bin/python3
import glob, os, re

suffix1 = "_1.trim2.fq.gz"
suffix2 = "_2.trim2.fq.gz"
for filename in glob.glob("*"+suffix1):
    s = re.search("^(.*)%s"%(suffix1),filename)
    prefix = s.group(1)
    sigsuffix = ".trim2.scaled10k.k21_31_51.sig"

    if(os.path.isfile(prefix+sigsuffix)):
        print("Skipping file %s, file exists."%(prefix+sigsuffix))
    else:
        print("Running docker command")

        datadir         = "/data"
        dockercmd       = ["docker","run"]
        volume          = ["-v","%s:%s"%(os.getcwd(),datadir)]
        quay_sourmash   = ["quay.io/biocontainers/sourmash:2.0.0a3--py36_0"]
        sourmash        = ["sourmash","compute"]
        merge           = ["--merge","%s/%s.trim2.fq.gz"%(datadir,prefix)]
        flags           = ["--track-abundance"]
        scaled          = ["--scaled 10000"]
        kmers           = ["-k","21,31,,51"]
        files           = ["%s/%s_%d.trim2.fq.gz"%(datadir,prefix,i+1) for i in range(2)]
        output          = ["-o","%s/%s%s"%(datadir, prefix, sigsuffix)]



