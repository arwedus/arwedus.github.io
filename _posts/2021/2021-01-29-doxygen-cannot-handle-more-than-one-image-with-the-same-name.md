---
title: "Doxygen cannot handle more than one image with the same name"
date: "2021-01-29"
categories:
  - "programming"
layout: post
lang: en
---

As you might know, you can include images in the output of your Doxygen html documentation like this:

```
@image html path/to/img.png
```

In one of my larger projects, I found out that doxygen simply copies all referenced images, which it finds somewhere below the IMAGE\_PATH, into the root directory of the output folder. Given the following structure:

```
src/component1/doc/component1.mdsrc/component1/doc/img/structure.svgsrc/component2/doc/component2.mdsrc/component2/doc/img/structure.svg
```

where component1.md and component2.md both have the following content:

```
...
![Structure](img/structure.svg)
...
```

the output will show the component2/doc/img/structure.svg for both component1 and component2. There is no warning or error message during doxygen generation about this.

As I don't think this behavior can be right, I added an issue report for it:

[https://github.com/doxygen/doxygen/issues/8362](https://github.com/doxygen/doxygen/issues/8362)

Nevertheless, this means for the time being: Make sure all image file names referenced by Doxygen are unique.
