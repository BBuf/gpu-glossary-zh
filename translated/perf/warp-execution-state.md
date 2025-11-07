<!--
原文: 文件路径: gpu-glossary/perf/warp-execution-state.md
翻译时间: 2025-11-06 18:45:34
-->

---
title: 什么是线程束执行状态？
---

运行[内核](/gpu-glossary/device-software/kernel)的[线程束](/gpu-glossary/device-software/warp)状态可通过多个非互斥的形容词来描述：活跃的、停滞的、符合条件的和被选中的。

![](https://files.mdnice.com/user/59/34f2af6b-b744-4fe2-9880-8883c5f83b38.png)

> 线程束执行状态通过颜色表示。图表灵感来源于 GTC 2025 的 [*CUDA Techniques to Maximize Compute and Instruction Throughput*](https://www.nvidia.com/en-us/on-demand/session/gtc25-s72685/) 演讲。

从[线程](/gpu-glossary/device-software/thread)开始执行，到[线程束](/gpu-glossary/device-software/warp)中的所有[线程](/gpu-glossary/device-software/thread)都从[内核](/gpu-glossary/device-software/kernel)退出为止，该[线程束](/gpu-glossary/device-software/warp)被认为是*活跃的*。活跃的[线程束](/gpu-glossary/device-software/warp)构成了一个资源池，[线程束调度器](/gpu-glossary/device-hardware/warp-scheduler)每个周期从中选择候选者来发射指令（即放入某个发射槽中）。

每个[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor) 上活跃[线程束](/gpu-glossary/device-software/warp)的最大数量因[架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)而异，并在 [NVIDIA 文档](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html?highlight=compute%2520capability#compute-capabilities)中针对[计算能力](/gpu-glossary/device-software/compute-capability)列出。例如，在具有[计算能力](/gpu-glossary/device-software/compute-capability) 9.0 的 H100 SXM GPU 上，每个 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 最多可以有 64 个活跃[线程束](/gpu-glossary/device-software/warp)（2048 个线程）。请注意，活跃的[线程束](/gpu-glossary/device-software/warp)不一定正在执行指令。在上图中，除了一个槽位+周期外，其余所有槽位+周期都有活跃的[线程束](/gpu-glossary/device-software/warp)——这表明了高[占用率](/gpu-glossary/perf/occupancy)。

一个*符合条件的*[线程束](/gpu-glossary/device-software/warp)是指一个活跃的[线程束](/gpu-glossary/device-software/warp)，它已准备好发射其下一条指令。要使一个[线程束](/gpu-glossary/device-software/warp)符合条件，必须满足以下所有条件：

-   下一条指令已被获取，
-   所需的执行单元可用，
-   所有指令依赖关系已解决，并且
-   没有同步屏障阻塞执行。

符合条件的[线程束](/gpu-glossary/device-software/warp)代表了[线程束调度器](/gpu-glossary/device-hardware/warp-scheduler)进行指令发射的即时候选者。在上图中，除了周期 n + 2 之外的所有周期都出现了符合条件的[线程束](/gpu-glossary/device-software/warp)。在许多周期内没有符合条件的[线程束](/gpu-glossary/device-software/warp)可能对性能不利，特别是当您主要使用像 [CUDA 核心](/gpu-glossary/device-hardware/cuda-core) 这样的低延迟算术单元时。

一个*停滞的*[线程束](/gpu-glossary/device-software/warp)是指一个活跃的[线程束](/gpu-glossary/device-software/warp)，由于未解决的依赖关系或资源冲突而无法发射其下一条指令。[线程束](/gpu-glossary/device-software/warp)因各种原因而停滞，包括：

-   执行依赖，即它们必须等待先前算术指令的结果，
-   内存依赖，即它们必须等待先前内存操作的结果，
-   流水线冲突，即执行资源当前被占用。

当线程束因访问共享内存或因执行长时间运行的算术指令而停滞时，我们称其停滞在"短计分板"上。当线程束因访问 GPU RAM 而停滞时，我们称其停滞在"长计分板"上。这些是[线程束调度器](/gpu-glossary/device-hardware/warp-scheduler)内部的硬件单元。[计分板](https://www.cs.umd.edu/~meesh/411/website/projects/dynamic/scoreboard.html)是一种在动态指令调度中用于跟踪依赖关系的技术，其历史可以追溯到"第一台超级计算机"——[Control Data Corporation 6600](https://en.wikipedia.org/wiki/CDC_6600)，其中一台在 1966 年[推翻了欧拉幂和猜想](https://www.ams.org/journals/bull/1966-72-06/S0002-9904-1966-11654-3/S0002-9904-1966-11654-3.pdf)。与 CPU 不同，计分板不用于[线程](/gpu-glossary/device-software/thread)内部的乱序执行（指令级并行），而只用于跨线程的执行（线程级并行）；参见[此 NVIDIA 专利](https://patents.google.com/patent/US7676657)。

在上图中，每个周期的多个槽位中都出现了停滞的[线程束](/gpu-glossary/device-software/warp)。停滞的[线程束](/gpu-glossary/device-software/warp)本身并不一定是坏事——大量并发停滞的[线程束](/gpu-glossary/device-software/warp)集合可能是[隐藏延迟](/gpu-glossary/perf/latency-hiding)所必需的，这些延迟来自长时间运行的指令，如内存加载或像 `HMMA` 这样的[张量核心](/gpu-glossary/device-hardware/tensor-core)指令，这些指令[可能运行数十个周期](https://arxiv.org/abs/2206.02874)。

一个*被选中的*[线程束](/gpu-glossary/device-software/warp)是指一个符合条件的[线程束](/gpu-glossary/device-software/warp)，它在当前周期被[线程束调度器](/gpu-glossary/device-hardware/warp-scheduler)选中以接收一条指令。每个周期，[线程束调度器](/gpu-glossary/device-hardware/warp-scheduler)会查看其符合条件的[线程束](/gpu-glossary/device-software/warp)资源池，如果存在任何符合条件的线程束，则选择一个并向其发射一条指令。在每个有符合条件的[线程束](/gpu-glossary/device-software/warp)的周期中，都有一个被选中的[线程束](/gpu-glossary/device-software/warp)。在[活跃周期](/gpu-glossary/perf/active-cycle)中，某个[线程束](/gpu-glossary/device-software/warp)被选中并发射指令的比例就是[发射效率](/gpu-glossary/perf/issue-efficiency)。