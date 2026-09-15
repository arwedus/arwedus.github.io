---
title: "Linux: Show files from an apt package"
date: "2021-04-28"
categories: 
  - "linux"
tags: 
  - "apt"
layout: post
lang: en
---

As I search for these commands time and time again, I'll just copy the Post which lists them all:

https://serverfault.com/questions/96964/list-of-files-installed-from-apt-package

To find which files were installed by a package, use `dpkg -L`:

```
$ dpkg -L $package
```

`apt-file` can tell you which files will be installed by a package before installing it:

```
root# apt-get install apt-file
root# apt-file update
$ apt-file list $package
```

NOTE: apt-file needs to be installed first (sudo apt-get install apt-file).

Or if you have the package as a `.deb` file locally already, you can run `dpkg` on it:

```
$ dpkg --contents $package.deb
```

To find which package provides a file that is already on your system, use:

```
$ dpkg -S /path/to/file
```

To find which package provides a file that is not currently on your system, use `apt-file` again:

```
$ apt-file search /path/to/file
```
