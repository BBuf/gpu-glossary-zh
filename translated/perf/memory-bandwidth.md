<!--
原文: 文件路径: gpu-glossary/perf/memory-bandwidth.md
翻译时间: 2025-11-06 18:52:00
-->

---
title: 什么是内存带宽？
---

内存带宽是指数据在[内存层次结构](/gpu-glossary/device-software/memory-hierarchy)的不同层级之间传输的最大速率。

它代表了以字节/秒为单位移动数据时理论上可达到的最大吞吐量。它决定了硬件[屋顶线模型](/gpu-glossary/perf/roofline-model)中"内存屋顶"的斜率。

在一个完整的系统中有许多内存带宽——[内存层次结构](/gpu-glossary/device-software/memory-hierarchy)的每一层级之间都有一个带宽。

最重要的带宽是[GPU显存](/gpu-glossary/device-hardware/gpu-ram)与[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)的[寄存器文件](/gpu-glossary/device-hardware/register-file)之间的带宽，因为大多数[内核](/gpu-glossary/device-software/kernel)的[工作集](https://en.wikipedia.org/wiki/Working_set_size)只能存放在[GPU显存](/gpu-glossary/device-software/memory-hierarchy)中，而无法放在[内存层次结构](/gpu-glossary/device-software/memory-hierarchy)中更高的层级。正是由于这个原因，在GPU[内核](/gpu-glossary/device-software/kernel)性能的[屋顶线建模](/gpu-glossary/perf/roofline-model)中，该带宽是主要使用的带宽。

当代GPU的内存带宽以TB/秒为单位进行测量。例如，[B200 GPU](https://modal.com/blog/introducing-b200-h200)与其HBM3e内存之间的（双向）内存带宽为8 TB/秒。这远低于这些GPU中[张量核心](/gpu-glossary/device-hardware/tensor-core)的[算术带宽](/gpu-glossary/perf/arithmetic-bandwidth)，从而导致[屋顶线模型](/gpu-glossary/perf/roofline-model)中的[脊点](/gpu-glossary/perf/roofline-model)所需的[算术强度](/gpu-glossary/perf/arithmetic-intensity)增加。

下表列出了从Ampere到Blackwell[流式多处理器架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)的NVIDIA数据中心GPU的代表性带宽数值。

| **系统（计算/内存）**                                                                                                                               | **[算术带宽](/gpu-glossary/perf/arithmetic-bandwidth) (TFLOPs/s)** | **内存带宽 (TB/s)** | **[脊点](/gpu-glossary/perf/roofline-model) (FLOPs/byte)** |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------- | -----------------------------------------------------------------------------: | --------------------------: | ----------------------------------------------------------------: |
| [A100 80GB SXM BF16 TC / HBM2e](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf) |                                                                            312 |                           2 |                                                               156 |
| [H100 SXM BF16 TC / HBM3](https://resources.nvidia.com/en-us-gpu-resources/h100-datasheet-24306)                                                            |                                                                            989 |                        3.35 |                                                               295 |
| [B200 BF16 TC / HBM3e](https://resources.nvidia.com/en-us-dgx-systems/dgx-b200-datasheet)                                                                   |                                                                           2250 |                           8 |                                                               281 |
| [H100 SXM FP8 TC / HBM3](https://resources.nvidia.com/en-us-gpu-resources/h100-datasheet-24306)                                                             |                                                                           1979 |                        3.35 |                                                               592 |
| [B200 FP8 TC / HBM3e](https://resources.nvidia.com/en-us-dgx-systems/dgx-b200-datasheet)                                                                    |                                                                           4500 |                           8 |                                                               562 |
| [B200 FP4 TC / HBM3e](https://resources.nvidia.com/en-us-dgx-systems/dgx-b200-datasheet)                                                                    |                                                                           9000 |                           8 |                                                              1125 |