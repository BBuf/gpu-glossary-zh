<!--
原文: 文件路径: gpu-glossary/perf/littles-law.md
翻译时间: 2025-11-06 18:57:59
-->

---
title: 什么是利特尔法则？
---

利特尔法则确立了通过吞吐量完全[隐藏延迟 (hide latency)](/gpu-glossary/perf/latency-hiding)所需的并发量。

```
并发量 (操作数) = 延迟 (秒) * 吞吐量 (操作数/秒)
```

利特尔法则被[Lazowska等人所著的经典定量系统教科书](https://homes.cs.washington.edu/~lazowska/qsp/Images/Chap_03.pdf)描述为分析中"最重要的基本法则"。

利特尔法则决定了GPU需要通过[线程束调度器 (warp schedulers)](/gpu-glossary/device-hardware/warp-scheduler)进行[线程束 (warp)](/gpu-glossary/device-software/warp)切换（也称为细粒度线程级并行，类似于CPU中的[同步多线程](https://en.wikipedia.org/wiki/Simultaneous_multithreading)）来[隐藏延迟 (hide latency)](/gpu-glossary/perf/latency-hiding)时，必须有多少指令处于"执行中"状态。

如果GPU的峰值吞吐量为每周期1条指令，内存访问延迟为400个周期，那么程序中所有[活跃线程束 (active warps)](/gpu-glossary/perf/warp-execution-state)需要400个并发内存操作。如果吞吐量增加到每周期10条指令，那么程序需要4000个并发内存操作才能充分利用这种增长。更多细节请参阅关于[延迟隐藏 (latency hiding)](/gpu-glossary/perf/latency-hiding)的文章。

对于利特尔法则的一个非平凡应用，请考虑[Vasily Volkov博士论文](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2016/EECS-2016-143.pdf)第4.3节中关于[延迟隐藏 (latency hiding)](/gpu-glossary/perf/latency-hiding)的以下观察：隐藏纯内存访问延迟所需的线程束数量并不比隐藏纯算术延迟所需的线程束数量多太多（在他的实验中是30 vs 24）。直观上看，内存访问的较长延迟似乎需要更多并发性。但并发性不仅由延迟决定，还由吞吐量决定。由于[内存带宽 (memory bandwidth)](/gpu-glossary/perf/memory-bandwidth)远低于[算术带宽 (arithmetic bandwidth)](/gpu-glossary/perf/arithmetic-bandwidth)，所需的并发性结果大致相同——这对于面向[延迟隐藏 (latency hiding)](/gpu-glossary/perf/latency-hiding)且将混合执行算术和内存操作的系统来说，是一种有用的平衡形式。