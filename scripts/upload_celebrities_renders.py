#!/usr/bin/env python
import os

infuraId = input("1️⃣ What's your Infura IPFS id?: ")
infuraSecret = input("2️⃣ What's your Infura IPFS secret?: ")

cmd = './ipfs-upload-client --id ' + infuraId + ' --secret ' + infuraSecret + ' ./tiny_celebrities_renders'
so = os.popen(cmd).read()

print (so)