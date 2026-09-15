---
title: "Windows: CD/DVD brennen ohne Adminrechte"
date: "2014-01-02"
categories: 
  - "computers-and-software"
  - "windows"
layout: post
lang: de-DE
---

Unter den Windows Versionen ab 2000, XP, Vista, Windows 7 und vermutlich auch Windows 8 haben Benutzer ohne Adminrechte (Hauptbenutzer oder normale Benutzer) keine Berechtigung zum Brennen von Wechselmedien. Häufig wird im Internet empfohlen, Zusatzsoftware zu installieren, es geht aber auch mit Windows-Bordmitteln:

1\. Gruppenrichtlinien-Editor mit Administratorrechten öffnen (Startmenü -> Alle Programme -> Verwaltung -> Lokale Sicherheitsrichtlinie) 2. Öffnen von "Lokale Richtlinien" -> Sicherheitsoptionen 3. Die Richtlinie "Geräte: Formatieren und Auswerfen von Wechselmedien zulassen" durch Doppelklick öffnen. 4. Die Einstellung "Administratoren und interaktive Benutzer" auswählen und auf OK klicken.

Auf Englisch heißt die Richtlinie "Devices: Allowed to Format and Eject removable Media", die Englische Anleitung findet sich auf der MSDN Seite:

http://msdn.microsoft.com/en-us/library/windows/desktop/bb540662%28v=vs.85%29.aspx
