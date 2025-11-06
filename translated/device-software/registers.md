<!--
原文: 文件路径: gpu-glossary/device-software/registers.md
翻译时间: 2025-11-06 18:40:09
-->

---
title: 什么是寄存器？
---

![](https://files.mdnice.com/user/59/01fd1dd1-9924-4a8e-ab3b-7275250bcd13.png)

> 寄存器是[内存层次结构](/gpu-glossary/device-software/memory-hierarchy)中与单个[线程](/gpu-glossary/device-software/thread)相关联的内存（左图）。改编自 NVIDIA 的 [CUDA Refresher: The CUDA Programming Model](https://developer.nvidia.com/blog/cuda-refresher-cuda-programming-model/) 和 NVIDIA [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#programming-model) 中的图表。

在[内存层次结构](/gpu-glossary/device-software/memory-hierarchy)的最底层是寄存器，它们存储由单个[线程](/gpu-glossary/device-software/thread)操作的信息。

寄存器中的值通常存储在[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)的[寄存器文件](/gpu-glossary/device-hardware/register-file)中，但也可能溢出到[GPU RAM](/gpu-glossary/device-hardware/gpu-ram)中的[全局内存](/gpu-glossary/device-software/global-memory)，这会带来显著的性能损失。

与 CPU 编程类似，这些寄存器不能通过高级语言（如[CUDA C](/gpu-glossary/host-software/cuda-c)）直接操作。它们仅对底层语言可见，此处即[并行线程执行 (PTX)](/gpu-glossary/device-software/parallel-thread-execution)。它们通常由 `ptxas` 等编译器管理。编译器的目标之一是限制每个[线程](/gpu-glossary/device-software/thread)使用的寄存器空间，以便可以将更多[线程块](/gpu-glossary/device-software/thread-block)同时调度到单个[SM](/gpu-glossary/device-hardware/streaming-multiprocessor)中，从而提高[占用率](/gpu-glossary/perf/occupancy)。

[PTX](/gpu-glossary/device-software/parallel-thread-execution) 指令集架构中使用的寄存器记录在[此处](https://docs.nvidia.com/cuda/parallel-thread-execution/#register-state-space)。据我们所知，[SASS](/gpu-glossary/device-software/streaming-assembler) 中使用的寄存器则没有公开文档。