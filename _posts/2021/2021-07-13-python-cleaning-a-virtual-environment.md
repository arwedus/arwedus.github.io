---
title: "Python: Cleaning a virtual environment"
date: "2021-07-13"
categories:
  - "python"
layout: post
lang: en
---

If you want to test whether a requirements.txt installs all packages required to run your python application, and you have experimented with the virtual environment before (installed some extra packages etc.), you want to remove all packages and keep only those a the requirements.txt would install. Two solutions come to my mind:

1. Delete the virtual environment and create it again.
2. Remove all packages installed into the virtual environment:

    `pip freeze | xargs pip uninstall -y Then install all packages from the requirements.txt again: pip install -r requirements.txt`
