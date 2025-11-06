<!--
原文: 文件路径: gpu-glossary/perf/register-pressure.md
翻译时间: 2025-11-06 18:58:37
-->

---
title: 什么是寄存器压力？
---

寄存器压力是一个形象的说法，用于描述当[寄存器文件](/gpu-glossary/device-hardware/register-file)成为[性能瓶颈](/gpu-glossary/perf/performance-bottleneck)时的情况。

在[并行线程执行 (PTX)](/gpu-glossary/device-software/parallel-thread-execution)语言中，[寄存器](/gpu-glossary/device-software/registers)是虚拟且无数量限制的，但[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)的[寄存器文件](/gpu-glossary/device-hardware/register-file)是物理实体，因此数量有限。

[线程](/gpu-glossary/device-software/thread)消耗的[寄存器文件](/gpu-glossary/device-hardware/register-file)空间大小由[内核](/gpu-glossary/device-software/kernel)的[流式汇编器 (SASS)](/gpu-glossary/device-software/streaming-assembler)代码决定。由于[线程块](/gpu-glossary/device-software/thread-block)中的所有[线程](/gpu-glossary/device-software/thread)都被调度到同一个[SM](/gpu-glossary/device-hardware/streaming-multiprocessor)上执行，因此[线程块](/gpu-glossary/device-software/thread-block)所需的总空间也由[内核](/gpu-glossary/device-software/kernel)启动配置决定。随着每个[线程块](/gpu-glossary/device-software/thread-block)分配的空间增加，能够调度到同一个[SM](/gpu-glossary/device-hardware/streaming-multiprocessor)上的[线程块](/gpu-glossary/device-software/thread-block)数量就会减少，从而降低[占用率](/gpu-glossary/perf/occupancy)，并使得[延迟隐藏](/gpu-glossary/perf/latency-hiding)更加困难。

关于寄存器压力与近期[流式多处理器架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)新增关键特性（如Ampere架构添加的异步拷贝、Hopper架构添加的[张量内存加速器](/gpu-glossary/device-hardware/tensor-memory-accelerator)(TMA)以及Blackwell架构添加的[张量内存](/gpu-glossary/device-hardware/tensor-memory)）之间关系的详细说明，请参阅[SemiAnalysis的这篇优秀文章](https://semianalysis.com/2025/06/23/nvidia-tensor-core-evolution-from-volta-to-blackwell/)。

寄存器压力也存在于CPU中，类似的寄存器[瓶颈](/gpu-glossary/perf/performance-bottleneck)会限制循环在[自动向量化过程中进行条带挖掘](https://hogback.atmos.colostate.edu/rr/old/tidbits/intel/macintel/doc_files/source/extfile/optaps_for/common/optaps_vec_mine.htm)的程度。