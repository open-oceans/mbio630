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

# Getting Started
This portion of the module will walk you through getting started with bringing your own data and uploading it into a FAIR complaint data repository. We will work with the following steps
* Setting up a Zenodo account
* Linking your Github account to Zenodo
* Creating a data repository and uploading data
* Creating a Zenodo release and minting DOI
* Uploading directly to Zenodo

## Setting up a Zenodo account
Although having a GitHub account is not mandatory for Zenodo usage, we'll demonstrate how to automate the creation of your data releases and acquire
your DOI and data citation information by using one. Linking your GitHub account to Zenodo is an optional step, and your use of Zenodo can proceed
without it, depending on your specific requirements and preferences.

```{figure} images/zenodo_signup.gif
---
name: zenodo_login
width: 90%
---
Logging into your Github repository and linking it to Zenodo
```


```{note}
 Some things to consider
```

- While I recommend using a GitHub account for sharing code and certain data, please be aware of file size limitations, typically capped around 100
MB. For larger files, consider breaking them into smaller segments. Additionally, the maximum size for a repository varies, generally ranging from 1
to 5 GB. However, this process is more automated, with most information flowing seamlessly from GitHub to Zenodo.

- To overcome these size constraints, I will also guide you on how to establish a data repository directly in Zenodo. Here, each file can be as
large as 50 GB, and there are virtually no limitations on the total number of files you can upload per release. This approach offers a higher degree
of manual control over data organization, which some users may find advantageous.
