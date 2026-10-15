---
title: "SVN Merge done right"
date: "2010-11-23"
categories:
  - "programming"
  - "vcs"
layout: post
lang: en
---

\[to be fleshed out\]

When merging by hand, the recommendation is to always specify the range of revisions you want to merge from your branch to the trunk. First, look up the revision in which the branch was created in the SVN log (select "stop on copy" to hide everything the revisions before the branch was created). Then, merge your branch to your trunk and create a comment like "merged branch revision x-y". Because if you want to merge the branch changes to the trunk again at a later point in time, you must not merge the changes prior to revision y again.

Here's how you merge a specific change from the trunk to your branch:

Select "SVN merge" on your branch and choose the repository URL of your trunk. Look up the revision which brought the change you want and select that revision. If you want to merge all changes in the trunk since the last merge, lookup your svn:mergeinfor property or check your merge comment for the revision number, and enter as range everything from the next revision until HEAD. Now do the merge. The merge happens in your working copy, so you have to commit the changes to your branch working copy after the merge.

Always commit the whole working copy (from the toplevel directory) after a merge. You will see in the commit log that the toplevel directory was modified. If you double click the toplevel folder you will see that the difference is that the SVN property svn:mergeinfo was created and it contains the revision number of your merge (e.g. svn:mergeinfo: Folder/trunk:388).

If TortoiseSVN finds this property in your working copy, it will not merge changes prior to that revision when you merge again, even if you do not specify a revision (which, by default, would mean "merge all changes", even the ones already merged). This is the theory. In practice, always do a "test merge" first.

It is important to remember that a SVN merge is based on diff, so it's a from -> to semantic. If you want to merge changes from the trunk into your branch, it's from "trunk" to "branch". If you want to reintegrate the changes in your branch into the trunk, you actually want to get the trunk from the "current trunk" to the "branch", so it's a merge from "trunk" to "branch". Remember to always merge the changes to the trunk into your branch before you reintegrate your branch. This splits up the merging into two distinct steps and you prevent chaos (hopefully). Here's a nice how to about this:

http://bchavez.bitarmory.com/archive/2008/06/03/quothow-toquot-svn-merge-with-tortoisesvn.aspx

Read up on merging here: http://tortoisesvn.net/docs/release/TortoiseSVN\_en/tsvn-dug-merge.html http://svnbook.red-bean.com/en/1.0/ch04s04.html
