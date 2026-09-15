---
title: "C: Unit test of static functions (module local)"
date: "2015-07-09"
categories: 
  - "c-and-c"
layout: post
lang: en
---

When you want to unit test the functions you do not export, i.e., you have defined them with the "static" keyword, there are three ways to accomplish this:

1. Add the unit tests at the end of the file containing the static functions.
2. Expose the function declarations in the header (probably guarded by some `#ifdef UNIT_IMPL`), and instead of writing `static`, use a preprocessor definition like VISIBILITY, which you redefine to an empty string if you want to build your unit test suite. Include the header in your separate unit test file.
3. Include the file under test in the unit test file: `// content of module_test.c: #include "module.c" // ...`

I find the 3rd way to be the most elegant.
