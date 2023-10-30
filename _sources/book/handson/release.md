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

# Release & Cite

Synchronizing your GitHub repository with Zenodo enables you to generate a new Zenodo release with a newly minted DOI and citation each time you create a GitHub release. This process is made possible through the use of webhooks, which act as triggers for automating Zenodo records. This automation is highly advantageous when you want your releases to be published as Zenodo records automatically.

```{figure} images/create-release.gif
---
name: creating a release
width: 90%
---
Now let's create a GitHub release
```

GitHub releases are specific and delibrate and are different than commits.

```{note}
 Webhooks are triggered only once with Zenodo, meaning once created Zenodo releases will not automatically get updated if you update your GitHub release. However you can edit Zenodo releases to some degree.
```

## Zenodo release

There are two ways to create a zenodo release or a zenodo object. The one below is a walkthrough of the automated release and fetching your citation and DOI information.
* Use a Github Release to created a Zenodo release (this one is automatic)
* Upload files directly to Zenodo as a repository. (this one is manual)

```{figure} images/zenodo-release.gif
---
name: creating a zenodo release
width: 90%
---
Zenodo release
```
