---
title: "Random Bash wisdom"
date: "2021-01-11"
categories: 
  - "linux"
  - "programming"
layout: post
lang: en
---

I've recently found myself writing some bash scripts and I wanted to collect some random wisdom I aggregated:

1\. [This is a great cheat-sheet for bash if conditions: https://clburlison.com/bash-if-then-cheat-sheet/](https://clburlison.com/bash-if-then-cheat-sheet/)

2\. If you have a back-up solution in case a certain command is not available in the PATH, you can use the following to test it:

```
if ! command -v my_tool > /dev/null; then
    # do something in case my_tool is not available
fi
```

NOTE: In bash, you can also use "hash" command, as this post summarizes: [https://scripter.co/check-if-a-command-exists-from-shell-script/](https://scripter.co/check-if-a-command-exists-from-shell-script/)

3\. To get the path of your own script:

```
SCRIPT_DIR=$(realpath $(dirname "$0"))
```

4\. Understanding Curly braces: [https://www.linux.com/topic/desktop/all-about-curly-braces-bash/](https://www.linux.com/topic/desktop/all-about-curly-braces-bash/)  
Now, I don't think every variable should be put in ${}, but it's useful to have a reference on what you can do when using ${} instead of just the $ sign.

5\. I like using pushd and popd, but I also like them to be silent. [https://serverfault.com/questions/108154/can-i-call-pushd-popd-and-prevent-it-printing-the-stack](https://serverfault.com/questions/108154/can-i-call-pushd-popd-and-prevent-it-printing-the-stack) shows how to do it:

```
pushd mydir > /dev/null
# work in mydir
popd > /dev/null
```

Finally, the Wikibook on Bash Shell Scripting is realy good ([https://en.wikibooks.org/wiki/Bash\_Shell\_Scripting](https://en.wikibooks.org/wiki/Bash_Shell_Scripting)).
