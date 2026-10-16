---
title: "Keyword substitution with Subversion"
date: "2010-05-28"
categories:
  - "programming"
  - "tools"
layout: post
lang: en
---

It's a cumbersome task to keep the revision number, last-changed date and last-modified-by information of a source file up-to-date. That's what subversion keyword substitution is for.

How it works: You add special fields to your file comment, like $Author$. This is my default C++ header comment:

\[sourcecode language="c++"\] /\*\* \* \* \\brief Short description of the purpose of this file \* \* @copyright Copyright (c) 2010 me \* @author Original Author: me \* @author Last changed: $Author$ \* @date Creation date: 2010-05-28 \* @date Last changed: $Date$ \* @version $Revision$ \* \*/ \[/sourcecode\]

When you add and commit this file, nothing will happen to the special fields enclosed in dollar signs. First, you have to add them to the subversion property "keywords". To do so with ToroiseSVN, right click and open the file's propertys and go to the subversion tab. Select svn:keywords from the drop-down list and enter something like "Date Author Revision" on the edit line. You can also select multiple files and change the property for all of them at once. Your next commit will show the auto-updated fields.

For a description of all possible keywords, look [here](http://svnbook.red-bean.com/en/1.4/svn.advanced.props.special.keywords.html).
