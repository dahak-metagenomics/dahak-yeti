#!/bin/bash
#
# Runs sourmash using the data downloaded from OSF

for filename in *_1.trim2.fq.gz
do
    #Remove _1.trim.fq from file name to create base
    base=$(basename $filename _1.trim2.fq.gz)
    sigsuffix=".trim2.scaled10k.k21_31_51.sig"
    echo $base

    if [ -f ${base}${sigsuffix} ]
    then
        # skip
        echo "Skipping file ${base}${sigsuffix}, file exists."
    else
        echo "Okay I'm gonna run Docker now"

        docker run -v ${PWD}:/data quay.io/biocontainers/sourmash:2.0.0a3--py36_0 sourmash compute \
                --merge /data/${base}.trim2.fq.gz \
                --track-abundance \
                --scaled 10000 \
                -k 21,31,51 \
                /data/${base}_1.trim2.fq.gz \
                /data/${base}_2.trim2.fq.gz \
                -o /data/${base}${sigsuffix}
    fi
done

for filename in *_1.trim30.fq.gz
do
    #Remove _1.trim.fq from file name to create base
    base=$(basename $filename _1.trim30.fq.gz)
    sigsuffix=".trim30.scaled10k.k21_31_51.sig"
    echo $base

    if [ -f ${base}${sigsuffix} ]
    then
        # skip
        echo "Skipping file ${base}${sigsuffix}, file exists."
    else
        echo "Okay I'm gonna run Docker now"

        docker run -v ${PWD}:/data quay.io/biocontainers/sourmash:2.0.0a3--py36_0 sourmash compute \
            --merge /data/${base}.trim30.fq.gz \
            --track-abundance \
            --scaled 10000 \
            -k 21,31,51 \
            /data/${base}_1.trim30.fq.gz \
            /data/${base}_2.trim30.fq.gz \
            -o /data/${base}${sigsuffix}
    fi
done

