---
title: "Find out default python version for any Ubuntu release"
date: "2022-02-18"
layout: post
lang: en
---

If you want to find the default Python 3 version of _any_ Ubuntu release, run the command

```
rmadison python3
```

example output:

```
 python3 | 3.6.5-3         | bionic         | amd64, arm64, armhf, i386, ppc64el, s390x
 python3 | 3.6.7-1~18.04   | bionic-updates | amd64, arm64, armhf, i386, ppc64el, s390x
 python3 | 3.8.2-0ubuntu2  | focal          | amd64, arm64, armhf, i386, ppc64el, riscv64, s390x
 python3 | 3.9.4-1build1   | impish         | amd64, arm64, armhf, i386, ppc64el, riscv64, s390x
 python3 | 3.9.7-4         | jammy          | amd64, arm64, armhf, i386, ppc64el, riscv64, s390x
 python3 | 3.10.1-0ubuntu1 | jammy-proposed | amd64, arm64, armhf, i386, ppc64el, riscv64, s390x
```

Alternatively, check the package

https://packages.ubuntu.com/search?suite=groovy&keywords=python3
