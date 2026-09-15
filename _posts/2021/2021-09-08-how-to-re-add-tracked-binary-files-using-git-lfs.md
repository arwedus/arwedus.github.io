---
title: "How to re-add tracked binary files using git LFS"
date: "2021-09-08"
tags: 
  - "git"
  - "lfs"
layout: post
lang: en
---

Using git lfs migrate rewrites history, which is not always acceptable, especially in distributed projects. You can add files to git LFS by either renaming them (which deletes and re-adds the file, with the new file tracked by git LFS), or by modifying them. The following command chain uses the second approach to re-add binary files using git LFS, without a modification of the file itself:

```
touch binary_image.png
git add binary_image.png
git commit -m "Re-add binary_image tracked by git LFS"
```

Done!
