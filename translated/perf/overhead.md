<!--
原文: 文件路径: gpu-glossary/perf/overhead.md
翻译时间: 2025-11-06 18:44:08
-->

---
title: 什么是开销？
---

开销延迟是指未执行有用工作所花费的时间。

与在[计算限制](/gpu-glossary/perf/compute-bound)或[内存限制](/gpu-glossary/perf/memory-bound)下的[性能瓶颈](/gpu-glossary/perf/performance-bottleneck)期间不同——那时 GPU 正在尽可能快地工作——由开销引起的延迟代表 GPU 在等待接收工作的时间。

开销通常来自 CPU 端的瓶颈，这些瓶颈阻止 GPU 足够快地接收工作。例如，每个内核启动的 CUDA API 调用开销大约增加 10 微秒。此外，像 PyTorch 或 TensorFlow 这样的框架需要时间决定启动哪个[内核](/gpu-glossary/device-software/kernel)，这可能花费许多微秒。我们通常在这里使用术语"主机开销"，尽管它并非完全标准化。
[CUDA Graphs](https://developer.nvidia.com/blog/cuda-graphs/) 将多个设备端[内核](/gpu-glossary/device-software/kernel)集合成一个主机端启动，是解决这些开销的常见方案。更多信息，请参阅 [GTC 2025 上的《最大化并发和系统利用率的 CUDA 技术》演讲](https://www.nvidia.com/en-us/on-demand/session/gtc25-s72686/)。

"内存开销"或"通信开销"是在 CPU 与 GPU 之间或 GPU 与 GPU 之间来回移动数据时产生的开销延迟。但当通信带宽成为限制因素时，通常最好将其视为一种[内存限制](/gpu-glossary/perf/memory-bound)的形式，其中"内存"分布在多台机器上。