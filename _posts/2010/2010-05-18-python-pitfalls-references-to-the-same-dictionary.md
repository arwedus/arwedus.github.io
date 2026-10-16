---
title: "Python Pitfalls: References to the same dictionary"
date: "2010-05-18"
categories:
  - "python"
tags:
  - "dictionaries"
layout: post
lang: en
---

Today, I tried to build a dictionary which contains the contents of a list as keys and empty dictionarys as values. First, I went with the method dict.fromkeys(seq, \[value\]), then I filled the sub-dictionaries in a for loop, like this:

```python
mydict = dict.fromkeys(lstLabels, {}) for strLabel in dict.keys(): mydict[strLabel][strLabel] = "x"
```

What I ended up with was that the sub-dictionaries referenced by the keys from lstLabels all referenced to the same dictionary instance. What this means is, that whenever you add something to dict\[lstLabels\[0\]\], it appears in dict\[lstLabels\[1\]\], too, and so on.

The correct way to accomplish what I wanted - different instances of subdirectories - was this:

```python
for strLabel in lstLabels: mydict[strLabel] = {} mydict[strLabel][strLabel] = "x"
```

Apparently, the dict.fromkeys() method does something like lstFail = \[\[\] \* 3\]

Are there more elegant ways to create a dictionary with subdictionarys based on a list of strings than the one presented?
