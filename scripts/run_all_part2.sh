#!/bin/bash

./prepare_biocontainers.sh

./get_sbt.sh

./get_trimmed_data.py

./calculate_signatures.sh

## Skipping this script
#./compare_components.sh

./unpack_kaiju.sh

## Start from here...
#./run_kaiju.sh
#
#./kaiju_to_korona.sh
#
#./filter_taxa.sh
#
#./visualize_korona.sh
