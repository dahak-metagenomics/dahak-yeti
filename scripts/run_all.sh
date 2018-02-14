#!/bin/bash

sudo ./install_singularity.sh 

./install_pyenv.sh

./install_snakemake 

./prepare_biocontainers.sh

./get_sbt.sh

./get_trimmed_data.sh

./calculate_signatures.sh

