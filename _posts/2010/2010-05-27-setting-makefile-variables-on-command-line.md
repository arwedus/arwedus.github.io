---
title: "Setting Makefile variables on command line"
date: "2010-05-27"
categories: 
  - "programming"
  - "tools"
layout: post
lang: en
---

Usually you write something like VARNAME=value within a Makefile to define a make variable. You can also set this when you call make. For example the ADTF Makefiles set ENABLE\_DEBUG to true by default. When I want to build an ADTF example filter for release, I call make with:

`make ENABLE_DEBUG=false`
