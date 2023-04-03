#!/usr/bin/env python
import os
from os.path import dirname, abspath

d = dirname(abspath(__file__))
meta_final = d + "/meta-celebrities"
meta_temp = d + "/temp"

hash = input("🙋🏻‍♂️ Enter the hash of the IPFS celebrities images: ")

for filename in os.listdir(meta_final):
    if filename.endswith(".json"):
        file = open(os.path.join(meta_final, filename))
        contents = file.read()
        replaced_contents = contents.replace("<hash>", hash)
        replaced_contents_png = replaced_contents.replace(".png", ".jpeg")
        with open(meta_temp + "/" + filename, "w") as f:
            f.write(replaced_contents_png)