---
title: "Docker as a build environment, Part 2: Bind mounts"
date: "2021-01-23"
categories:
  - "programming"
  - "docker"
layout: post
lang: en
---

In my previous post, I ended with two goals yet unaccomplished:

- Avoiding costly copy of all source files (we're talking about a multiple Gigabyte repository here) into the docker image
- Using Docker as a build environment but not as an execution environment in the leanest possible way.

Even though all tutorials tell you to, I am not happy with the solution to copy all source files into the docker image (using the COPY instruction inside the Dockerfile). The build environment itself rarely changes, whereas the source files change all the time - and thus a new Docker image is created for every build, filling up your image cache. Docker offers an alternative to that: the [bind mounts](https://docs.docker.com/get-started/06_bind_mounts/).

Using a bind mount, you could map the input directory, e.g. your source tree, directly into a mount point in the running docker container. Given a build environment docker image called build\_env, the command would look like this:

```
docker run -it --name build-container --mount type=bind,ro=true,source=$(pwd),destination=/src  build_env:latest /src/build.sh
```

The last argument (**/src/build.sh**) calls a build command which is part of the source folder in the host file system - no need to COPY anything, no need to create a new docker image for the build stage!

The --mount argument declares that this is a read-only bind mount, so no temp files will be accidentally written to your source tree (possibly with a user that does not exist in the host OS or - even worse, owned by _root_). This read-only source tree also makes it clear that the bind-mount strategy only works with out-of-source builds.

But where do the build results go? They are generated inside the docker container file system.

As soon as the container is removed, the build result disappears with it. So better copy them out into your destination directory before:

```bash
docker cp build-container:/path/to/build-output .
docker rm build-container
```

**It is not advisable** to simply add a (second) mount binding to use as build output destination directory, because the owner of the files created by the docker process will be what was defined as USER previously in the Dockerfile - per default root. This may cause big trouble, throwing garbage owned by root into the host's file system. Juan Treminio has written an in-depth [blog post about this](https://jtreminio.com/blog/running-docker-containers-as-current-host-user/). Bottom line: You can run the container as your own user, but before that, you have to make sure that _any user_ has enough access rights inside the container to run the programs e.g. the build toolchain. This is the command:

```
docker container run --rm \
    -v ${PWD}:/var/www \
    -w /var/www \
    -u $(id -u ${USER}):$(id -g ${USER}) \
    jtreminio/php:7.2 composer require psr/log
```

It seems safer and simpler to me to use "docker cp" instead.

So, for just building locally, there's the possibility to run docker, then get the build output from the running (or stopped) container. Unfortunately, there is no way to get the functionality of a "bind mount" into Docker _image creation_, though.

The "COPY --from" command which is used in a multi-stage docker build to copy the build result from a previous stage into the final _execution environment_ image only works with Docker images which are created in the same _Dockerfile_ as source.

I found out that you cannot use "docker run --name build-container --mount ..." to build in a Docker _container_ named _build-container_, and then use "COPY --from=_build-container_ ..." in a Dockerfile to copy the build output from the container into the dodo image. The [Dockerfile reference](https://docs.docker.com/engine/reference/builder/#copy) is very clear about this:

> Optionally `COPY` accepts a flag `--from=<name>` that can be used to set the source location to a previous build stage (created with `FROM .. AS <name>`) that will be used instead of a build context sent by the user. In case a build stage with a specified name can’t be found an image with the same name is attempted to be used instead.

Okay, so an image works as well... but not a container.

If you think about how Docker works internally, this limitation becomes clear: The _Docker build command_ sends commands (and the build context) to the _Docker daemon_, which creates the image. The _Docker daemon_ could run on a different node and does not see our _local_ Docker containers.

So what to do if we want to create an _execution environment_ image with the build output? We have no choice but to resort to the multi-stage build and create an image for the build itself as well - which means we have to COPY the source tree into the build image. Too bad :-(.

But, in the next post about Docker I will show some ways to clean up temporary images systematically.

* * *

p.s.: When you feel like losing overview over all your docker images or running low on disk space, check out [https://linuxconfig.org/how-to-remove-all-docker-images-stored-in-a-local-repository](https://linuxconfig.org/how-to-remove-all-docker-images-stored-in-a-local-repository) to free up some space. If this command tells you that images are used by a container, please enter

```
docker ps -a
```

to see all the currently not running docker containers. Even containers you stopped a while ago is still listed there. You have to remove them if you don't need them any more:

docker rm
