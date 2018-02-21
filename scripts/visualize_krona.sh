#!/bin/bash

kaijudir="${PWD}/kaijudb"
kronaurl="quay.io/biocontainers/krona:2.7--pl5.22.0_1"

docker pull ${kronaurl}

suffix="kaiju_out_krona"
for i in *${suffix}.summary
do
        docker run \
            -v ${kaijudir}:/data \
            ${kronaurl} \
            ktImportText \
            -o /data/${i}.${suffix}.html \
            /data/${i}
done

suffix="kaiju_out_krona.1percenttotal"
for i in *${suffix}.summary
do
        docker run \
            -v ${kaijudir}:/data \
            ${kronaurl} \
            ktImportText \
            -o /data/${i}.${suffix}.html \
            /data/${i}
done

suffix="kaiju_out_krona.1percentclassified"
for i in *${suffix}.summary
do
        docker run \
            -v ${kaijudir}:/data \
            ${kronaurl} \
            ktImportText \
            -o /data/${i}.${suffix}.html \
            /data/${i}
done

