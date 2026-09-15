---
title: "Indentation of XML documents"
date: "2010-05-19"
categories: 
  - "xml"
layout: post
lang: en
---

A nice way to auto-indent your XML documents is via the free editor [Notepad++](http://notepad-plus.sourceforge.net/de/site.htm).

Load your XML document, then navigate the menu TextFX -> TextFX HTML Tidy -> Tidy: Reindent XML

The preconfigured HTML tidy also does some other fixes on your XML code, e.g. converting special characters to ampersand notation and word wrapping at 69 characters. To disable those, you have to alter the TIDYCFG.INI file in folder "plugins\\Config\\tidy" in your Notpad++ program directory. Add a new configuration like this:

`[Tidy: Reindent XML] input-xml:yes indent:yes wrap:0 wrap-sections:no` Look at the Tidy project page for a [list of all HTML tidy attributes](http://tidy.sourceforge.net/docs/quickref.html).
