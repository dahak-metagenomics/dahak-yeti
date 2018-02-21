# dahak yeti scripts

This contains scripts to prepare for Dahak workflows.

## setup for dahak

To get dahak set up:

```
./install_pyenv.py

./install_snakemake.py

sudo ./install_singularity.py 
```

## run taxonomic classification workflow

`prepare_biocontainers.sh` - download Docker containers from biocontainers

`get_sbt.sh` - get sequence bloom trees for microbial genomes

`get_trimmed_data.sh` - get trimmed data from OSF from URLs in `trimmed_data.dat`

`calculate_signatures.sh` - run sourmash biocontainer to compute signatures

(Will take a really long time) `compare_components.sh` - 

`unpack_kaiju.py` - download and unpack tarballs from the NR Euk. database

(Will take a really long time) `run_kaiju.py` - run kaiju through docker

`kaiju2krona.py` - convert kaiju output to krona output

`filter_taxa.py` - perform the same operation as above, but filtering the taxonomies showed

`visualize_krona.py` - generate krona html output.

