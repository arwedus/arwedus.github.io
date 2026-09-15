---
title: "Zweite SSD Festplatte in Lenvo Yoga 13 einbauen"
date: "2016-01-02"
categories: 
  - "computers-and-software"
  - "hardware"
layout: post
lang: de-DE
---

## Anleitung auf Deutsch

Das Ideapad Yoga 13 von Lenovo hat einen zweiten mSATA Slot, in welchen eine weitere SSD installiert werden kann. Dies bietet sich an, weil auf der standardmäßig installierten 120 GB SSD bereits mehrere Partitionen für Rescue-Daten etc. reserviert wurden, so dass insgesamt neben Windows 8 oder gar Windows 10 nicht mehr viel Platz für eigene Dateien bleibt. Im folgenden beschreibe ich, was beim Einbau einer zweiten SSD zu beachten ist:

### Benötigtes Material

- Eine mSATA SSD, z.B. die Samsung SSD 850 Evo 500 GB (diese funktioniert mit meinem Yoga 13) oder die Crucial Mx200 512 GB SSD, für welche Crucial selbst die Kompatibilität mit dem Yoga 13 garantiert.
- Eine Kreuzschlitzschraube (Phillips Head) mit 2 mm Gewindedurchmesser und 3 mm Länge, kurz M2 x 3 mm. Diese sind relativ schwer erhältlich, bei Amazon ist sie von einem Fremdhändler gelistet - ich habe mir eine ähnliche Schraube mit gleichem Gewinde aus einem uralten Thinkpad "ausgeliehen". Ansonsten kann man auch eine beim Ausbau der Gehäusefront anfallende M2x3mm Schraube nehmen, wenn gar nichts anderes zur Hand ist.
- Feinmechaniker-Schraubendreher: Ein Torx T5 und ein M2 Kreuzschlitzschraubendreher ("Phillips Head"). Hilfreich ist auch eine Pinzette, um die kleinen Schrauben zu greifen.
- Eine sehr flache Plastikklinge und Abstandshalter, am Besten aus antistatischem Plastik, helfen beim Ausbau sehr.
- Wenn man am Ende genau den gleichen Zustand wie am Anfang haben möchte, braucht man ein bisschen dünnes doppelseitiges Klebeband (ich habe darauf verzichtet).
- Außerdem sollte man darauf achten, dass man auf einer nicht leitfähigen Oberfläche arbeitet (am Besten ESD-Matte) und ein antistatisches Armband (mit Erdung) verwendet.

### Informationsquellen (Englisch)

