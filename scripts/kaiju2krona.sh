#!/bin/bash

# Convert kaiju file to format readable by krona:

for i in *trim{"2","30"}.out
do
    docker run -v ${PWD}:/data quay.io/biocontainers/kaiju:1.6.1--pl5.22.0_0 \
            kaiju2krona \
            -v \
            -t \
            /data/kaijudb/nodes.dmp \
            -n /data/kaijudb/names.dmp \
            -i /data/${i} \
            -o /data/${i}.kaiju.out.krona
done

for i in *trim{"2","30"}.out
do
    docker run -v ${PWD}:/data quay.io/biocontainers/kaiju:1.6.1--pl5.22.0_0 \
            kaijuReport \
            -v \
            -t \
            /data/kaijudb/nodes.dmp \
            -n /data/kaijudb/names.dmp \
            -i /data/${i} \
            -r genus \
            -o /data/${i}.kaiju_out_krona.summary 
done

