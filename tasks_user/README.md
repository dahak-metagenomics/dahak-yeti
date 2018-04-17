# user init scripts

This directory contains scripts that are called by cloud init.
They run user tasks as the ubuntu user.

Python tasks must be run in the following order:
* `install_pyenv.py` to install pyenv
* (`$HOME/.pyenv/bin` must be added to `$PATH`)
* `activate_conda.sh` to install miniconda using pyenv
* `install_snakemake.py` to install snakemake using conda

