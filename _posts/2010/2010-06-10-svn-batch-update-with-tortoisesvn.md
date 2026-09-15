---
title: "SVN Batch Update with TortoiseSVN"
date: "2010-06-10"
categories: 
  - "project-management"
  - "tools"
layout: post
lang: en
---

This one-liner within a .bat file will update all subversion copies in the directory of the .bat file:

\[sourcecode\] for /d %%d in (\*. ) do call c:\\programme\\tortoisesvn\\bin\\tortoiseproc /command:update /path:%%d /notempfile /closeonend:3 \[/sourcecode\]
