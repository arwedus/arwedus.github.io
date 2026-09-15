---
title: "Libxml2 and Python on Windows"
date: "2010-05-19"
categories: 
  - "python"
  - "xml"
layout: post
lang: en
---

For the purpose of using XPath and XQuery out of my python scripts for test statistics generation, I decided to try libxml2. I mostly decided against ElementTree because their website told me the XPath subset does not support queries like:

`count(//event[evalresult/text()="FALSE"][warnlevel/text()="1"])`

Also, I hope to be faster with the C-based implementation of libxml2. For installation, I only had to download [this pre-bundled lxml windows binary](http://pypi.python.org/packages/2.5/l/lxml/lxml-2.2.4.win32-py2.5.exe) from [the python package repository](http://pypi.python.org/simple/lxml); it comes with libxml2 included.

The following code is enough to get the above count: \[sourcecode light="true" language="python"\] from lxml import etree doc = etree.parse(filePath) result = doc.xpath('//event\[evalresult/text()="FALSE"\]\[warnlevel/text()="1"\]') count = len(result) count2 = doc.xpath(count('//event\[evalresult/text()="FALSE"\]\[warnlevel/text()="1"\]')) # alternative \[/sourcecode\]

About XQuery: lxml serves as frontend for libxml2 and libxslt, neither of which support XQuery.

Further information: [lxml homepage](http://codespeak.net/lxml/) [SketchPath, a good XPath expression evaluation software](http://qutoric.com/sketchpath/downloads/basic-index.html)
