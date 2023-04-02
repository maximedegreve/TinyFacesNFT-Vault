# TinyFaces NFT - Vault

![Vault](https://user-images.githubusercontent.com/980622/229357697-29f8f094-1aa7-4d85-afcd-87a52ea4674b.png)

Storing copies of NFT art on GitHub is not a requirement for NFT projects, but it can be a useful tool for ensuring the authenticity and provenance of the art.

This can be especially important for NFT art that is sold or traded on the secondary market, as it can help to prevent fraudulent copies or imporsination of meta data. By referencing the GitHub repository, buyers can verify that the NFT they are purchasing is authentic and stay informed on how it's meta data changed over time.

Even though our art is currently [IPFS](https://en.wikipedia.org/wiki/InterPlanetary_File_System) pinned in a free [Infura](https://infura.io) account, storing our art on GitHub can provide a backup in case the original files are lost or damaged. It can also make it easier for developers to work with the art, as they can access and download the files directly from the repository.

It's important to note that while GitHub can provide a public record of NFT art, the history can be altered and therefore the trust still ultimately lies with the NFT project founder (@maximedegreve) who is responsible for maintaining the authenticity and provenance of their art through reviewing every change to the meta data carefully.

## 🧠 Contribute

People are free to contribute improvements to the metadata in the repository. We regularly update the contract IPFS data if the changes are reviewed and merged.

## 🚀 Get started

There are multiple folders that each have their own use case.

- `tiny_meta_temp`: Contains all files without the hash set.
- `tiny_meta`: Contains all files with the hash changed. Edits are not allowed in those files as they are auto created from the `tiny_meta_temp` files.
- `tiny_renders`: Contains all original rendered images.

## 📁 Update IPFS

If changes happened to the `tiny_meta_temp` files we need to update this within the contract with a new IPFS location.

This is currently only can be done by people who have access to the contract wallet.

**🖼️ Update the art (optional):**

1. Run `python3 ./scripts/upload_renders.py`
1. Save the returned id somewhere

**💿 Update the meta data (optional):**

1. Run `python3 ./scripts/upload_meta.py`
1. Save the returned id somewhere
