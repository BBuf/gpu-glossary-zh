<!--
原文: 文件路径: gpu-glossary/device-software/thread-block-grid.md
翻译时间: 2025-11-06 18:30:26
-->

---
title: 什么是线程块网格？
---

![线程块网格是 [CUDA 编程模型](/gpu-glossary/device-software/cuda-programming-model) 线程组层次结构的最高层级（左图）。它们映射到多个 [流式多处理器 (Streaming Multiprocessor)](/gpu-glossary/device-hardware/streaming-multiprocessor) 上（右图，底部）。改编自 NVIDIA 的 [CUDA Refresher: The CUDA Programming Model](https://developer.nvidia.com/blog/cuda-refresher-cuda-programming-model/) 和 NVIDIA [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#programming-model) 中的图表。](../images/cuda-programming-model.svg)

当 CUDA [内核 (kernel)](/gpu-glossary/device-software/kernel) 启动时，它会创建一个称为线程块网格的[线程 (thread)](/gpu-glossary/device-software/thread) 集合。网格可以是一维、二维或三维的。它们由[线程块 (thread block)](/gpu-glossary/device-software/thread-block) 组成。

在[内存层次结构 (memory hierarchy)](/gpu-glossary/device-software/memory-hierarchy) 中对应的级别是[全局内存 (global memory)](/gpu-glossary/device-software/global-memory)。

[线程块 (thread block)](/gpu-glossary/device-software/thread-block) 实际上是独立计算单元。它们并发执行，即执行顺序不确定，范围从在只有一个[流式多处理器 (Streaming Multiprocessor)](/gpu-glossary/device-hardware/streaming-multiprocessor) 的 GPU 上完全顺序执行，到在有足够资源同时运行所有线程块的 GPU 上完全并行执行。