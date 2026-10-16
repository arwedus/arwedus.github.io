---
title: "Remotedesktopverbindung ohne Abmelden des lokalen Benutzers"
date: "2014-01-02"
categories:
  - "computers-and-software"
  - "windows"
layout: post
lang: de-DE
---

Unter Windows 2000, XP, Vista und Windows 7 muss der aktuell angemeldete lokale Benutzer abgemeldet werden, wenn eine Benutzersession per Remotedesktopverbindung aufgebaut werden soll.

Dieses Limit besteht nicht unter Windows Server Versionen.

Es existiert ein Patch für die Datei termsrv.dll, welcher dieses Limit aufhebt:

http://deepxw.blogspot.de/search/label/Universal%20Termsrv.dll%20Patch

Das Programm startet ohne Installation, ein Klick auf "Patch", gefolgt von einem Neustart des Systems, reicht aus. Der Patch funktioniert bei mir (Windows 7) einwandfrei. Der Patcher legt eine Backup-Datei der originalen termsrv.dll Datei an.
