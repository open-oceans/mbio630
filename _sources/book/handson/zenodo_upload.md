---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Creating a Zenodo Upload

Zenodo also allows you to upload files directly for publication along with minting a DOI for your data and helping you arrange them as needed along with a lot of additional information that cannot be passed by GitHub integration directly.

```{note}
 * Github integration based Zenodo uploads can be modified and these additional fields can be added.
 * Zenodo has a file count limit of 100 per upload but with a much larger file size limit of 50GB per upload.
```

## File uploads

One of the easiest things to do with Zenodo uploads if you can might be to zip the files into a single file. While this is not necessary this allows you to overcome the 100 file limitation since you can zip hundreds of files into a single zip file. This is not necessary and if you want your users to be able to actually preview contents without downloading them then single file uploads are perfectly fine.

## Steps to upload

Here's a breakdown of the steps involved in uploading files to zenodo

1. **Prepare Your Dataset:**
   Ensure that your dataset is properly organized and contains all the necessary files and metadata that you want to associate with the DOI. This may include data files, documentation, code, and any relevant metadata files.

2. **Create a Zenodo Account:**
   If you don't already have one, sign up for a Zenodo account at [Zenodo.org](https://zenodo.org/).

3. **Create a New Deposit:**
   - Log in to your Zenodo account.
   - Click on the "New Upload" button to create a new deposit.
   - Provide basic information about your dataset, such as the title, authors, and a description.

```{figure} images/zenodo-manual.gif
---
name: Uploading a zenodo dataset
width: 100%
---
Let's upload some files directly to zenodo
```

4. **Upload Your Dataset:**
   - Add your dataset files by clicking the "Upload" button.
   - You can upload files individually or as a zip archive.
   - Fill in the metadata for each file, including the file name, description, and file type.

5. **Complete Dataset Metadata:**
   - Fill out the metadata for your dataset, including the community (related field of research), keywords, and license.
   - Make sure to add relevant information about your dataset to make it discoverable and understandable.

6. **Create a New Version:**
   - If you make updates to your dataset in the future, you can create a new version of your deposit.
   - Each version will have a unique DOI.

7. **Publish Your Deposit:**
   - Review the information you've provided for accuracy.
   - Click the "Publish" button to make your dataset publicly accessible on Zenodo.

8. **Obtain the DOI:**
   - After publishing, Zenodo will mint a DOI for your dataset.
   - You can find the DOI on the dataset's Zenodo page.
