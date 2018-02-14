#!/bin/bash
#
# Runs sourmash using the data downloaded from OSF

for filename in *_1.trim2.fq.gz
do
    #Remove _1.trim.fq from file name to create base
    base=$(basename $filename _1.trim2.fq.gz)
    echo $base

    docker run \
        sourmash compute \
            quay.io/biocontainers/sourmash:2.0.0a2--py36_0 \
            -v ${PWD}:/data \
            --merge /data/${base}.trim2.fq.gz \
            --track-abundance \
            --scaled 10000 -k 21,31,51 \
            /data/${base}_1.trim2.fq.gz \
            /data/${base}_2.trim2.fq.gz \
            -o /data/${base}.trim2.scaled10k.k21_31_51.sig
done

for filename in *_1.trim30.fq.gz
do
    #Remove _1.trim.fq from file name to create base
    base=$(basename $filename _1.trim30.fq.gz)
    echo $base

    docker run \
        sourmash compute \
        quay.io/biocontainers/sourmash:2.0.0a2--py36_0 \
        -v ${PWD}:/data \
        --merge /data/${base}.trim.fq.gz \ 
        --track-abundance \
        --scaled 10000 -k 21,31,51 \ 
        /data/${base}_1.trim30.fq.gz /data/${base}_2.trim30.fq.gz \
        -o /data/${base}.trim30.scaled10k.k21_31_51.sig
done

