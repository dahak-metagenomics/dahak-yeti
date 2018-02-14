# dahak yeti scripts

This contains scripts to prepare for Dahak workflows.

Run scripts in the following order:



**General stuff:**

`install_pyenv.sh` - installs pyenv for control over python verison.

`install_snakemake.sh` - installs snakemake using miniconda.

`install_singularity.sh` - installs singularity



**Taxonomic classification:**

`prepare_biocontainers.sh` - download Docker containers from biocontainers

`get_sbt.sh` - get sequence bloom trees for microbial genomes

`get_trimmed_data.sh` - get trimmed data from OSF from URLs in `trimmed_data.dat`

`calculate_signatures.sh` - run sourmash biocontainer to compute signatures

