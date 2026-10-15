---
title: "Invaluable SVN properties for source files"
date: "2010-09-02"
categories:
  - "programming"
  - "vcs"
layout: post
lang: en
---

If you add a source file to your repository, think about adding those SVN properties:

`svn:eol-style = native svn:mime-type = text/plain svn:keywords = Date Revision HeadURL Author`

The first line checks a file for consistent line endings before it can be commited. The last line enables the magic tags like $Date: $ (see previous post).

You can also make TortoiseSVN auto-add properties by setting it up in the \[auto-props\] section of your SVN config file (%APPDATA%/Subversion/config). Here are some useful lines:

`[auto-props] *.cpp = svn:mime-type=text/plain;svn:eol-style=native *.hpp = svn:mime-type=text/plain;svn:eol-style=native *.h = svn:mime-type=text/plain;svn:eol-style=native *.c = svn:mime-type=text/plain;svn:eol-style=native *.dbc = svn:mime-type=text/plain;svn:eol-style=CRLF *.doc = svn:needs-lock=true;svn:mime-type=application/msword`
