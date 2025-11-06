<!--
原文: 文件路径: gpu-glossary/device-software/warp.md
翻译时间: 2025-11-06 18:31:23
-->

---
title: 什么是线程束？
---

线程束 (Warp) 是一组被一起调度并并行执行的[线程](/gpu-glossary/device-software/thread)。一个线程束中的所有[线程](/gpu-glossary/device-software/thread)都被调度到单个[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor) 上。单个 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 通常执行多个线程束，至少包括来自同一个[协作线程阵列](/gpu-glossary/device-software/cooperative-thread-array)（也称为[线程块](/gpu-glossary/device-software/thread-block)）的所有线程束。

线程束是 GPU 上典型的执行单元。在正常执行过程中，线程束的所有[线程](/gpu-glossary/device-software/thread)并行执行相同的指令——这就是所谓的"单指令多线程"或 SIMT 模型。当线程束中的[线程](/gpu-glossary/device-software/thread)分道扬镳执行不同指令时（也称为[线程束分化](/gpu-glossary/perf/warp-divergence)），性能通常会急剧下降。

线程束大小在技术上是与机器相关的常数，但在实践中（以及本词汇表的其他地方）它是 32。

当线程束被发出指令时，结果通常无法在单个时钟周期内获得，因此无法发出相关指令。虽然这对于从[全局内存](/gpu-glossary/device-software/global-memory)的读取最为明显（通常需要[离开芯片](/gpu-glossary/device-hardware/gpu-ram)），但对于某些算术指令也是如此（请参阅[CUDA C++ 最佳实践指南](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html#arithmetic-instructions)了解特定指令每个时钟周期的结果表）。

下一个指令因缺少操作数而延迟的线程束被称为[停滞](/gpu-glossary/perf/warp-execution-state)。

当多个线程束被调度到单个 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 上时，[线程束调度器](/gpu-glossary/device-hardware/warp-scheduler)不会等待指令结果返回，而是选择另一个线程束执行。这种[延迟隐藏](/gpu-glossary/perf/latency-hiding)是 GPU 实现高吞吐量并确保执行期间所有核心始终有工作可用的方式。因此，最大化调度到每个 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 上的线程束数量通常是有益的，确保始终有[符合条件的](/gpu-glossary/perf/warp-execution-state)线程束供 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 运行。线程束被发出指令的周期比例称为[发射效率](/gpu-glossary/perf/issue-efficiency)。线程束调度中的并发程度称为[占用率](/gpu-glossary/perf/occupancy)。

线程束实际上并不是 [CUDA 编程模型](/gpu-glossary/device-software/cuda-programming-model)的[线程层次结构](/gpu-glossary/device-software/thread-hierarchy)的一部分。相反，它们是在 NVIDIA GPU 上实现该模型的实现细节。从这个意义上说，它们有点类似于 CPU 中的[缓存行](https://www.nic.uoregon.edu/~khuck/ts/acumem-report/manual_html/ch03s02.html)：一种您不直接控制且不需要考虑程序正确性的硬件特性，但对于实现[最佳性能](/gpu-glossary/perf)很重要。

根据 [Lindholm 等人，2008](https://www.cs.cmu.edu/afs/cs/academic/class/15869-f11/www/readings/lindholm08_tesla.pdf)，线程束的命名参考了编织——"第一种并行线程技术"。其他 GPU 编程模型中与线程束等效的概念包括 WebGPU 中的[子组](https://github.com/gpuweb/gpuweb/pull/4368)、DirectX 中的[波阵面](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_SM_6_6_WaveSize.html)以及 Metal 中的[simdgroups](https://developer.apple.com/documentation/metal/compute_passes/creating_threads_and_threadgroups#2928931)。