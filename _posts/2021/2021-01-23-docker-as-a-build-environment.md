---
title: "Docker as a build environment"
date: "2021-01-23"
categories:
  - "programming"
  - "docker"
layout: post
lang: en
---

This is the first of a series of posts about using Docker to create and use containerized build environments.

The need for this came up at work in software projects where a large tool landscape was needed to work with the codebase (C/C++ for embedded targets and Python with lots of extra package dependencies). In my particular case, I wanted to facilitate generating the documentation in a docs-as-code fashion (see for example [https://doctoolchain.github.io/docToolchain/](https://doctoolchain.github.io/docToolchain/)).

This is not a gentle introduction to Docker. It requires basic knowledge of how to create a Docker image and how to work with Docker containers.

My docker build is a [multi-stage build](https://docs.docker.com/develop/develop-images/multistage-build/), as recommended by Docker for this use case:

- Stage 1 builds a generic image that contains all dependencies required to build documentation ("build environment).  This image may be cached locally or the docker registry.
- Stage 2 copies all source files into the build environment image and runs the build steps to generate build output (in this case: static HTML pages).
- Stage 3 builds an "execution environment" (in this case: nginx web server) and copies the buid output from Stage 2 to the location from which it can be run (or in this case, the root directory for the nginx webserver).

The _build environment_ image can be reused easily, the _build stage_ is temporary and short-lived, and the _execution environment_ image can run the executable(s) or, in this case, the webserver hosting the static HTML pages for the project documentation, without containing all the build toolchain or source code. This makes the _execution environment_ image small and easy to deploy or exchange.

Multi-stage builds are also recommended by Microsoft in their well-written VSCode [Docker tutorial](https://docs.microsoft.com/en-us/visualstudio/docker/tutorials/image-building-best-practices#multi-stage-builds).

While these builds are nice, two open points remained for me:

1. At least in stage 2, a COPY operation of the source files into the container is required. In addition, the build context will be large - as large as your source tree (.dockerignore file can reduce the size of the build context which is sent to the Docker daemon considerably, but the COPY operation still remains, and eats up both time and increases image size).
2. What if I only want to have a containerized _build environment_, but no need for a containerized _execution environment_ (let's assume I have installed the dependencies or a framework, e.g. ROS, anyways?).

Could a "bind mount" be the solution to those problems? Find the answer in my next blog post.
