<!--
原文: 文件路径: gpu-glossary/host-software/nvrtc.md
翻译时间: 2025-11-06 18:24:09
-->

---
title: 什么是 NVIDIA 运行时编译器？
abbreviation: nvrtc
---

NVIDIA 运行时编译器 (`nvrtc`) 是一个用于 CUDA C 的运行时编译库。它能够将 [CUDA C++](/gpu-glossary/host-software/cuda-c) 编译为 [PTX](/gpu-glossary/device-software/parallel-thread-execution)，而无需在另一个进程中单独启动 [NVIDIA CUDA 编译器驱动程序](/gpu-glossary/host-software/nvcc) (`nvcc`)。一些库或框架会使用它，例如，将生成的 C/C++ 代码映射到可以在 GPU 上运行的 [PTX](/gpu-glossary/device-software/parallel-thread-execution) 代码。

请注意，此 [PTX](/gpu-glossary/device-software/parallel-thread-execution) 随后会通过 JIT（即时）编译，从 [PTX](/gpu-glossary/device-software/parallel-thread-execution) 中间表示进一步编译为 [SASS 汇编代码](/gpu-glossary/device-software/streaming-assembler)。这一步由 [NVIDIA GPU 驱动程序](/gpu-glossary/host-software/nvidia-gpu-drivers) 完成，并且与 NVRTC 执行的编译是分开的。包含 [PTX](/gpu-glossary/device-software/parallel-thread-execution) 的 CUDA 二进制文件（为实现前向兼容性所必需）同样需要经过此编译步骤。

NVRTC 是闭源的。您可以在[此处](https://docs.nvidia.com/cuda/nvrtc/index.html)找到其文档。