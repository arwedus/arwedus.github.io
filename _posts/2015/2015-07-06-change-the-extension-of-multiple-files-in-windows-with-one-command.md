---
title: "Change the extension of multiple files in Windows with one command"
date: "2015-07-06"
categories: 
  - "windows"
layout: post
lang: en
---

With the windows command "ren" (rename), it's possible to rename multiple files in a specific way, but it's not possible to remove the extension of multiple files. I wrote myself a script once that modifies text files in-place but first saves a backup copy to "%filename.bak". If I want to restore the \*.bak files, I need to remove the ending .bak only. This is possible with one command by using the "for" batch command like this:

`for %x in (*.bak) do ren "%x" "%~nx"`
