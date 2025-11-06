<!--
原文: 文件路径: gpu-glossary/perf/occupancy.md
翻译时间: 2025-11-06 18:57:27
-->

---
title: 什么是占用率？
---

占用率是设备上[活动线程束](/gpu-glossary/perf/warp-execution-state)数量与最大[活动线程束](/gpu-glossary/perf/warp-execution-state)数量的比值。

![四个时钟周期中每个周期有四个线程束槽位，因此共有16=4*4个线程束槽位，其中15个槽位中有活动线程束，占用率约为94%。图表灵感来自GTC 2025的[*CUDA Techniques to Maximize Compute and Instruction Throughput*](https://www.nvidia.com/en-us/on-demand/session/gtc25-s72685/)演讲。](../images/cycles.svg)

占用率测量有两种类型：

- **理论占用率**：由于内核启动配置和设备能力而导致的占用率上限。
- **实际占用率**：在[内核](/gpu-glossary/device-software/kernel)执行期间（即在[活动周期](/gpu-glossary/perf/active-cycle)期间）测量的实际占用率。

作为[CUDA编程模型](/gpu-glossary/device-software/cuda-programming-model)的一部分，[线程块](/gpu-glossary/device-software/thread-block)中的所有[线程](/gpu-glossary/device-software/thread)都被调度到同一个[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)上。每个[SM](/gpu-glossary/device-hardware/streaming-multiprocessor)都有资源（如[共享内存](/gpu-glossary/device-software/shared-memory)中的空间），这些资源必须在[线程块](/gpu-glossary/device-software/thread-block)之间进行分配，因此限制了可以在[SM](/gpu-glossary/device-hardware/streaming-multiprocessor)上调度的[线程块](/gpu-glossary/device-software/thread-block)数量。

让我们来看一个例子。考虑NVIDIA H100 GPU，它具有以下规格：

```
最大线程束/SM：64
最大块/SM：32
（32位）寄存器：65536
共享内存：228 KB
```

对于一个使用每[线程块](/gpu-glossary/device-software/thread-block)32个[线程](/gpu-glossary/device-software/thread)、每[线程](/gpu-glossary/device-software/thread)8个[寄存器](/gpu-glossary/device-software/registers)和每[线程块](/gpu-glossary/device-software/thread-block)12 KB[共享内存](/gpu-glossary/device-software/shared-memory)的[内核](/gpu-glossary/device-software/kernel)，我们最终受到[共享内存](/gpu-glossary/device-software/shared-memory)的限制：

```
64 > 1   = 线程束/块 = 32线程/块 ÷ 32线程/线程束
32 < 256 = 块/寄存器文件 = 65,536寄存器/寄存器文件 ÷ (32线程/块 × 8寄存器/线程)
32       = 块/SM
19       = 块/共享内存 = 228 KB/共享内存 ÷ 12 KB/块
```

尽管我们的[寄存器文件](/gpu-glossary/device-hardware/register-file)足够大，可以同时支持256个[线程块](/gpu-glossary/device-software/thread-block)，但我们的[共享内存](/gpu-glossary/device-software/shared-memory)不够，因此我们每个[SM](/gpu-glossary/device-hardware/streaming-multiprocessor)只能运行19个[线程块](/gpu-glossary/device-software/thread-block)，对应19个[线程束](/gpu-glossary/device-software/warp)。这是常见情况，即存储在[寄存器](/gpu-glossary/device-software/registers)中的程序中间结果的大小远小于需要保留在[共享内存](/gpu-glossary/device-software/shared-memory)中的程序[工作集](https://en.wikipedia.org/wiki/Working_set)元素的大小。

当没有足够的[合格线程束](/gpu-glossary/perf/warp-execution-state)来[隐藏指令延迟](/gpu-glossary/perf/latency-hiding)时，低占用率会损害性能，这表现为低指令[发射效率](/gpu-glossary/perf/issue-efficiency)和[利用率不足的流水线](/gpu-glossary/perf/pipe-utilization)。然而，一旦占用率足以进行[延迟隐藏](/gpu-glossary/perf/latency-hiding)，进一步增加占用率实际上可能会降低性能。更高的占用率会减少每个[线程](/gpu-glossary/device-software/thread)的资源，可能导致[内核在寄存器上出现瓶颈](/gpu-glossary/perf/register-pressure)或降低现代GPU架构设计用来利用的[算术强度](/gpu-glossary/perf/arithmetic-intensity)。

更一般地说，占用率衡量的是GPU同时处理其最大并行任务的比例，这在大多数内核中本身并不是优化的目标。相反，如果我们处于[计算瓶颈](/gpu-glossary/perf/compute-bound)，我们希望最大化计算资源的[利用率](/gpu-glossary/perf/pipe-utilization)；如果我们处于[内存瓶颈](/gpu-glossary/perf/memory-bound)，我们希望最大化内存资源的利用率。

特别是，在Hopper和 Blackwell[架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)GPU上的高性能GEMM内核通常以个位数的占用率百分比运行，因为它们不需要很多[线程束](/gpu-glossary/device-software/warp)来完全饱和[张量核心](/gpu-glossary/device-hardware/tensor-core)。