- [Lenovo Yoga 13 Hardware Maintainance Manual](https://download.lenovo.com/consumer/mobiles_pub/ideapad_yoga13_hmm_1st_edition_oct_2012_english.pdf)
- [Josh Townsends großartiger Artikel über Speichererweiterung beim Yoga 13](http://vmtoday.com/2013/01/how-to-upgrade-memory-and-storage-on-the-lenovo-ideapad-yoga-13/)
- ["Old Guy Geek"s Videotutorial zur Installation einer zweiten SSD](https://www.youtube.com/watch?v=QQFoOmeZmbY)

### Tips von mir

1. Im Hardware Maintainance Manual steht, dass für den Austausch der SSD das "Keyboard", "Keyboard Bezel" (also die Abdeckung der Oberseite des Bodys) und die Batterie auszubauen sind. Die Batterie muss allerdings für den Einbau der 2. SSD nicht ausgebaut oder abgesteckt werden.
2. Außerdem wird der zweite mSATA Slot im Maintainance Manual nicht erwähnt. Dieser befindet sich, wie in den verlinkten Tutorials gezeigt, oben rechts, also ungefähr unter der "Entf"-Taste. Die erste Festplatte befindet sich unten rechts.
3. Beim Entfernen des Keyboards mit der Plastikklinge vorsichtig in der Richtung wie im Maintainance Manual beschrieben, also von rechts oben nach links oben, vorgehen. Einen flachen Spatel oder anderes Plastikwerkzeug als Keil zwischen die Tastatur und das Gehäufe legen, wo die Tastatur schon abgehoben wurde. Die Tastatur wird oben, links und rechts von Haltenasen gehalten, die "entrasten", wenn man mit einer flachen Plastikklinge durch den Spalt zwischen Tastatur und Gehäuse fährt. Unten ist die Tastatur mit Haltenasen in das Gehäuse eingehängt. Sobald also die gesamte Oberseite losgelöst ist, kann man durch leichtes Ziehen der Tastatur in Richtung des Displays (an der "Escape" und "Entfernen" Taste festhalten) die Tastatur aus dem Gehäuse bekommen. Nicht zu weit ziehen, damit das Flachbandkabel der Tastatur nicht reißt. Bei mir war rechts oben, also etwas unterhalb der "Entf"-Taste, die Tastatur mit doppelseitigem Klebeband am Gehäuse festgeklebt. In diesem Fall hilft nur etwas mehr Kraft bzw. gezieltes Lösen dieser Klebeverbindung mit einem Spatel.
4. Nun ist der RAM Sockel sichtbar, ein RAM Update kann nun einfach durchgeführt werden:![IMG_20160102_173451](/assets/img/posts/2016-01-02-zweite-ssd-festplatte-in-lenvo-yoga-13-einbauen/img_20160102_173451.jpg)
5. Die Tastatur umdrehen, so dass das Flachbandkabel nicht spannt. Das Flachbandkabel ist eingeklemmt in einen Connector. Der schwarze Teil des Connectors ist ein Hebel! Dieser kann vorsichtig mit dem Fingernagel hochgeklappt werden (also vom Mainboard weg), das Flachbandkabel kann dann herausgezogen werden und die Tastatur kann abgenommen werden. Beim Einbau das Flachbandkabel vorsichtig so weit es geht in den Connector reinschieben, bevor man den schwarzen Hebel wieder zurückklappt. Die weiße Linie auf dem Flachbandkabel sollte mit dem weißen Sockel des Connectors eine Linie bilden, dann ist das Kabel weit genug reingeschoben.
6. Alle Torx T5 Schrauben auf der Rückseite und die 5 M2 Schrauben auf der Oberseite wie im Hardware Maintainance Manual beschrieben lösen, danach mit dem Fingernagel oder flacher Plastikklinge den Gehäusedeckel lösen, dabei zwischen der silbernen Gehäuserückseite und der schwarzen Vorderseite ansetzen. Am Einfachsten geht dies, wenn der Laptopbildschirm vollständig umgeklappt ist und auf einer weichen, nicht kratzenden Unterlage liegt. Haltenasen befinden sich an mehreren Stellen auf der Rückseite, den Seiten und der Vorderseite, gehen aber ohne viel Kraftaufwand auf, wenn man dazwischenfährt. Es befindet sich auch eine Haltenase zwischen dem HDMI- und USB-Anschluss auf der linken Seite des Gehäuses. Diese ist am schwersten wegzudrücken. Die Gehäuseoberseite wird vorne von Magneten mit an Ort und Stelle gehalten, ist aber leicht anzuheben.
7. Vorsicht! Beim Anheben der Oberseite des Gehäuses auf das "Power Button Kabel" (links) und das Touchpad-Flachbandkabel (rechts) achten. Das Hardware Maintainance Manual schreibt vor, dass diese zu lösen sind. Man kommt aber an den zweiten mSATA-Slot, ohne diese zu lösen, insbesondere wenn eine zweite Person hilft und die Oberseite hoch und leicht zur Seite hält, während man die mSATA SSD einbaut. Das linke Kabel ist leicht zu lösen (herkömmlicher Stecker-Adapter), das Touchpad-Kabel habe ich nicht ausprobiert.
8. Wie "Old Guy Geek" schon geschrieben hat, muss man beim Neustart des Rechners in das BIOS, damit die Festplatte von Windows erkannt wird. Man muss im BIOS keine Einstellungen ändern, die Festplatte sollte dort erkannt werden:
    
    \[caption id="attachment\_173" align="alignnone" width="3264"\]![BIOS main page "Information"](/assets/img/posts/2016-01-02-zweite-ssd-festplatte-in-lenvo-yoga-13-einbauen/img_20160102_190953.jpg) Lenovo Yoga 13 after adding a 2nd SSD\[/caption\]
9. Damit Windows den Datenträger verwenden kann, muss in der "Datenträgerverwaltung" in der "Computerverwaltung" (Start -> Alle Programme -> Verwaltung -> Rechtsklick auf "Computerverwaltung" und  "Ausführen als Administrator") die Festplatte partitioniert werden.
