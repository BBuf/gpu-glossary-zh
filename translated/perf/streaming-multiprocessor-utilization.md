<!--
原文: 文件路径: gpu-glossary/perf/streaming-multiprocessor-utilization.md
翻译时间: 2025-11-06 18:48:04
-->

---
title: 什么是 SM 利用率？
---

SM 利用率衡量的是[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)执行指令的时间百分比。

SM 利用率类似于更常见的[`nvidia-smi`](/gpu-glossary/host-software/nvidia-smi)报告的[内核利用率](https://modal.com/blog/gpu-utilization-guide)，但粒度更细。它不再报告[内核](/gpu-glossary/device-software/kernel)在 GPU 上任何位置执行的时间比例，而是报告所有[SM](/gpu-glossary/device-hardware/streaming-multiprocessor)执行[内核](/gpu-glossary/device-software/kernel)的时间比例。如果一个[内核](/gpu-glossary/device-software/kernel)仅使用一个[SM](/gpu-glossary/device-hardware/streaming-multiprocessor)（例如，因为它只有一个[线程块](/gpu-glossary/device-software/thread-block)），那么在其活动期间它将达到 100% 的 GPU 利用率，但 SM 利用率最多仅为 SM 总数的倒数——在 H100 GPU 中低于 1%。

[与 GPU 利用率类似但不同于 CPU 利用率](https://modal.com/blog/gpu-utilization-guide)，SM 利用率应该很高，甚至可以达到 100%。

但尽管 SM 利用率比 GPU 利用率粒度更细，它仍然不足以捕捉 GPU 计算资源的使用效率。如果 SM 利用率很高，但性能仍然不足，程序员应检查[流水线利用率](/gpu-glossary/perf/pipe-utilization)，该指标衡量每个 SM 使用其内部功能单元的效能。高 SM 利用率伴随低[流水线利用率](/gpu-glossary/perf/pipe-utilization)表明您的[内核](/gpu-glossary/device-software/kernel)正在许多 SM 上运行，但未能充分利用每个 SM 内的计算资源。