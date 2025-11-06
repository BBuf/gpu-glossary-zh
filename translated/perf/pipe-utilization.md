<!--
原文: 文件路径: gpu-glossary/perf/pipe-utilization.md
翻译时间: 2025-11-06 18:48:33
-->

---
title: 什么是流水线利用率？
---

流水线利用率衡量的是[内核 (kernel)](/gpu-glossary/device-software/kernel)在每个[流式多处理器 (Streaming Multiprocessor, SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)内使用执行资源的效率。

每个[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)包含多个独立的执行流水线，这些流水线针对不同的指令类型进行了优化——[CUDA 核心 (CUDA Cores)](/gpu-glossary/device-hardware/cuda-core)用于通用浮点运算，[张量核心 (Tensor Cores)](/gpu-glossary/device-hardware/tensor-core)用于张量收缩，[加载/存储单元 (load/store units)](/gpu-glossary/device-hardware/load-store-unit)用于内存访问，以及用于分支的控制流单元。流水线利用率显示了当某个流水线至少有一个[线程束 (warp)](/gpu-glossary/device-software/warp)在执行时，该流水线达到其[峰值速率 (peak rate)](/gpu-glossary/perf/peak-rate)的百分比，这个值是所有活跃[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)上的平均值。

在从流水线利用率层面调试应用程序性能之前，GPU 程序员应首先考虑[GPU 内核利用率](https://modal.com/blog/gpu-utilization-guide)和[流式多处理器利用率 (SM utilization)](/gpu-glossary/perf/streaming-multiprocessor-utilization)。

流水线利用率可以通过 [NSight Compute](https://developer.nvidia.com/nsight-compute) (`ncu`) 中的 `sm__inst_executed_pipe_*.avg.pct_of_peak_sustained_active` 指标获取，其中星号代表特定的流水线，例如 [`fma`](/gpu-glossary/device-hardware/cuda-core)、[`tensor`](/gpu-glossary/device-hardware/tensor-core)、[`lsu`](/gpu-glossary/device-hardware/load-store-unit) 或 `adu`（地址）。