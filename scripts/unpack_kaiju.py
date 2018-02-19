#!/usr/bin/python3
import os
import subprocess

pwd = os.getcwd()
kaijudir = pwd+"/kaijudirb"
tarfile = "kaiju_index_nr_euk.tgz"
url = "http://kaiju.binf.ku.dk/database/kaiju_index_nr_euk.tgz"

subprocess.call(["mkdir",kaijudir])
subprocess.call(["curl","-LO",url], cwd=kaijudir)
subprocess.call(["tar","zxvf",tarfile], cwd=kaijudir)
subprocess.call(["rm","-f",tarfile], cwd=kaijudir)

