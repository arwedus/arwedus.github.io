---
title: "How to make docker in VS Code devcontainer use the host network"
date: "2025-02-21"
categories: 
  - "docker"
  - "linux"
layout: post
lang: en
---

If you have a complex set up, e.g. with VPN and proxy, and docker with an isolated (bridge) network is unable to connect to the internet or is even mis-configuring your DNS name resolution on the host machine (I will add another post on that), the docker option `--network=host` often helps. It tells docker to simply re-use the network connections of the host machine.

However, this is not the default and there is no central docker configuration file setting that would make this the default behavior, so when you have downloaded a project that ships it's own VS code devcontainer, chances are that the docker image build will fail (if some RUN commands in the Dockerfile require internet access) or that network access within the running docker devcontainer will not work.

You can add this configuration setting to .devcontainer/devcontainer.json to forward the \--network=host option to docker build:

```
{
  "build": {
    # ...
    "options": [
      "--network=host"
    ]
}
```

And you can add this configuration setting to .devcontainer/devcontainer.json to forward the \--network=host option to docker run:

```
{
  # ...
  "runArgs": ["--network=host"]
}
```

Try it out, and you will see the option appear in the docker build / docker run call in the devcontainer start-up log.
