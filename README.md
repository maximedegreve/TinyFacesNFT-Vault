# TinyFaces NFT - Vault

![Vault](https://user-images.githubusercontent.com/980622/229357697-29f8f094-1aa7-4d85-afcd-87a52ea4674b.png)

Storing copies of NFT art on GitHub is not a requirement for NFT projects, but it can be a useful tool for ensuring the authenticity and provenance of the art.

This can be especially important for NFT art that is sold or traded on the secondary market, as it can help to prevent fraudulent copies or imporsination of meta data. By referencing the GitHub repository, buyers can verify that the NFT they are purchasing is authentic and stay informed on how it's meta data changed over time.

Even though our art is currently [IPFS](https://en.wikipedia.org/wiki/InterPlanetary_File_System) pinned in a free [Infura](https://infura.io) account, storing our art on GitHub can provide a backup in case the original files are lost or damaged. It can also make it easier for developers to work with the art, as they can access and download the files directly from the repository.

It's important to note that while GitHub can provide a public record of our NFT art, the history can be altered and therefore the trust still ultimately lies with the NFT project founder (@maximedegreve) who is responsible for maintaining the authenticity and provenance of the art. This is done through reviewing every change to the meta data carefully before it gets merged on GitHub.

## 🧠 Contribute

People are free to contribute improvements to the metadata in the `meta-originals` and `meta-celebrities` folder. We regularly update the blockchain contract with the new IPFS identifier if the changes are reviewed, approved and merged.

## 🚀 Get started

There are multiple folders that each have their own use case.

- `meta-originals`: Contains all the meta for the [original collection](https://opensea.io/collection/tinyfacesofficial).
- `meta-celebrities`: Contains all the meta for the [celebrities collection](https://opensea.io/collection/tinyfacesofficial-celebrities).
- `renders`: Blender exported images from our [original collection](https://opensea.io/collection/tinyfacesofficial). Includes a transparent version as well. Is also used for our [wallpaper download](https://nft.tinyfac.es/yearbook) service.
- `renders-celebrities`: Blender exported images from our [celebrities collection](https://opensea.io/collection/tinyfacesofficial-celebrities). Includes a transparent version as well.
- `renders-downsized`: Downsized versions of the `renders`. Those are stored on IPFS. We don't use the original files as this would make it too expensive to pin on a IPFS service and too heavy to process by secondary marketplaces.
- `renders-downsized-celebrities`: Downsized versions of the `renders-celebrities`. Those are stored on IPFS. We don't use the original files as this would make it too expensive to pin on a IPFS service.

⚠️ This repository is over 50GB large therefore cloning could take a while.

## 📁 Update IPFS

If changes happened to the `meta-originals` or `meta-celebrities` files we need to update this within the [contract](https://etherscan.io/address/0xb363af6181a4335608880510772a5f61a5183c88) with a new IPFS location.

This is currently only can be done by people who have access to the contract wallet.

**🖼️ Update the art (optional):**

1. Using Terminal`cd` in the root folder
2. Run `python3 ./scripts/upload_renders.py`
3. Save the returned id to use in the next step

**💿 Update the meta data:**

1. Using Terminal`cd` in the root folder
2. Run `python3 ./scripts/upload_meta.py`
3. Save the returned id to save `ipfs://id/` to the contract

## 🤯 Upload bulk files

In rare cases where we want to update 4000+ large image files it can get tricky to upload those as one batch to GitHub.

We've created a small script that can automatically commit and push those files one by one for you. That way it's less likely pushing will timeout.

1. Using Terminal`cd` in the root folder
2. Make sure you're on the expected git branch.
3. Run `python3 ./scripts/bulk_git.py`
