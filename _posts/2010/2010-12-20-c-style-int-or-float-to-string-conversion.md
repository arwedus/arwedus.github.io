---
title: "C++ Style Int or Float to String conversion"
date: "2010-12-20"
categories:
  - "programming"
  - "C and C++"
layout: post
lang: en
---

If you want to convert an int or float/double value into a string representation without using snprintf or itoa, here's the C++ way:

```cpp
#include <sstream>

template <typename T> inline std::string to_string (const T& t) { std::stringstream ss; ss << t; return ss.str(); }
```

Of course you can also use the stringstream variable the same way as you would cout. (found on the net)
