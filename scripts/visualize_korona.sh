#!/bin/bash
# 
# Download the krona image from quay.io so we can visualize the results from kaiju:
docker pull quay.io/biocontainers/krona:2.7--pl5.22.0_1

# Generate krona html with output from all of the reads:

for i in *kaiju_out_krona.summary
do
        docker run -v /home/ubuntu/data:/data quay.io/biocontainers/krona:2.7--pl5.22.0_1 ktImportText -o \
        /data/${i}.kaiju_out_krona.all.html /data/${i}
done

# Generate krona html with output from genera at least 1 percent of the total reads:

for i in *kaiju_out_krona.1percenttotal.summary
do
        docker run -v /home/ubuntu/data:/data quay.io/biocontainers/krona:2.7--pl5.22.0_1 ktImportText -o \
        /data/${i}.kaiju_out_krona.1percenttotal.html /data/${i}
done


# Generate krona html with output from genera at least 1 percent of all classified reads:

for i in *kaiju_out_krona.1percentclassified.summary
do
        docker run -v /home/ubuntu/data:/data quay.io/biocontainers/krona:2.7--pl5.22.0_1 ktImportText -o \
        /data/${i}.kaiju_out_krona.1percentclassified.html /data/${i}
done

