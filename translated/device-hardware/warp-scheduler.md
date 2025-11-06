<!--
原文: 文件路径: gpu-glossary/device-hardware/warp-scheduler.md
翻译时间: 2025-11-06 19:08:01
-->

---
title: 什么是线程束调度器？
---

线程束调度器是[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)的核心组件，负责在每个时钟周期决定执行哪一组[线程](/gpu-glossary/device-software/thread)。

![](https://files.mdnice.com/user/59/24190e9b-c268-40b0-b7e0-116a7034c57c.png)

> H100 SM 内部架构图。橙色部分为线程束调度器和分发单元。改编自 NVIDIA 的 [H100 白皮书](https://modal-cdn.com/gpu-glossary/gtc22-whitepaper-hopper.pdf)。

这些被称为[线程束](/gpu-glossary/device-software/warp)的线程组会在每个时钟周期（约一纳秒）进行切换——类似于 CPU 中同步多线程（"超线程"）的细粒度线程级并行处理，但规模更为庞大。线程束调度器能够在指令操作数就绪时快速切换大量并发任务，这种能力是实现 GPU [延迟隐藏](/gpu-glossary/perf/latency-hiding)特性的关键所在。

完整的 CPU 线程上下文切换需要数百到数千个时钟周期（更接近微秒级而非纳秒级），因为需要保存当前线程上下文并恢复另一个线程的上下文。此外，CPU 的上下文切换会降低数据局部性，通过增加缓存未命中率进一步影响性能（参见 [Mogul and Borg, 1991](https://www.researchgate.net/publication/220938995_The_Effect_of_Context_Switches_on_Cache_Performance)）。

由于每个[线程](/gpu-glossary/device-software/thread)都拥有从 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 的[寄存器文件](/gpu-glossary/device-hardware/register-file)分配的私有[寄存器](/gpu-glossary/device-software/registers)，GPU 的上下文切换无需任何数据移动来保存或恢复上下文。

而且由于 GPU 的 [L1 缓存](/gpu-glossary/device-hardware/l1-data-cache)可完全由程序员管理，并在共同调度到 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 的[线程束](/gpu-glossary/device-software/warp)之间[共享](/gpu-glossary/device-software/shared-memory)（参见[协作线程数组](/gpu-glossary/device-software/cooperative-thread-array)），GPU 的上下文切换对缓存命中率的影响要小得多。有关 GPU 中程序员管理缓存与硬件管理缓存交互的详细信息，请参阅 [CUDA C 编程指南的"最大化内存吞吐量"章节](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#maximize-memory-throughput)。

线程束调度器还负责管理[线程束的执行状态](/gpu-glossary/perf/warp-execution-state)。