---
title: "A good introduction to dependency management in large software projects"
date: "2023-06-16"
categories:
  - "programming"
  - "tools"
tags:
  - "bazel"
  - "continuous-integration"
layout: post
lang: en
---

I have worked on some parts of the build dependency handling in a large software project in my company (monorepo project, > 1800 packages, > 10 million LOC, 100s of external dependencies). I recently stumbled upon this article in Google's Bazel documentation and really enjoyed reading it:

https://bazel.build/basics/dependencies

As usual, when it comes to developing software at scale, Google has already written about the experiences you make in your journey. I can agree to all of the points about dependency handling that they make.
