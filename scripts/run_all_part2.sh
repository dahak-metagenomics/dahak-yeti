#!/bin/bash

./prepare_biocontainers.sh

./get_sbt.sh

./get_trimmed_data.sh

./calculate_signatures.sh

## Skipping this script
#./compare_components.sh

./unpack_run_kaiju.sh

./kaiju_to_korona.sh

./filter_taxa.sh

./visualize_korona.sh

