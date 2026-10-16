---
title: "Fix Synology Diskstation Performance issue due to AV"
date: "2020-12-04"
categories:
  - "network-attached-storage"
tags:
  - "diskstation"
  - "ssh"
  - "synology"
layout: post
lang: en
---

Recently my old Synology NAS Diskstation DS213j had severe performance issues. Connecting to it via web GUI or one of the apps (photo station / audio station) would take ages and often the client would report "network time limit exceeded" or "no connection".

To find the culprit, I resorted to SSH:

1. Open a shell (works under Linux as well as Windows 10) and connect to diskstation using "ssh <user>@<diskstation-hostname>"
2. Answer the security prompt with "yes"
3. Enter the account PW at the prompt and you should be logged in to your DiskStation.
4. Enter the command "top" and look for large memory or CPU consumtion in the continuously refereshing list of processes.

In my case, it was the "Antivirus Essential" program that continuously used up > 50% of the available RAM, which caused the rest of the system to be very unresponsive. Antivirus Essential also used CPU budget sporadically (on access to some files via any of the apps), but that was way less.

Anyhow, disabling (or uninstalling) Antivirus Essential solved the performance issue for me. Maybe the performance is less of an issue on Diskstations with larger installed RAM.
