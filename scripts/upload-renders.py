#!/usr/bin/env python
import os

infuraId = input("1️⃣ What's your Infura IPFS id?: ")
infuraSecret = input("2️⃣ What's your Infura IPFS secret?: ")

parent = os.path.abspath(__file__ + "/../../")
scripts_folder = parent + "/scripts"
renders = parent + "/renders"

cmd = scripts_folder + '/ipfs-upload-client --id ' + infuraId + ' --secret ' + infuraSecret + " " + renders

so = os.popen(cmd).read()

print (so)