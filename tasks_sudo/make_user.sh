#!/bin/bash
#
# make a new user
# and set them up
#
if [ "$(id -u)" != "0" ]; then
    echo ""
    echo ""
    echo "This script should be run as root."
    echo ""
    echo ""
    exit 1;
fi

set -x

REGUSER="florence"

mkdir /home/florence

useradd -s /bin/bash -d /home/$REGUSER $REGUSER
usermod -a -G ubuntu $REGUSER
usermod -a -G sudo $REGUSER

# copy the user init script
wget https://raw.githubusercontent.com/dahak-metagenomics/dahak-yeti/master/tasks_user/user_init.sh -O /home/$REGUSER/user_init.sh
chown $REGUSER:$REGUSER /home/$REGUSER/user_init.sh
chmod gu+x /home/$REGUSER/user_init.sh

# run user init script as user
sudo -H -i -u $REGUSER /home/$REGUSER/user_init.sh

set +x
