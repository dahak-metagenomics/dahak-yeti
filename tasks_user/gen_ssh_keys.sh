#!/bin/bash
#
# create ssh keys for the user in $HOME/.ssh/id_rsa

ssh-keygen -t rsa -N '' -b 4096 -f $HOME/.ssh/id_rsa -C "charlesreid1@gmail.com"
chmod 700 $HOME/.ssh
touch $HOME/.ssh/authorized_keys
chmod 600 $HOME/.ssh/authorized_keys

