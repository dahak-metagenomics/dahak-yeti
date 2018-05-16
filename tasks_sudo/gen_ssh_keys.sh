#!/bin/bash
#
# create ssh keys for the root user in /root/.ssh/id_rsa

ssh-keygen -t rsa -N '' -b 4096 -f /root/.ssh/id_rsa -C "charlesreid1@gmail.com"
chmod 700 /root/.ssh
touch /root/.ssh/authorized_keys
chmod 600 /root/.ssh/authorized_keys

