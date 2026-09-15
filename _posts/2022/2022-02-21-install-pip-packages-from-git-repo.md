---
title: "Install pip packages from git repo"
date: "2022-02-21"
categories: 
  - "python"
tags: 
  - "git"
layout: post
lang: en
---

* * *

Pip supports installing a python package using a link to a git repository directly. You can specify such a direct link to the package source from the pip command line or a requirements.txt file. The following article gives an overview how.

It can be handy to use pip to install a project dependency directly from a git repository instead of from a Python package index. I'll show you why you might want to do that and how to do it.

## How to pip install from a git repository

Instead of a package name, give pip a git repository URL as parameter:

```bash
# general form: pip install git+<repository_url>
# example:
pip install git+https://github.com/arwedus/some-example.git
```

If this repo does not yet contain a python package struture, you'll need to add a setup.py at least, so that pip can carry out the install (c.f. cookie-cutter).

You can explicitly call out the package name that you're installing with _#egg=_

```
# general form: pip install git+<repository_url>#egg=<package_name>
# example:
pip install git+https://github.com/arwedus/some-example.git#egg=example-package
```

There are also a number of different ways to specify a version of the repository that you want to fetch:

```
# Use a commit SHA
pip install git+https://github.com/arwedus/some-example.git@4045597
# Use a tag
pip install git+https://github.com/arwedus/some-example.git@v1.1
# Use a branch
pip install git+https://github.com/arwedus/some-example.git@feature/fix-readme
```

## How to include the dependency in a requirements.txt

If you want to share a git repository dependency with other developers, you'll likely want to add it to your requirements.txt, like so:

```
# Just put the pip install argument straight into your requirements.txt
package-a==1.2.3
git+https://github.com/arwedus/some-package.git@v1.1
package-b==4.5.6

# Or you can use the preferred PEP 440 direct URL syntax
package-a==1.2.3
some-example @ git+https://github.com/arwedus/some-example.git@deadbeef123
```
