---
title: "Profiling with Python: cProfile and RunSnakeRun"
date: "2010-06-01"
categories: 
  - "programming"
  - "python"
  - "tools"
layout: post
lang: en
---

This is my favorite way to analyze the performance of my Python scripts:

1. Call the script with cProfile: `python -m cProfile -o profile.dat main.py`
2. Open the profiler data with RunSnakeRun: `%PYTHON_ROOT%\scripts\runsnake.exe` A nice GUI will start up, and you can open the profile.dat file in there.

You have to install RunSnakeRun first, of course. You should choose the [easy\_install procedure I described here](http://arwedus.wordpress.com/2010/05/17/installing-python-packages-with-easy_install/) for the runsnake.exe to be installed in the scripts directory. You can find the current RunSnakeRun package [on pypi](http://pypi.python.org/simple/RunSnakeRun/).

[RunSnakeRun homepage](http://www.vrplumber.com/programming/runsnakerun/)
