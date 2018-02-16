#!/usr/bin/python
import os
import subprocess

pwd = os.getcwd()
datadir = pwd+"/data"

subprocess.call(["mkdir","-p",datadir], cwd=pwd)

for prefix in ["refseq","genbank"]:
    for kmers in [21,31,51]:
        filename = "microbe-%s-sbt-k%d-2017.05.09.tar.gz"%(prefix,kmers)
        url = "https://s3-us-west-1.amazonaws.com/spacegraphcats.ucdavis.edu/%s"%(filename)
        subprocess.call(["curl","-O",url])


#
# The individual signatures for the above SBTs were calculated as follows:
# 
# sourmash compute -k 4,5 \
#    -n 2000 \
#    --track-abundance \
#    --name-from-first \
#    -o {output} \
#    {input}
#
#+sourmash compute -k 21,31,51 \
#     --scaled 2000 \
#     --track-abundance \
#     --name-from-first \
#     -o {output} \
#     {input}
#
