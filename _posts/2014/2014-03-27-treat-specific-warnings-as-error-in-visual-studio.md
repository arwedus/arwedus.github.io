---
title: "Treat specific warnings as error in Visual Studio"
date: "2014-03-27"
categories: 
  - "c-and-c"
  - "programming"
  - "visual-studio"
layout: post
lang: en
---

Some warnings are so severe that they should be treated as errors at compilation, others are not.

There's the option to treat all warnings as errors in the Visual Studio IDE or at the command line (/WX). In Visual studio 2013, and also in Visual Studio 2005, there's an option to treat only specific warnings as errors, with the command line option /we.

Example: To treat the warning that a function is being used without a previous declaration into an error, add /we4013 to the compiler's command line.

To read more on compiler warning options, see the [Micrsosoft Page](http://msdn.microsoft.com/en-us/library/thxezb7y.aspx).
