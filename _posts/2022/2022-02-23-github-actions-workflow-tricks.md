---
title: "Github actions: Workflow tricks"
date: "2022-02-23"
layout: post
lang: en
---

This is a collection of how to accomplish various tasks and tricks in github workflows, which are not directly covered by the github actions documentation and aren't obvious.

### How to query the type of an event

When you add a trigger event, for example "pull\_request", to the workflow, this event usually has more than one type. In the case of pull\_request, this could be "open", "reopened" and "synchronize". If you only want to run a step of your workflow when the workflow was triggered by a certain event type (e.g. when a pull request was opened, but not when it receives new pushes), you can add an if-condition to the steps.

The if-condition has to query github.event.action:

{% raw %}
```yaml
on:
  workflow_dispatch:
  pull_request:
    types: [opened, closed, reopened, synchonize]

jobs:
  build:    
    name: Print info
    runs-on: ubuntu-latest
    steps:
      - name: Print GitHub event action
        run: |
          echo "${{ github.event.action }}"
      - name: Run when PR is opened
        if: ${{ github.event_name == 'pull_request' && github.event.action == 'opened' }}
        run: |
          echo "You just opened a PR!"
```
{% endraw %}
