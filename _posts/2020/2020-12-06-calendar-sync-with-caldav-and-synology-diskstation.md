---
title: "Calendar Sync with CalDAV and Synology DiskStation"
date: "2020-12-06"
tags: 
  - "caldav"
  - "calendar"
  - "diskstation"
  - "nas"
  - "synology"
layout: post
lang: en
---

I've always used my mobile phone's calendar heavily. It's just convenient to not have to remember everything when you're on the go, but managing calender entries is so much better on the PC or laptop screen. When I switched to a smartphone, I did not want to push my calendar into the Google Cloud, though, and I ended up using MyPhoneExplorer for synchronizing between Thunderbird (+Lightning) and my Android phone (+aCalendar). That sufficed for a while, but since I'm in a relationship, we needed to share and synchronize calendar entries.

In 2013 I bought a Synology DiskStation NAS for us and I wanted to create my own cloud calendar. I used the Synology WebDAV Server app and some free CalDAV android sync app which failed to work lately. Now, I've set it up again using the "Synology Calendar" app. It's quite nice because it has built-in support for calendar sharing between users of the DiskStation (DS). This is the setup I ended up creating:

<figure>

[![](https://arwedus.wordpress.com/wp-content/uploads/2020/12/synology_caldav_sync.png?w=676)](https://arwedus.wordpress.com/wp-content/uploads/2020/12/synology_caldav_sync.png)

<figcaption>

Calendar Synchronization with CalDAV and Synology Calendar

</figcaption>

</figure>

The key point is: Not only are no external Cloud Services involved, but also we don't have to open up the DiskStation to the internet for calendar sync to work. If you don't like the restriction that you can't sync calendar entries with each other outside the home network, this can be changed, too, by opening up the DiskStation via DDNS, but I will not cover this in this article.

Here is the step-by-step guide how I made calendar sync with my DS work.

Let's start with some helpful links first:

1. Synology Calendar product page: [https://www.synology.com/en-us/dsm/feature/calendar](https://www.synology.com/en-us/dsm/feature/calendar)
2. [Synology Calendar CalDAV sync: https://www.synology.com/en-global/knowledgebase/DSM/tutorial/Collaboration/How\_to\_Sync\_Synology\_Calendar\_with\_CalDAV\_Clients#t6](https://www.synology.com/en-global/knowledgebase/DSM/tutorial/Collaboration/How_to_Sync_Synology_Calendar_with_CalDAV_Clients#t6)
3. Android CalDAV sync adapter app:[http://www.davx5.com](http://www.davx5.com)
4. How to export all your existing calendar entries to move them into the new shared calendars: [https://support.mozilla.org/en-US/kb/exporting-and-sharing-a-calendar](https://support.mozilla.org/en-US/kb/exporting-and-sharing-a-calendar)

Part 1: Installing Synology Calendar

1. Log in to your DiskStation GUI as admin
2. Install the "Synology Calendar" app
3. Your users need access rights to the application (Control Center -> Users):  
    Click on Application tab and select "Synology Calendar" - Allow (see below)
4. Log in as regular user on the DS and try to open the Calendar -> should work
5. You see a "My Calendar". Create a second calendar for shared calendar entries.  
    For this calendar, you can invite other DiskStation users via drop-down menu point "share" ("Freigeben").
6. Klick on the little drop-down menu icon next to the calendar name and select "CalDAV Account" (D: "CalDAV Konto"). Write down the URLs.  
    

[![](https://arwedus.wordpress.com/wp-content/uploads/2020/12/grafik.png?w=894)](https://arwedus.wordpress.com/wp-content/uploads/2020/12/grafik.png)

Part 2: Getting Thunderbird to sync

Thunderbird has some easy-to-follow guide on how to set up a calendar, and since it changes with new versions I'll just give the link here:

[https://support.mozilla.org/de/kb/neue-kalender-erstellen#thunderbird:linux:tb78](https://support.mozilla.org/de/kb/neue-kalender-erstellen#thunderbird:linux:tb78)

It's in German because I could not find an English version of the same page, but the help page by Synology I linked above explains how to set CalDAV up in English. Here are the steps which you need to do inside the "Calendar" tab of Thunderbird (if you don't have one, you might wanna install "lightning" calendar add-on):

1. Right-click on "Calendar" -> select "New Calendar"
2. Select "on the network", click next
3. Select "CalDAV", and enter the URL which you have written down from "CalDAV Account".  
    NOTE: You can also use https://name-of-my-diskstation:5001/caldav/<username>/home if you want to have SSH connection  
    Mark "offline support" checkbox and click next
4. Add your mail address and all other info, then click finish
5. Try to synchronize with a test calendar entry. You'll notice that all your existing calendar entries are still in the old calendar and thus, not synced. More on that later.

Part 3: Get CalDAV sync on Android

I tried several CalDAV sync apps on my phone, but in the end only DAVx (former dav-droid) would work. It also has a cool feature to allow syncing only in certain Wi-Fi networks (it's called "[Wifi SSID restriction](https://www.davx5.com/manual/settings.html#synchronization)").

1. Install DAVx from Android app store. It comes at a price it is well worth, but for tests sake you can also download and install from [https://f-droid.org/packages/at.bitfire.davdroid/](https://f-droid.org/packages/at.bitfire.davdroid/) for free.
2. Go through the set-up steps by following their great installation guide. Use "base URL" as shown in Synology Calendar ("CalDAV Account" dialog, the https://name-of-my-diskstation:5000/caldav/Username URL).
3. If all goes well you see the calendars which are within your account on the DS appear.
4. You can select those calendars in aCalendar, e.g. your "My Calendar" shall be the new default calendar.

Part 4: Importing all your calendar entries.

This may vary from calendar app to calendar app, but what I did is:

1. Export all my calendar entries to ICS (e.g. [https://support.mozilla.org/en-US/kb/exporting-and-sharing-a-calendar](https://support.mozilla.org/en-US/kb/exporting-and-sharing-a-calendar)). Save the ics files as a backup.
2. Import the calendar entries to the new shared calendar. You can import ICS in Synology Calendar, or in Thunderbird, or in aCalendar. If your synchronization works, you will see the entries appear in all other places sooner or later. Give it some time for a large calendar.
3. It is also easy to split up an ics calendar file in several smaller ones if import fails. Just open the ICS file in a good text editor and try to get a grasp of the ICS format.

Part 5: Finish the migration

For now, I just disabled the previous un-synced calendars in the calendar apps (works in aCalendar as well as in Thunderbird by un-checking them). Somtetime in the future, I will delete them.

Summary

There's some reading involved and the CalDAV sync on Android costs some Euros, but it is possible in a few hours to set up automated local-network calendar synchronization, backup, and shared calendars with Synology DiskStation, DAVx and Thunderbird. Other organizer software will work as well, as CalDAV is an established standard.
