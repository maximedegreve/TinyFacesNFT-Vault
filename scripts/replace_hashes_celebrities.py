#!/usr/bin/env python
import os
from os.path import dirname, abspath

d = dirname(abspath(__file__))
meta_temp = d + "/tiny_celebrities_meta_temp"
meta_final = d + "/tiny_celebrities_meta"

hash = input("🙋🏻‍♂️ Enter the hash of the IPFS celebrities images folder: ")

for filename in os.listdir(meta_temp):
    if filename.endswith(".json"):
        file = open(os.path.join(meta_temp, filename))
        contents = file.read()
        replaced_contents = contents.replace("<hash>", hash)
        replaced_contents_png = replaced_contents.replace(".png", ".jpeg")
        with open(meta_final + "/" + filename, "w") as f:
            f.write(replaced_contents_png)