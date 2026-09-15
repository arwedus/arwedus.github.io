---
title: "Timed shutdown (Windows 7)"
date: "2014-11-22"
layout: post
lang: en
---

This has been posted many times all over the Internet, but I find it so useful I'll include it in my collection: How to do a timed shutdown of the computer:

Start a command line window (Start Menu -> Search for "cmd" -> hit enter).

In the command line, run the shutdown command with any of the following parameters:

- **shutdown /h** _(hibernate, NOT help!)_
- **shutdown /t 300** _(shutdown in 300 s, or 5 minutes)_
- **shutdown /s** _(shuts down immediately)_
- **shutdown /f** _(force closing running applications)_
- **shutdown /r** _(restart)_
- **shutdown /a** _(abort a shutdown)_
