#!/usr/bin/env python
import os

parent = os.path.abspath(__file__ + "/../../")
meta_final = parent + "/meta"
meta_temp = parent + "/meta-temp"

hash = input("🙋🏻‍♂️ Enter the hash of the IPFS celebrities images: ")

if not os.path.exists(meta_temp):
    os.makedirs(meta_temp)

for filename in os.listdir(meta_final):
    if filename.endswith(".json"):
        file = open(os.path.join(meta_final, filename))
        contents = file.read()
        replaced_contents = contents.replace("<hash>", hash)
        replaced_contents_png = replaced_contents.replace(".png", ".jpeg")
        with open(meta_temp + "/" + filename, "w") as f:
            f.write(replaced_contents_png)