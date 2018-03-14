#!/bin/bash
# 
# make a unix user dahak

if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

groupadd dahak
sudo su -c "useradd dahak -s /bin/bash -m -g dahak -G sudo"
chpasswd << 'END'
dahak:m3t4g3n0m1c5
END

mkdir /home/dahak/.ssh
chmod 700 /home/dahak/.ssh
touch /home/dahak/.ssh/authorized_keys
chmod 600 /home/dahak/.ssh/authorized_keys

# This is a good place to hard code any public keys
