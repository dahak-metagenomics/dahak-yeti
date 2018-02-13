# This is the bash profile.
# 
# This file sets PATH and bash options.
#
# to add your own non-committed machine-specific settings,
# use ~/.extra 

# Must
EDITOR="vim"

# Set $PATH here
#PATH="/usr/local/bin:$PATH"




# Python:
# Try not to have to deal with PYTHONPATH...

# Go
#export PATH="${HOME}/.local/bin:${PATH}"




# Bash history

HISTFILE="$HOME/.bash_history"
HISTFILESIZE=1000000000
HISTIGNORE="ls:cls:clc:clear:pwd:l:ll:[ \t]*"
HISTSIZE=1000000
HISTTIMEFORMAT=': %Y-%m-%d_%H:%M:%S; '

# Append to the Bash history file, rather than overwriting it
shopt -s histappend;
# Save Bash history 
shopt -s cmdhist;


