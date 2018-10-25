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

USERNAME="matomo"

sudo mkdir -p /home/${USERNAME}

sudo useradd -s /bin/bash -d /home/$USERNAME $USERNAME
sudo usermod -a -G ubuntu $USERNAME
sudo usermod -a -G sudo $USERNAME

echo "${REGUSER} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${REGUSER}

# copy the user init script
sudo wget https://raw.githubusercontent.com/dahak-metagenomics/dahak-yeti/master/tasks_user/user_init.sh -O /home/$USERNAME/user_init.sh
sudo chown -R ${USERNAME}:${USERNAME} /home/${USERNAME}
sudo chmod gu+x /home/$USERNAME/user_init.sh

# run user init script as user
sudo -H -i -u $USERNAME /home/$USERNAME/user_init.sh

# addd to sudoers
sudo echo "${USERNAME} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${USERNAME}

set +x
