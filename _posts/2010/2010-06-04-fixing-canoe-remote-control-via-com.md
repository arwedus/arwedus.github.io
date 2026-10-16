---
title: "Fixing CANoe remote control via COM"
date: "2010-06-04"
categories:
  - "programming"
  - "tools"
layout: post
lang: en
---

If you need to control replay of a CANoe/CANalyzer logfile from an outside application (e.g. a script), you can do so via the COM interface CANoe/CANalyzer provides. When you create an instance of the CANoe "Application" object, Windows COM service retrieves the CANoe executable path etc. from the registry and starts the application. If that information does not work for you, e.g. because you installed several versions of CANoe on your machine and want the older version to handle the COM requests, you can repair the registry entries by typing:

`canoe32 -regserver`

You can find the changes in the registry key `[HKEY_CLASSES_ROOT\CLSID\{7F31DEB1-5BCC-11d3-8562-00105A3E017B}]`.

Not all functions listed in the CANoe COM help have to be available in every version. To be sure, you can inspect the exported object interface withe the Visual Studio helper application "oleview.exe":

1. Open a Visual Studio 2005 command prompt and enter "oleview"
2. In the Tree view part, open "Type Libraries" and select CANoe Type Library
3. Click on the "View" button ![view button](/assets/img/posts/2010-06-04-fixing-canoe-remote-control-via-com/oleview_btn.png "oleview_btn") in the tool bar to open the interface/class viewer for CANoe
