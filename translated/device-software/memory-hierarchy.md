<!--
原文: 文件路径: gpu-glossary/device-software/memory-hierarchy.md
翻译时间: 2025-11-06 18:34:38
-->

---
title: 什么是 CUDA 内存层次结构？
---

![[共享内存 (Shared Memory)](/gpu-glossary/device-software/shared-memory) 和 [全局内存 (Global Memory)](/gpu-glossary/device-software/global-memory) 是 [CUDA 编程模型 (CUDA Programming Model)](/gpu-glossary/device-software/cuda-programming-model) 中的两个内存层次（左图），分别映射到 [L1 数据缓存 (L1 Data Cache)](/gpu-glossary/device-hardware/l1-data-cache) 和 [GPU 显存 (GPU RAM)](/gpu-glossary/device-hardware/gpu-ram)。改编自 NVIDIA 的 [CUDA Refresher: The CUDA Programming Model](https://developer.nvidia.com/blog/cuda-refresher-cuda-programming-model/) 和 NVIDIA [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#programming-model) 中的图表。](../images/cuda-programming-model.svg)

作为 [CUDA 编程模型 (CUDA Programming Model)](/gpu-glossary/device-software/cuda-programming-model) 的一部分，[线程层次结构 (Thread Hierarchy)](/gpu-glossary/device-software/thread-hierarchy) 的每个级别都可以访问该级别中所有[线程 (Thread)](/gpu-glossary/device-software/thread) 共享的独立内存块：即"内存层次结构"。该内存可用于协调和通信，并由程序员（而非硬件或运行时）管理。

对于[线程块网格 (Thread Block Grid)](/gpu-glossary/device-software/thread-block-grid)，其共享内存位于 [GPU 显存 (GPU RAM)](/gpu-glossary/device-hardware/gpu-ram) 中，称为[全局内存 (Global Memory)](/gpu-glossary/device-software/global-memory)。可以通过原子操作和屏障来协调对此内存的访问，但跨[线程块 (Thread Block)](/gpu-glossary/device-software/thread-block) 的执行顺序是不确定的。

对于单个[线程 (Thread)](/gpu-glossary/device-software/thread)，其内存是[流式多处理器 (Streaming Multiprocessor, SM)](/gpu-glossary/device-hardware/streaming-multiprocessor) 的[寄存器文件 (Register File)](/gpu-glossary/device-hardware/register-file) 的一部分。根据 [CUDA 编程模型 (CUDA Programming Model)](/gpu-glossary/device-software/cuda-programming-model) 的原始语义，此内存是[线程 (Thread)](/gpu-glossary/device-software/thread) 私有的，但为了在[张量核心 (Tensor Core)](/gpu-glossary/device-hardware/tensor-core) 上实现矩阵乘法而添加到 [PTX (Parallel Thread Execution)](/gpu-glossary/device-software/parallel-thread-execution) 和 [SASS (Streaming Assembler)](/gpu-glossary/device-software/streaming-assembler) 的某些指令会在[线程 (Thread)](/gpu-glossary/device-software/thread) 之间共享输入和输出。

介于两者之间的是线程层次结构中[线程块 (Thread Block)](/gpu-glossary/device-software/thread-block) 级别的[共享内存 (Shared Memory)](/gpu-glossary/device-software/shared-memory)，它存储在每个 [SM (Streaming Multiprocessor)](/gpu-glossary/device-hardware/streaming-multiprocessor) 的 [L1 数据缓存 (L1 Data Cache)](/gpu-glossary/device-hardware/l1-data-cache) 中。对此缓存的精心管理——例如，在加载新数据之前将数据加载到其中以支持[最大数量的算术运算](/gpu-glossary/perf/arithmetic-intensity)——是设计[高性能 (High-Performance)](/gpu-glossary/perf) CUDA [内核 (Kernel)](/gpu-glossary/device-software/kernel) 的关键所在。