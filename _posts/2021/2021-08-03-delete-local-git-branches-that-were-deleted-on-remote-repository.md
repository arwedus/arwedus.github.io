---
title: "Delete local git branches that were deleted on remote repository"
date: "2021-08-03"
layout: post
lang: en
---

This blog post is based on the [article with the same name by KC Müller,](https://medium.com/@kcmueller/delete-local-git-branches-that-were-deleted-on-remote-repository-b596b71b530c) which I extend a little bit here so that my command takes care of not deleting local branches checked out in worktrees.

We let our remote servers (GitHub or Bitbucket) delete branches after merging a pull request per default. I sometimes check out branches I'm reviewing, and we work with many branches, so the old branches for which the remote tracking branch has been deleted start to pile up.

A "git prune" will only remove the remote tracking branch, but not delete the branch in your local git repo. So this is the command I use (in Linux!) to delete all local branches with a deleted remote tracking branch, which are not currently checked out:

```
git branch -vv | grep ': gone]' | grep -Ev "(\*|\+|master|develop)" | xargs -r -n 1 git branch -d
```

Here's how it works:

- git branch -vv lists all local branches and shows information about the remote branch, saying ": gone\]" if the remote branch is not present any more.
    
- grep ': gone\]' filters for those lines which contain the ': gone\]' phrase.
    
- grep -Ev ... removes lines from the result that contain an asterisk, a plus, or the names "master" or "develop". This will ignore the branch you are currently on (marked with an asterisk), branches checked out in other worktrees (marked with a +), and the special branches "develop" and "master". It will also prevent that the “git branch -d” is executed with a “\*” at the end which would result in deleting all your local branches.  
    NOTE: This might filter out braches like "merge-xy-to-master". I will likely improve this regular expression in the future.
- xargs -r -n 1 git branch -d calls "git branch -d" on each argument. The option -r avoids that the command is called with no arguments, and the option "-n 1" limits the number of passed arguments to one, which means that the first word - which happens to be the branch name - is passed. With the option -D, also branches which have not been fully merged into the current branch are deleted, which is helpful if the project has several long-running integration branches.

There you go, all stale branches cleaned!

I added this to my .bashrc as an alias:

```
# deletes all branches which have been deleted on remote, except for 
git-cleanup() {
    git branch -vv | grep ': gone]' | grep -Ev "(\*|\+|master|develop)" | awk '{print $1}' | xargs -r -n 1 git branch -D
}
```

I use a function instead of an alias to avoid trouble with escaping the Dollar signs and single/double quotes.
