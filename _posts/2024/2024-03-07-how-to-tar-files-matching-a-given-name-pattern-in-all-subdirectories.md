---
title: "How to tar files matching a given name pattern in all subdirectories"
date: "2024-03-07"
categories: 
  - "computers-and-software"
  - "linux"
layout: post
lang: en
---

This is just a quick repost of [https://stackoverflow.com/questions/18731603/how-to-tar-certain-file-types-in-all-subdirectories](https://stackoverflow.com/questions/18731603/how-to-tar-certain-file-types-in-all-subdirectories), because I find it so useful:

Given a directory with deeply nested subdirectories, and I want to just extract e.g. all \*.yaml configuration files, this is the command to do it:

`find . -name "*.yaml" | tar -cvf my_archive -T -`
