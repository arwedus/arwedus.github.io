---
title: "Modify last commit date in git"
date: "2022-04-01"
categories:
  - "programming"
tags:
  - "git"
layout: post
lang: en
---

## Set the date of the last commit to the current date

`git commit --amend --no-edit --date "$(date)"`

## Set the date of the last commit to an arbitrary date

`git commit --amend --no-edit --date "Mon 21 Jul 2021 20:21:00 CET"`
