#!/bin/bash

# Convert kaiju file to format readable by krona:

kaijuurl="quay.io/biocontainers/kaiju:1.6.1--pl5.22.0_0"
kaijudir="kaijudb"
for i in *trim{"2","30"}.out
do
    docker run \
        -v ${PWD}:/data \
        ${kaijuurl} \
        kaiju2krona \
        -v \
        -t \
        /data/${kaijudir}/nodes.dmp \
        -n /data/${kaijudir}/names.dmp \
        -i /data/${i} \
        -o /data/${i}.kaiju.out.krona
done

for i in *trim{"2","30"}.out
do
    docker run \
        -v ${PWD}:/data \
        ${kaijuurl} \
        kaijuReport \
        -v \
        -t \
        /data/${kaijudir}/nodes.dmp \
        -n /data/${kaijudir}/names.dmp \
        -i /data/${i} \
        -r genus \
        -o /data/${i}.kaiju_out_krona.summary 
done

