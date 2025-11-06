<!--
原文: 文件路径: gpu-glossary/device-software/cooperative-thread-array.md
翻译时间: 2025-11-06 18:41:29
-->

---
title: 什么是协作线程阵列？
---

![协作线程阵列对应于 [CUDA 编程模型](/gpu-glossary/device-software/cuda-programming-model) 中线程块层次结构的[线程块](/gpu-glossary/device-software/thread-block)级别。改编自 NVIDIA 的 [CUDA Refresher: The CUDA Programming Model](https://developer.nvidia.com/blog/cuda-refresher-cuda-programming-model/) 和 NVIDIA [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#programming-model) 中的图表。](../images/cuda-programming-model.svg)

协作线程阵列 (Cooperative Thread Array, CTA) 是被调度到同一个[流式多处理器 (Streaming Multiprocessor, SM)](/gpu-glossary/device-hardware/streaming-multiprocessor) 上的线程集合。CTA 是 [CUDA 编程模型](/gpu-glossary/device-software/cuda-programming-model) 中[线程块](/gpu-glossary/device-software/thread-block) 在 [PTX](/gpu-glossary/device-software/parallel-thread-execution)/[SASS](/gpu-glossary/device-software/streaming-assembler) 层面的实现。CTA 由一个或多个[线程束 (warp)](/gpu-glossary/device-software/warp) 组成。

程序员可以指示 CTA 内的[线程](/gpu-glossary/device-software/thread)相互协调。位于 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 的 [L1 数据缓存](/gpu-glossary/device-hardware/l1-data-cache) 中的程序员管理的[共享内存 (shared memory)](/gpu-glossary/device-software/shared-memory) 使这种协调变得快速。与 CTA 内的线程不同，不同 CTA 中的线程无法通过屏障相互协调，而必须通过[全局内存 (global memory)](/gpu-glossary/device-software/global-memory) 进行协调，例如通过原子更新指令。由于驱动程序在运行时控制 CTA 的调度，CTA 的执行顺序是不确定的，并且一个 CTA 阻塞等待另一个 CTA 很容易导致死锁。

可以调度到单个 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 上的 CTA 数量决定了[可实现的占用率 (achievable occupancy)](/gpu-glossary/perf/occupancy)，并取决于多种因素。从根本上说，[SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 的资源是有限的——[寄存器文件 (register file)](/gpu-glossary/device-hardware/register-file) 中的行数、[线程束 (warp)](/gpu-glossary/device-software/warp) 的"槽位"、[L1 数据缓存](/gpu-glossary/device-hardware/l1-data-cache) 中的[共享内存 (shared memory)](/gpu-glossary/device-software/shared-memory) 字节数——而每个 CTA 在被调度到一个 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 上时，都会使用一定量的这些资源（在[编译](/gpu-glossary/host-software/nvcc)时计算得出）。