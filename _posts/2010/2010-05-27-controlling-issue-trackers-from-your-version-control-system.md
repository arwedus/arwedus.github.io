---
title: "Controlling issue trackers from your version control system"
date: "2010-05-27"
categories:
  - "programming"
  - "vcs"
layout: post
lang: en
---

I've been looking around for issue trackers and this is a short summary on how to control issues from commit comments.

Trac: see #Nr - reference an issue (comment shows up in history of the ticket with that number) fixes #Nr - automatically closes a "bug" ticket with that number closes #Nr - automatically closes a "feature request" ticket with that number

Redmine: for referencing issues: refs, references, IssueID for fixing issues: fixes, closes example: This commit refs #1, #2 and fixes #3

Mantis: Has to be configured by a regular expression. Could be issue, bug #id for referencing and fixes, closes #id etc. for fixing issues.

Some more notes on these systems: Trac (current version 0.12) requires python with setuptools and Genshi, one DBMS (SQLite, PostgreSQL or MySQL) and the svn repository (one per Trac installation) has to exist on the same server as the Trac. Redmine (current version 0.95, 1.0 coming soon) is based on Ruby on Rails, and works at least with mysql/pgsql/sqlite as DBMS. SVN binaries have to be installed on the machine running the redmine, but the SVN server can exist somewhere else. Mantis (current version 1.3) is based on PHP and is proven to work with MySQL/PGsql/MS SQL or DB2, but not SQLite. The SVN server can reside on a different machine. While Mantis and Trac SVN integration seems to work via a post-commit hook only, Redmine also allows to update SVN information periodically (e.g. cron-job) or on demand.
