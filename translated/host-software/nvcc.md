<!--
原文: 文件路径: gpu-glossary/host-software/nvcc.md
翻译时间: 2025-11-06 18:28:45
-->

---
title: 什么是 NVIDIA CUDA 编译器驱动程序？
abbreviation: nvcc
---

NVIDIA CUDA 编译器驱动程序是一个用于编译
[CUDA C/C++](/gpu-glossary/host-software/cuda-c) 程序的工具链。它输出符合主机 ABI 的二进制可执行文件，其中包含要在 GPU 上执行的
[PTX](/gpu-glossary/device-software/parallel-thread-execution) 和/或
[SASS](/gpu-glossary/device-software/streaming-assembler) —— 即所谓的"胖二进制文件"。这些二进制文件可以使用与其他二进制文件相同的工具（如 Linux 上的 `readelf`）进行检查，但还可以使用专门的
[CUDA 二进制工具集](/gpu-glossary/host-software/cuda-binary-utilities) 进行额外操作。

包含的 [PTX](/gpu-glossary/device-software/parallel-thread-execution) 代码按
[计算能力 (Compute Capability)](/gpu-glossary/device-software/compute-capability)
进行版本控制，通过向 `--gpu-architecture` 或 `--gpu-code` 选项传递 `compute_XYz` 值来配置。

包含的 [SASS](/gpu-glossary/device-software/streaming-assembler) 代码按
[流式多处理器架构版本 (SM architecture version)](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)
进行版本控制，通过向 `--gpu-architecture` 或 `--gpu-code` 选项传递 `sm_XYz` 值来配置。将 `compute_XYz` 传递给 `--gpu-code` 也会触发生成与
[PTX](/gpu-glossary/device-software/parallel-thread-execution) 版本相同的
[SASS](/gpu-glossary/device-software/streaming-assembler) 代码。

主机/CPU 代码的编译是使用主机系统的编译器驱动程序完成的，例如 `gcc` 编译器驱动程序。请注意，不要将编译器驱动程序与硬件驱动程序（如
[NVIDIA GPU 驱动程序](/gpu-glossary/host-software/nvidia-gpu-drivers)）混淆。

`nvcc` 的文档可以在
[此处](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/) 找到。