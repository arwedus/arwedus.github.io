---
title: "Eclipse: Fixing the \"Program is not a Recognized Executable\" Error"
date: "2011-01-02"
categories:
  - "programming"
  - "C and C++"
  - "eclipse"
layout: post
lang: en
---

This has been taken from a FAQ at http://wiki.wxwidgets.org

When you compile & link a program, the Eclipse run feature will try to recognize the executable, using one of several parsers. If the wrong binary parser (or none at all) is selected for the project, Eclipse will show the above error in the "Run..." dialog when you select the executable file for your project. Follow those steps to add a binary parser:

In the Eclipse main menu

- select "Project" -> "Properties"

- navigate to "C/C++ Build" -> "Settings" -> (on the right) "Binary Parsers"

In the "Binary parser:" list, check the "PE Windows Parser" and click "OK" (lower right)
