#!/bin/bash

mkdir -p /tmp/data
cd /tmp/data

curl -O https://s3-us-west-1.amazonaws.com/spacegraphcats.ucdavis.edu/microbe-refseq-sbt-k51-2017.05.09.tar.gz
curl -O https://s3-us-west-1.amazonaws.com/spacegraphcats.ucdavis.edu/microbe-refseq-sbt-k31-2017.05.09.tar.gz
curl -O https://s3-us-west-1.amazonaws.com/spacegraphcats.ucdavis.edu/microbe-refseq-sbt-k21-2017.05.09.tar.gz
curl -O https://s3-us-west-1.amazonaws.com/spacegraphcats.ucdavis.edu/microbe-genbank-sbt-k51-2017.05.09.tar.gz
curl -O https://s3-us-west-1.amazonaws.com/spacegraphcats.ucdavis.edu/microbe-genbank-sbt-k31-2017.05.09.tar.gz
curl -O https://s3-us-west-1.amazonaws.com/spacegraphcats.ucdavis.edu/microbe-genbank-sbt-k21-2017.05.09.tar.gz

tar xzf microbe-refseq-sbt-k51-2017.05.09.tar.gz
tar xzf microbe-refseq-sbt-k31-2017.05.09.tar.gz
tar xzf microbe-refseq-sbt-k21-2017.05.09.tar.gz
tar xzf microbe-genbank-sbt-k51-2017.05.09.tar.gz
tar xzf microbe-genbank-sbt-k31-2017.05.09.tar.gz
tar xzf microbe-genbank-sbt-k21-2017.05.09.tar.gz

rm -r microbe-refseq-sbt-k51-2017.05.09.tar.gz
rm -r microbe-refseq-sbt-k31-2017.05.09.tar.gz
rm -r microbe-refseq-sbt-k21-2017.05.09.tar.gz
rm -r microbe-genbank-sbt-k51-2017.05.09.tar.gz

./get_trimmed_data.sh

