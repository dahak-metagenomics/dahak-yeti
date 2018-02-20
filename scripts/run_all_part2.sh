#!/bin/bash

./prepare_biocontainers.py

./get_sbt.py

./get_trimmed_data.py

./calculate_signatures.py

## Skipping this script
#./compare_components.sh

./unpack_kaiju.py

./run_kaiju.py

./kaiju2krona.py

./filter_taxa.py

./visualize_korona.py

