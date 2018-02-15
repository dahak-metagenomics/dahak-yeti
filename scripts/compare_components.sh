#!/bin/bash
# 
# Skipping this script for now,
# due to missing JSON files.

for kmer_len in 21 31 51
do
        for sig in *sig
        do
            docker run -v ${PWD}:/data quay.io/biocontainers/sourmash:2.0.0a2--py36_0 sourmash gather \
                    -k ${kmer_len} \
                    ${sig} \
                    genbank-k${kmer_len}.sbt.json \
                    refseq-k${kmer_len}.sbt.json \
                    -o ${sig}.k${kmer_len}.gather.output.csv \
                    --output-unassigned ${sig}.k${kmer_len}gather_unassigned.output.csv \
                    --save-matches ${sig}.k${kmer_len}.gather_matches
        done
done

