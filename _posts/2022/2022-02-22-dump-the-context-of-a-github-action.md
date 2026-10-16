---
title: "Dump the context of a github action"
date: "2022-02-22"
categories:
  - "programming"
layout: post
lang: en
---

Github Actions documentation on specific events, e.g. "pull\_request", isn't great. To answer questions like "where can I find the labels added to the PR that triggered the workflow", it may be the most straightforward way to simply dump all information that the workflow receives, by dumping the github context.

You can to this within a github workflow file with this step:

{% raw %}
```yaml
- name: Dump GitHub context
  env:
    GITHUB_CONTEXT: ${{ toJson(github) }}
  run: echo "$GITHUB_CONTEXT"
```
{% endraw %}
