---
title: "Unix: Copy a list of files"
date: "2010-10-01"
categories:
  - "programming"
  - "shell"
layout: post
lang: en
---

In one project, we have a selection of files I want to update from another directory tree containing much more stuff. Here's how I get the selection of files I want to copy:

`find . -type f | egrep -v '/\.svn/|\.obj' > selection.txt`

For copying only the files named in selection.txt, I use tar to build an archive from those files:

`tar czvf files.tgz -T selection.txt`

By extracting those files, you have a copy of only those files you wanted with relative directories created as well. (--from-file is synonymous to -T)
