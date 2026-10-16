---
title: "Installing Python packages with easy_install"
date: "2010-05-17"
categories:
  - "python"
tags:
  - "easy_install"
  - "firewall"
  - "proxy"
layout: post
lang: en
---

Python comes with a nice tool called easy\_install that enables you to install additional packages as easy as:

easy\_install <package\_name>

If you are behind a HTTP proxy server, this might fail unless you specify the proxy URL in the environment variable HTTP\_PROXY like this:

set http\_proxy="http://www.myproxy.org"

However, when you are sitting behind a firewall (like we at my company are), you might still not be able to download any packages from the python package repository. Here's a quick guide how to circumvent the issue:

1. Create a folder on your local machine that will contain all packages you have to download.
2. Go to http://pypi.python.org/simple/ and download the package you want to install into your local folder.
3. In the scripts directory of your python installation, call: easy\_install -H none -f d:\\Backup\\Programs\\python-packages <package\_name>
4. When you disallow all foreign hosts with "-H none", easy\_install will not be able to fetch any packages your package depends on, so you have to resolve all dependency errors by repeating step 1 - 3 for the missing package if easy\_install gives you a message like this: "No local packages or download links found for logilab-common>=0.49.0"

Another solution I found on the internet would be to install and use ASProxy, but I'm not going to try that for now.

See also: [easy\_install guide](http://peak.telecommunity.com/DevCenter/EasyInstall)
