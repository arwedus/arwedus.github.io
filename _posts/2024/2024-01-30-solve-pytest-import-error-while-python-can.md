---
title: "Solve pytest import error (while python can)"
date: "2024-01-30"
categories: 
  - "programming"
  - "python"
tags: 
  - "pytest"
layout: post
lang: en
---

After refactoring a formerly monolithic python script into several files, I started getting problems related to module imports. I shifted the source code into a package directory, and the test/ directory was now parallel to the package source directory. The full directory layout was like this:

```
<packagename>|- <packagename>/|  |- __init__.py|  |- module_1.py|  `- ...|- test/|  |- __init__.py|  |- test_module1.py|  `- ...|- __init__.py|- README.md`- packagename.py
```

When running "pytest <packagename>", I got:

```
ImportError while importing test module '...'
```

However, when running "packagename.py" (executable python script via shebang), everything worked fine. Both the test modules and the main script contained the same import statement:

```
from packagename import module_1
```

A google search turned up: [https://stackoverflow.com/questions/41748464/pytest-cannot-import-module-while-python-can](https://stackoverflow.com/questions/41748464/pytest-cannot-import-module-while-python-can), which pointed me in the direction that the issue must be related to \_\_init\_\_.py  
  
However, the solution was not to delete \_\_init\_\_.py in the test folder, but to delete \_\_init\_\_.py in the main package folder. I came to this solution based on the documentation of pytest: [https://docs.pytest.org/en/latest/explanation/goodpractices.html#tests-as-part-of-application-code](https://docs.pytest.org/en/latest/explanation/goodpractices.html#tests-as-part-of-application-code)

The working layout is:

```
<packagename>|- <packagename>/|  |- __init__.py|  |- module_1.py|  `- ...|- test/|  |- __init__.py|  |- test_module1.py|  `- ...|- README.md`- packagename.py
```

**Disclaimer:**

I do not want to advertise this directory layout for python packages. In my use case, I have a python script inside a very large repository that is not distributed as a package outside of this repository; I just wanted to improve maintainability.  
When you want to create a python package for distribution, you're faced with many other considerations. There are two competing package structure styles: With or without the package sources inside a "src/" folder. The python packing guide advertises the "src/" folder layout. See [https://packaging.python.org/en/latest/tutorials/packaging-projects/#a-simple-project](https://packaging.python.org/en/latest/tutorials/packaging-projects/#a-simple-project) for an example of "<packagename>/src/<packagename>" layout. If in doubt, go with one of the more popular cookiecutter templates.
