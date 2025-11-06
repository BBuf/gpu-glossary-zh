<!--
原文: 文件路径: gpu-glossary/perf/issue-efficiency.md
翻译时间: 2025-11-06 18:42:55
-->

---
title: 什么是发射效率？
---

发射效率 (Issue efficiency) 衡量的是[线程束调度器](/gpu-glossary/device-hardware/warp-scheduler)通过从[合格线程束](/gpu-glossary/perf/warp-execution-state)发射指令来保持执行流水线繁忙的有效程度。

![](https://files.mdnice.com/user/59/17b78aa8-e57b-497f-be43-5f2c16853c17.png)

> 在此图的四个时钟周期中，有三个周期发射了指令，因此发射效率为75%。该图灵感来源于GTC 2025上的[*CUDA Techniques to Maximize Compute and Instruction Throughput*](https://www.nvidia.com/en-us/on-demand/session/gtc25-s72685/)演讲。

100%的发射效率意味着每个[调度器](/gpu-glossary/device-hardware/warp-scheduler)在每个周期都发射了一条指令，表明每个周期至少有一个[合格线程束](/gpu-glossary/perf/warp-execution-state)。低于100%的数值表明，在某些周期内，所有[活跃线程束](/gpu-glossary/perf/warp-execution-state)都处于[停滞状态](/gpu-glossary/perf/warp-execution-state)——正在等待数据、资源或依赖关系——因此[调度器](/gpu-glossary/device-hardware/warp-scheduler)处于空闲状态，整体指令吞吐量下降。