<!--
原文: 文件路径: gpu-glossary/device-hardware/core.md
翻译时间: 2025-11-06 19:07:18
-->

---
title: 什么是 GPU 核心？
---

核心是构成[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)的主要计算单元。

![](https://files.mdnice.com/user/59/24190e9b-c268-40b0-b7e0-116a7034c57c.png)

> H100 GPU 流式多处理器内部架构示意图。GPU 核心显示为绿色，其他计算单元为栗色，调度单元为橙色，内存为蓝色。修改自 NVIDIA 的 [H100 白皮书](https://modal-cdn.com/gpu-glossary/gtc22-whitepaper-hopper.pdf)。

GPU 核心类型的示例包括 [CUDA 核心](/gpu-glossary/device-hardware/cuda-core)和 [Tensor 核心](/gpu-glossary/device-hardware/tensor-core)。

虽然 GPU 核心与 CPU 核心类似，都是执行实际计算的组件，但这种类比可能会产生误导。相反，从[定量计算机架构师](https://archive.org/details/computerarchitectureaquantitativeapproach6thedition)的角度来看，将它们视为数据流入并返回转换后数据的"管道"可能更有帮助。从硬件角度来看，这些管道与特定的[指令](/gpu-glossary/device-software/streaming-assembler)相关联；从程序员角度来看，则与不同的基础吞吐量能力相关（例如 [Tensor 核心](/gpu-glossary/device-hardware/tensor-core)的浮点矩阵乘法算术吞吐量）。

[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)更接近于 CPU 核心的对应物，因为它们具备存储信息的[寄存器内存](/gpu-glossary/device-hardware/register-file)、转换数据的核心，以及指定和命令转换的[指令调度器](/gpu-glossary/device-hardware/warp-scheduler)。