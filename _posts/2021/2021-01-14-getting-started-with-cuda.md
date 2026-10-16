---
title: "Getting started with CUDA"
date: "2021-01-14"
categories:
  - "CUDA"
layout: post
lang: en
---

First example I used was the [even easier introduction to CUDA blog post.](https://developer.nvidia.com/blog/even-easier-introduction-cuda/) First thing that did not quite work is the call to nvprof:

```
$ nvprof ./add_cuda
==7511== NVPROF is profiling process 7511, command: ./add_cuda
Max error: 0
==7511== Profiling application: ./add_cuda
==7511== Profiling result:
No kernels were profiled.
No API activities were profiled.
==7511== Warning: Some profiling data are not recorded. Make sure cudaProfilerStop() or cuProfilerStop() is called before application exit to flush profile data.
======== Error: Application received signal 11
```

`"Signal 11"` is `SIGSEGV` (segmentation fault). I did some web search to find out that I need to add an option for nvprof to work:
`$ nvprof --unified-memory-profiling off ./add_cuda`

But why doesn't it work like in the example? Because NVidia profiler is deprecated since the Volta GPU generation, which is the last to still support it.

- Pascal Architecture: Full support for nvprof
- NVidia Xavier Gen1 (on Drive board) = Volta Architecture, full support for nvprof but deprecated
- NVidia Geforce RTX 20... (on workstation) = Turing Architecture, inofficial/partial support for nvprof
- See also: [https://docs.nvidia.com/cuda/profiler-users-guide/index.html#migrating-to-nsight-tools](https://docs.nvidia.com/cuda/profiler-users-guide/index.html#migrating-to-nsight-tools)

So the call failed but it's also not supported any more. I tried using the replacement _nsys_ instead.
Turns out you need to install NsightSystems first. To do so, register at [https://developer.nvidia.com/](https://developer.nvidia.com/) and go to the Download section. After installation, run from the console:

```
$ nsys nvprof ./add_cuda
```

So, that works fine and I was able to finish the excercise.

The Cuda-10 manual also mentions that "Nvidia Nsight Eclipse Edition" is going to be removed by the next release, so Cuda-11 and newer only come with the Nvidia Nsight Eclipse plug-ins. `/usr/local/cuda-xyz/doc/pdf/Nsight_Eclipse_Plugins_Installation_Guide.pdf` explains how to install them into an existing Eclipse. cuda-10.0 Nsight Eclipse plug-ins were compatible with the newest Eclipse version as of the time of writing this (2020.12).
