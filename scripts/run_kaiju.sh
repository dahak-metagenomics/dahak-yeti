#!/bin/bash

for filename in *1.trim2.fq.gz
do
    #Remove _1.trim2.fq from file name to create base
    base=$(basename $filename _1.trim2.fq.gz)
    echo $base

    docker run -v ${PWD}:/data quay.io/biocontainers/kaiju:1.5.0--pl5.22.0_0 kaiju \
        -x \
        -v \
        -t /data/kaijudb/nodes.dmp \
        -f /data/kaijudb/kaiju_db_nr_euk.fmi \
        -i /data/${base}_1.trim2.fq.gz \
        -j /data/${base}_2.trim2.fq.gz \
        -z 4

        #-o /data/${base}.kaiju_output.trim2.out \

    exit 1;

done

for filename in *1.trim30.fq.gz
do
    #Remove _1.trim30.fq from file name to create base
    base=$(basename $filename _1.trim30.fq.gz)
    echo $base

    docker run -v ${PWD}:/data quay.io/biocontainers/kaiju:1.5.0--pl5.22.0_0 kaiju \
        -x \
        -v \
        -t /data/kaijudb/nodes.dmp \
        -f data/kaijudb/kaiju_db_nr_euk.fmi \
        -i /data/${base}_1.trim30.fq.gz \
        -j /data/${base}_2.trim30.fq.gz \
        -o /data/${base}.kaiju_output.trim30.out \
        -z 4
done

