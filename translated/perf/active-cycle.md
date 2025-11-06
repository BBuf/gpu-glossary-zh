<!--
原文: 文件路径: gpu-glossary/perf/active-cycle.md
翻译时间: 2025-11-06 18:48:46
-->

---
title: 什么是活动周期？
---

活动周期是指一个时钟周期，在该周期内，[流式多处理器 (Streaming Multiprocessor)](/gpu-glossary/device-hardware/streaming-multiprocessor) 中至少驻留有一个[活动线程束 (active warp)](/gpu-glossary/perf/warp-execution-state)。该[线程束 (warp)](/gpu-glossary/device-software/warp) 可能处于[就绪 (eligible)](/gpu-glossary/perf/warp-execution-state) 或[停滞 (stalled)](/gpu-glossary/perf/warp-execution-state) 状态。

![](https://files.mdnice.com/user/59/d23a7691-199b-4580-a351-9dda7417bb73.png)

> 此图中描绘的所有周期都是活动周期。图表灵感来源于 GTC 2025 上的 [*CUDA Techniques to Maximize Compute and Instruction Throughput*](https://www.nvidia.com/en-us/on-demand/session/gtc25-s72685/) 演讲。

