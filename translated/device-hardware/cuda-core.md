<!--
原文: 文件路径: gpu-glossary/device-hardware/cuda-core.md
翻译时间: 2025-11-06 19:01:35
-->

---
title: 什么是 CUDA 核心？
---

CUDA 核心是执行标量算术指令的 GPU [核心](/gpu-glossary/device-hardware/core)。

![](https://files.mdnice.com/user/59/24190e9b-c268-40b0-b7e0-116a7034c57c.png)

> H100 SM 的内部架构。CUDA 核心和张量核心以绿色显示。请注意张量核心尺寸更大且数量更少。改编自 NVIDIA 的 [H100 白皮书](https://modal-cdn.com/gpu-glossary/gtc22-whitepaper-hopper.pdf)。

它们与执行矩阵运算的[张量核心](/gpu-glossary/device-hardware/tensor-core)形成对比。

与 CPU 核心不同，发送到 CUDA 核心的指令通常不是独立调度的。相反，成组的核心会由[线程束调度器](/gpu-glossary/device-hardware/warp-scheduler)同时发出相同的指令，但将这些指令应用于不同的[寄存器](/gpu-glossary/device-software/registers)。通常，这些组的大小为 32，即一个[线程束](/gpu-glossary/device-software/warp)的大小，但对于现代 GPU，组可以包含少至一个线程，但这会以性能为代价。

"CUDA 核心"这个术语略有模糊性：在不同的[流式多处理器架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)中，CUDA 核心可以由不同的单元组成——即 32 位整数单元与 32 位和 64 位浮点单元的不同混合。或许最好通过与早期 GPU 的对比来理解它们，早期 GPU 包含各种更专业化的计算单元，映射到着色器流水线上（参见 [CUDA 设备架构](/gpu-glossary/device-hardware/cuda-device-architecture)）。

例如，[H100 白皮书](https://resources.nvidia.com/en-us-hopper-architecture/nvidia-h100-tensor-c)指出，H100 GPU 的每个[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor) 都有 128 个 "FP32 CUDA 核心"，这准确统计了 32 位浮点单元的数量，但却是 32 位整数或 64 位浮点单元数量的两倍（如上图所示）。为了估算性能，最好直接查看特定操作的硬件单元数量。