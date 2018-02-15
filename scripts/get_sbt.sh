#!/bin/bash
#
# Prepare for taxonomic classification
# by downloading SBT (sequence bloom trees)
# for microbial genomes in refseq and genbank.

mkdir -p data/
cd data/

tar_files=( \
"microbe-refseq-sbt-k51-2017.05.09.tar.gz"
"microbe-refseq-sbt-k31-2017.05.09.tar.gz"
"microbe-refseq-sbt-k21-2017.05.09.tar.gz"
"microbe-genbank-sbt-k51-2017.05.09.tar.gz"
"microbe-genbank-sbt-k31-2017.05.09.tar.gz"
"microbe-genbank-sbt-k21-2017.05.09.tar.gz"
)

for tar_file in "${tar_files[@]}"
do
    curl -O https://s3-us-west-1.amazonaws.com/spacegraphcats.ucdavis.edu/${tar_file}
    tar xzf ${tar_file}
    rm -rf ${tar_file}
done

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
