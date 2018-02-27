#!/usr/bin/python3
import os
import subprocess

quayurls = [ "quay.io/biocontainers/sourmash:2.0.0a3--py36_0",
             "quay.io/biocontainers/krona:2.7--pl5.22.0_1",
             "quay.io/biocontainers/kaiju:1.6.1--pl5.22.0_0"]

pwd = os.getcwd()
for quayurl in quayurls:
    subprocess.call(["docker","pull",quayurl], cwd=pwd)

