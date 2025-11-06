<!--
原文: 文件路径: gpu-glossary/device-software/thread-block.md
翻译时间: 2025-11-06 18:38:40
-->

---
title: 什么是 CUDA 线程块？
---

![线程块是 [CUDA 编程模型](/gpu-glossary/device-software/cuda-programming-model) 线程层次结构中的中间层级（左图）。一个线程块在单个 [流式多处理器 (Streaming Multiprocessor)](/gpu-glossary/device-hardware/streaming-multiprocessor) 上执行（右图，中间）。改编自 NVIDIA 的 [CUDA 复习：CUDA 编程模型](https://developer.nvidia.com/blog/cuda-refresher-cuda-programming-model/) 和 NVIDIA [CUDA C++ 编程指南](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#programming-model) 中的图表。](../images/cuda-programming-model.svg)

线程块是 [CUDA 编程模型 (CUDA programming model)](/gpu-glossary/device-software/cuda-programming-model) 的[线程层次结构 (thread hierarchy)](/gpu-glossary/device-software/thread-hierarchy) 中的一个层级，位于[网格 (grid)](/gpu-glossary/device-software/thread-block-grid) 之下但在[线程 (thread)](/gpu-glossary/device-software/thread) 之上。它是 [CUDA 编程模型](/gpu-glossary/device-software/cuda-programming-model) 中与 [PTX (Parallel Thread Execution)](/gpu-glossary/device-software/parallel-thread-execution)/[SASS (Streaming Assembler)](/gpu-glossary/device-software/streaming-assembler) 中具体的[协作线程阵列 (cooperative thread array)](/gpu-glossary/device-software/cooperative-thread-array) 相对应的抽象概念。

在 [CUDA 编程模型](/gpu-glossary/device-software/cuda-programming-model) 中，线程块是向程序员暴露的最小线程协调单元。线程块必须独立执行，因此任何线程块的执行顺序都是有效的，从任意顺序的完全串行执行到所有交错的并行执行。

单个 CUDA [内核 (kernel)](/gpu-glossary/device-software/kernel) 启动会产生一个或多个线程块（以[线程块网格 (thread block grid)](/gpu-glossary/device-software/thread-block-grid) 的形式），每个线程块包含一个或多个[线程束 (warp)](/gpu-glossary/device-software/warp)。线程块的大小可以是任意的，但通常是[线程束](/gpu-glossary/device-software/warp) 大小的倍数（在所有当前的 CUDA GPU 上为 32）。