#!/bin/bash

bash <( curl https://get.docker.com/ )

usermod -aG docker ubuntu
