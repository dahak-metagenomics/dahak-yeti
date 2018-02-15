#!/bin/bash

mkdir kaijudb
cd kaijudb
curl -LO http://kaiju.binf.ku.dk/database/kaiju_index_nr_euk.tgz
tar zxvf kaiju_index_nr_euk.tgz
rm -r kaiju_index_nr_euk.tgz
cd ../

