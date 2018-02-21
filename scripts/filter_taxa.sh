#!/bin/bash

# Now let's filter out taxa with low abundances by obtaining genera that comprise at least 1 percent of the total reads:

for i in *trim{"2","30"}.out
do
    docker run -v /home/ubuntu/data:/data quay.io/biocontainers/kaiju:1.6.1--pl5.22.0_0 \
        kaijuReport 
        -v \
        -t /data/kaijudb/nodes.dmp \
        -n /data/kaijudb/names.dmp \
        -i /data/${i} \
        -r genus \
        -m 1 \
        -o /data/${i}.kaiju_out_krona.1percenttotal.summary
done

# Now for comparison, let's take the genera that comprise at least 1 percent of all of the classified reads:

for i in *trim{"2","30"}.out
do
    docker run -v /home/ubuntu/data:/data quay.io/biocontainers/kaiju:1.6.1--pl5.22.0_0 \
        kaijuReport \
        -v \
        -t /data/kaijudb/nodes.dmp \
        -n /data/kaijudb/names.dmp \
        -i /data/${i} \
        -r genus \
        -m 1 \
        -u \
        -o /data/${i}.kaiju_out_krona.1percentclassified.summary
done

