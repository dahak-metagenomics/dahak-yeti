#!/bin/bash
#
# create ssh in the default key location ~/.ssh/id_rsa
# 
# this can be run by the root user
# or by any regular user

ssh-keygen -t rsa -N '' -b 4096 -f /home/ubuntu/.ssh/id_rsa -C "charlesreid1@gmail.com"
chmod 700 $HOME/.ssh
touch $HOME/.ssh/authorized_keys
chmod 600 $HOME/.ssh/authorized_keys

