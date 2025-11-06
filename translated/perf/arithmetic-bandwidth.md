<!--
原文: 文件路径: gpu-glossary/perf/arithmetic-bandwidth.md
翻译时间: 2025-11-06 18:49:34
-->

---
title: 什么是算术带宽？
---

算术带宽是指系统执行算术工作的[峰值速率](/gpu-glossary/perf/peak-rate)。

它代表了每秒算术操作可实现吞吐量的理论最大值，决定了硬件[屋顶模型](/gpu-glossary/perf/roofline-model)中"计算屋顶"的高度。

在一个完整系统中有多种算术带宽——每组提供算术操作执行带宽的硬件单元都有对应的算术带宽。

在许多 GPU 中，最重要的算术带宽是[CUDA 核心](/gpu-glossary/device-hardware/cuda-core)的浮点算术带宽。GPU 通常为浮点操作提供的带宽高于整数操作，而[统一计算设备架构 (CUDA)](/gpu-glossary/device-hardware/cuda-device-architecture)的关键在于[CUDA 核心](/gpu-glossary/device-hardware/cuda-core)及其支持系统为 GPU 应用程序提供了统一的计算接口（与早期的 GPU 架构不同）。

但在近期的 GPU 中，随着[张量核心](/gpu-glossary/device-hardware/tensor-core)的引入，架构的统一性有所减弱。张量核心仅执行矩阵乘法运算，但其算术带宽远高于[CUDA 核心](/gpu-glossary/device-hardware/cuda-core)——[张量核心](/gpu-glossary/device-hardware/tensor-core)与[CUDA 核心](/gpu-glossary/device-hardware/cuda-core)带宽的比例通常约为 100:1。这使得[张量核心](/gpu-glossary/device-hardware/tensor-core)的算术带宽对于希望最大化性能的[内核](/gpu-glossary/device-software/kernel)最为重要。

当代 GPU 的[张量核心](/gpu-glossary/device-hardware/tensor-core)算术带宽以 petaFLOPS（每秒千万亿次浮点运算）为单位。例如，[B200 GPU](https://modal.com/blog/introducing-b200-h200)在运行 4 位浮点矩阵乘法时的带宽为 9 PFLOPS。

下表列出了 NVIDIA 数据中心 GPU 从安培到布莱克威尔[流式多处理器架构 (Streaming Multiprocessor Architecture)](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)的代表性带宽数据。

| **系统 (计算 / 内存)**                                                                                                                               | **算术带宽 (TFLOPs/秒)** | **[内存带宽](/gpu-glossary/perf/memory-bandwidth) (TB/秒)** | **[屋脊点](/gpu-glossary/perf/roofline-model) (FLOPs/字节)** |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------: | -----------------------------------------------------------------: | ----------------------------------------------------------------: |
| [A100 80GB SXM BF16 TC / HBM2e](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf) |                                 312 |                                                                  2 |                                                               156 |
| [H100 SXM BF16 TC / HBM3](https://resources.nvidia.com/en-us-gpu-resources/h100-datasheet-24306)                                                            |                                 989 |                                                               3.35 |                                                               295 |
| [B200 BF16 TC / HBM3e](https://resources.nvidia.com/en-us-dgx-systems/dgx-b200-datasheet)                                                                   |                                2250 |                                                                  8 |                                                               281 |
| [H100 SXM FP8 TC / HBM3](https://resources.nvidia.com/en-us-gpu-resources/h100-datasheet-24306)                                                             |                                1979 |                                                               3.35 |                                                               592 |
| [B200 FP8 TC / HBM3e](https://resources.nvidia.com/en-us-dgx-systems/dgx-b200-datasheet)                                                                    |                                4500 |                                                                  8 |                                                               562 |
| [B200 FP4 TC / HBM3e](https://resources.nvidia.com/en-us-dgx-systems/dgx-b200-datasheet)                                                                    |                                9000 |                                                                  8 |                                                              1125 |