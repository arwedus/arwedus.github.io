---
title: "Linux: Fix missing xorg.conf"
date: "2020-02-17"
categories:
  - "computers-and-software"
  - "linux"
tags:
  - "nvidia"
layout: post
lang: en
---

I'm using Ubuntu Linux 18.10 with an old Thinkpad T410 laptop and am quite satisfied, but I had to do some work to get the laptop display's brightness control keys working with my Nvidia graphics card. I had to add the following to xorg.conf:

```
Option "RegistryDwords" "EnableBrightnessControl=1"
```

(Source: https://www.thomas-krenn.com/de/wiki/Fehlerhafte\_Helligkeitssteuerung\_unter\_Linux\_beim\_Thinkpad\_T410\_beheben )

However, there was no xorg.conf anywhere! I found out after some research that in Ubuntu 18.04 onwards, xorg.conf is not created by default. Run

```
nvidia-xconfig
```

and it creates an /etc/X11/xorg.conf. The changes I added there were applied on the next reboot and I was able to use the Fn - Pos1 / End keys for the laptop screen's brightness control again.
