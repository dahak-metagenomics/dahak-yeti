#!/usr/bin/python3
import glob

kmers = [21,31,51]

pwd = os.getcwd()
for kmer_len in kmers:
    for sig in glob.glob("*sig"):

        sourmashurl = "quay.io/biocontainers/sourmash:2.0.0a2--py36_0"

        cmd =  ["docker","run"]
        cmd += ["-v","%s:%s"%(pwd,datadir)]
        cmd += [sourmashurl]
        cmd += ["-k",str(kmer_len)]
        cmd += [sig]
        cmd += ["genbank-k%d.sbt.json"%(kmer_len)]
        cmd += ["refseq-k%d.sbt.json"]
        cmd += ["-o","%s.k%d.gather.output.csv"%(sig,kmer_len)]
        cmd += ["--output-unassigned","%s.k%dgather_unassigned.output.csv"%(sig,kmer_len)]
        cmd += ["--save-matches","%s.k%d.gather_matches"%(sig,kmer_len)]

        print("Running docker command from %s:"%(pwd))
        print(" ".join(cmd))

        subprocess.call(cmd, cwd=pwd)

