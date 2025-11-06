<!--
原文: 文件路径: gpu-glossary/perf/peak-rate.md
翻译时间: 2025-11-06 18:46:02
-->

---
title: 什么是峰值速率？
---

峰值速率是指硬件系统能够完成工作的理论最大速率。

峰值速率代表了当每个执行单元都以最高效率满负荷运行时，GPU 性能的绝对上限。它假设的是理想运行状态，即没有任何资源限制（如[寄存器](/gpu-glossary/device-software/registers)、[内存带宽](/gpu-glossary/perf/memory-bandwidth)、同步屏障等）造成[性能瓶颈](/gpu-glossary/perf/performance-bottleneck)。

峰值速率是衡量所有已实现性能的标尺。它在[屋顶线模型](/gpu-glossary/perf/roofline-model)中设定了[计算受限](/gpu-glossary/perf/compute-bound)的"屋顶"。它是在[流水线利用率](/gpu-glossary/perf/pipe-utilization)指标中报告的利用率分数的分母，也是[GPU 利用率的最终仲裁者](https://modal.com/blog/gpu-utilization-guide)。

富有诗意的是，NVIDIA 工程师通常称之为"光速"——这是由物理定律所决定的程序速度极限。

峰值速率是直接根据每个 GPU 架构的固定硬件规格计算得出的。

例如，一个具有 132 个流式多处理器 (SM) 的 [NVIDIA H100 GPU](https://resources.nvidia.com/en-us-hopper-architecture/nvidia-h100-tensor-c)，每个 SM 包含 128 个 FP32 核心，每个核心可以发出 1 个单精度融合乘加 (`FMA`) 操作，该操作包含 2 个浮点运算。这相当于每时钟周期 33,792 条[指令](https://en.wikipedia.org/wiki/Instructions_per_cycle)。当使用 FP32 核心时，H100 可以使其计算子系统时钟以最高 1980 MHz（每秒百万时钟周期）的速率运行，因此峰值速率为 66,908 亿 FLOPS，即 66.9 TFLOPS。

这与 [NVIDIA H100 白皮书](https://resources.nvidia.com/en-us-hopper-architecture/nvidia-h100-tensor-c)中宣传的峰值 FP32 TFLOPS（非 Tensor）速率完全吻合。