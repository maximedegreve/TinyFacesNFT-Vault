# TinyFaces NFT - Locker Room

This is meant to track changes to our metadata and artwork if something goes wrong. If you own a TinyFaces token you can compare it with the temp meta in this repository to confirm your meta data wasn't changed in a malicious way by anyone.

tiny_meta_temp: Contains all files without the hash set.

tiny_meta: Contains all files with the hash changed.

tiny_renders: Contains all original rendered images.

./ipfs-upload-client --id ID --secret SECRET ./tiny_celebrities_renders

python3 ./replace_hashes_celebrities.py

./ipfs-upload-client --id ID --secret SECRET ./tiny_celebrities_meta
