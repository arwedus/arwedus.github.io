---
title: "Fix a spurious ruff python linter warning E402"
date: "2024-02-01"
categories:
  - "programming"
  - "python"
layout: post
lang: en
---

Ruff issues the warning message "E402 Module level import not at top of file" for the following python code. First I thought that this is a bug, because the module imports are at the top of the file. There's just the [shebang](https://einfachpython.de/scripte-in-python-usrbinenv-python/), the module docstring, and the copyright string before that... and all those should appear before the import statements according to python style guides. So this example file should be valid python code:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__copyright__ = """
(c) 2017-2024 Arwed Starke
The reproduction, distribution and utilization of this file as
well as the communication of its contents to others without express
authorization is prohibited. Offenders will be held liable for the
payment of damages and can be prosecuted. All rights reserved
particularly in the event of the grant of a patent, utility model
or design.
"""

""" This ROS node displays traffic light interface data."""

import rospy
import signal

# ...
```

Another warning by pydocstyle that the module has no module docstring pointed me to the solution: I have to put the module docstring before the copyright string:

```python
#!/usr/bin/env python
""" This ROS node displays traffic light interface data."""

__copyright__ = """
(c) 2017-2024 Arwed Starke
The reproduction, distribution and utilization of this file as
well as the communication of its contents to others without express
authorization is prohibited. Offenders will be held liable for the
payment of damages and can be prosecuted. All rights reserved
particularly in the event of the grant of a patent, utility model or design.
"""

import rospy
import signal

# ...
```

It was an easy fix, but hard to find out because the ruff message is kinda unspecific for this issue and there is no auto-fix available.
