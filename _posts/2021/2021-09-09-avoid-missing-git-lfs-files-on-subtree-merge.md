---
title: "Avoid missing git LFS files on subtree merge"
date: "2021-09-09"
categories:
  - "programming"
  - "vcs"
layout: post
lang: en
---

If you follow the [github instrauctions about git subtree merges](https://docs.github.com/en/get-started/using-git/about-git-subtree-merges), but your source repository (remote) for the subtree merge has git LFS enabled and contains git LFS tracked files, you may see the following error when you want to push the merge commit to your remote:

```
$ git push
Unable to find source for object 6faf8b30c6ffa04ac6a40b313d2ad835979ee13870365fd953c64dfa581b771d (try running git lfs fetch --all)
```

git lfs fetch --all won't to the trick here, as you have to transfer the LFS files from the remote repository that is the source of the subtree merge to the target repository.

The workaround described by technoweenie in https://github.com/git-lfs/git-lfs/issues/854 does the trick:

Suppose you want to do a subtree merge of repository A into repository B. Then:

```
# in repo A
$ git remote add B git-server.com/org/B
$ git lfs push B master --all
```

After this, all git LFS objects of repo A are known on the LFS server of repo B, and you can continue to push your subtree merge commit.
