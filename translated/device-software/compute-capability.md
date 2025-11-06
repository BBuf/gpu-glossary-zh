<!--
原文: 文件路径: gpu-glossary/device-software/compute-capability.md
翻译时间: 2025-11-06 18:39:12
-->

---
title: 什么是计算能力？
---

[并行线程执行 (Parallel Thread Execution)](/gpu-glossary/device-software/parallel-thread-execution) 指令集中的指令仅与特定的物理 GPU 兼容。用于从指令集和[编译器 (compiler)](/gpu-glossary/host-software/nvcc) 中抽象出物理 GPU 细节的版本控制系统被称为"计算能力 (Compute Capability)"。

大多数计算能力版本号包含两个组成部分：主版本号和次版本号。NVIDIA 承诺按照[洋葱层模型](https://docs.nvidia.com/cuda/parallel-thread-execution/#ptx-module-directives-target)，在主版本和次版本之间保持向前兼容性（旧的 [PTX](/gpu-glossary/device-software/parallel-thread-execution) 代码可在新 GPU 上运行）。

随着 Hopper 架构的推出，NVIDIA 引入了额外的版本后缀，即 `9.0a` 中的 `a`，它包含偏离洋葱模型的功能：即使在同一主版本内，其未来兼容性也不受保证。

随着 Blackwell 架构的推出，NVIDIA 引入了另一个版本后缀，即 `10.0f` 中的 `f`，它也偏离了洋葱模型，更接近[语义化版本 (SemVer)](https://semver.org/)：兼容性在次版本之间得到保证，但在主版本之间不保证。

在调用 [NVIDIA CUDA 编译器驱动程序 (NVIDIA CUDA Compiler Driver)](/gpu-glossary/host-software/nvcc) `nvcc` 时，可以指定 [PTX](/gpu-glossary/device-software/parallel-thread-execution) 编译的目标计算能力。默认情况下，编译器还会为匹配的[流式多处理器架构 (Streaming Multiprocessor architecture)](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture) 生成优化的 [SASS](/gpu-glossary/device-software/streaming-assembler)。[`nvcc`](/gpu-glossary/host-software/nvcc) 的[文档](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html#virtual-architectures)将计算能力称为"虚拟 GPU 架构"，与 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 版本表示的"物理 GPU 架构"形成对比。

每个计算能力版本的技术规格可以在 [NVIDIA CUDA C 编程指南的计算能力部分](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html)找到。