<!--
原文: 文件路径: gpu-glossary/device-software/thread-hierarchy.md
翻译时间: 2025-11-06 18:33:11
-->

---
title: CUDA 线程层次结构是什么？
---

![CUDA 编程模型的线程层次结构从单个线程到线程块再到线程块网格（左侧），映射到硬件上则从 CUDA 核心到流式多处理器 (SM) 再到整个 GPU（右侧）。改编自 NVIDIA 的《CUDA Refresher: The CUDA Programming Model》和 NVIDIA 《CUDA C++ Programming Guide》中的图表。](https://modal.com/_next/image?url=%2Fgpu-glossary%2Fcuda-programming-model.svg&w=1920&q=75)

线程层次结构是 [CUDA 编程模型](/gpu-glossary/device-software/cuda-programming-model) 的关键抽象概念，与 [内存层次结构](/gpu-glossary/device-software/memory-hierarchy) 并列。它从单个线程到整个 GPU 设备，跨多个级别组织并行程序的执行。

最底层是单个 [线程](/gpu-glossary/device-software/thread)。与 CPU 上的执行线程类似，每个 [CUDA 线程](/gpu-glossary/device-software/thread) 执行一系列指令。执行算术和逻辑指令的硬件资源称为 [核心](/gpu-glossary/device-hardware/core) 或有时称为 "管道"。线程由 [线程束调度器](/gpu-glossary/device-hardware/warp-scheduler) 选择执行。

中间层由 [线程块](/gpu-glossary/device-software/thread-block) 组成，在 [PTX](/gpu-glossary/device-software/parallel-thread-execution) 和 [SASS](/gpu-glossary/device-software/streaming-assembler) 中也称为 [协作线程数组](/gpu-glossary/device-software/cooperative-thread-array)。每个 [线程](/gpu-glossary/device-software/thread) 在其 [线程块](/gpu-glossary/device-software/thread-block) 内具有唯一标识符。这些线程标识符是基于索引的，以便于根据输入或输出数组的索引将工作分配给线程。一个块内的所有线程同时调度到同一个 [流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor) 上。它们可以通过 [共享内存](/gpu-glossary/device-software/shared-memory) 进行协调，并通过屏障进行同步。

在最高层，多个 [线程块](/gpu-glossary/device-software/thread-block) 被组织成一个跨越整个 GPU 的 [线程块网格](/gpu-glossary/device-software/thread-block-grid)。[线程块](/gpu-glossary/device-software/thread-block) 在协调和通信方面受到严格限制。网格内的块彼此并发执行，没有保证的执行顺序。[CUDA 程序](/gpu-glossary/device-software/cuda-programming-model) 必须编写成任何块的交错执行都是有效的，从完全串行到完全并行。这意味着 [线程块](/gpu-glossary/device-software/thread-block) 不能，例如，通过屏障进行同步。与 [线程](/gpu-glossary/device-software/thread) 类似，每个 [线程块](/gpu-glossary/device-software/thread-block) 都有一个唯一的、基于索引的标识符，以支持基于数组索引的工作分配。

这种层次结构直接映射到 [GPU 硬件](/gpu-glossary/device-hardware)：
[线程](/gpu-glossary/device-software/thread) 在单个 [核心](/gpu-glossary/device-hardware/core) 上执行，
[线程块](/gpu-glossary/device-software/thread-block) 被调度到 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 上，
而 [网格](/gpu-glossary/device-software/thread-block-grid) 则利用设备上所有可用的 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor)。