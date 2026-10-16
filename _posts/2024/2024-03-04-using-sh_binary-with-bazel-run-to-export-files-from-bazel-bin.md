---
title: "Using sh_binary with bazel run to export files from bazel-bin"
date: "2024-03-04"
categories:
  - "programming"
tags:
  - "bazel"
layout: post
lang: en
---

In my quest to bazelize "side targets" like documentation, I've had to extract files which are the output of a bazel target to a folder outside of the "bazel world".

First, I tried to copy the files over from the `<workspace>/bazel-bin` directory in a CI script after running the `bazel build <target>` command. While this worked locally, the files were nowhere to be found when the job was executed by one of the CI/CD workers. This attempt failed for multiple reasons. First, the `bazel-bin` directory is a symlink, and it simply existed in a different path on the CI worker. So, I queried the bazel-bin directory with `bazel info bazel-bin`. Now, the action was able to see directories, but no files.

I learned that the root cause for this is that bazel was configured to only download artifacts from the remote cache when they are needed. Since bazel did not know about the script which "needs" the files to exist, it did not download the files. What was misleading about all this, is that bazel caches the build log (output), so in the log viewer of the CI/CD workflow, it always looked like the target was actually running everything (at least at first sight).

My next attempt was to add `--remote_download_outputs=all` to the bazel call. This worked, but not reliably. Since I had to copy build outputs from several targets bundled together as filegroups, it may have been more complicated. Some colleague suggested that I extract all the generated files from the build\_event JSON file, but another idea was more elegant in the end:

We created a small shell script that does the copying of the files, and added it as the source to a `sh_binary` rule. The user - or the CI workflow - can now use `bazel run <sh_binary_target>` and this will copy the files to the export folder outside of the "bazel directories". The beauty of this approach is, that we don't even have to run `bazel build <target>` before, because bazel will run this for us if the target is outdated. I also don't have to tell bazel build to download all remoute outputs explicitly - bazel will do so if the `bazel run` command is invoked, because the outputs are modelled as a data dependency to the `sh_binary` target.

In order to keep the copy job configurable (different output paths may be provided as command line argument), I've had to jump through some hoops, but here is a simplified version, that only copies one file to the export directory:

```
#!/bin/bash# export_files.shset -euo pipefailexported_file=$2cp "$1" "$exported_file"
```

This is the content of BUILD.bazel:

```
some_target(
    name = "output.tgz",
    srcs = [":all_srcs"],
)

sh_binary(
    name = "export_files",
    srcs = ["export_files.sh"],
    args = ["output_path"],
    data = [":output.tgz"],
)

```
