---
title: "Ubuntu: Find out from which repository a package comes from"
date: "2021-04-27"
categories:
  - "computers-and-software"
  - "linux"
layout: post
lang: en
---

Quick and short, the following command shows you the soure of an installed package:

```
apt-cache policy <Package Name>
```

A list of available sources is /etc/apt/sources.list
