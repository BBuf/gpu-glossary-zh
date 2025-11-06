<!--
原文: 文件路径: gpu-glossary/device-hardware/tensor-memory.md
翻译时间: 2025-11-06 19:02:13
-->

---
title: 什么是 Tensor Memory？
---

Tensor Memory（张量内存）是某些 GPU（如 [B200](https://modal.com/blog/introducing-b200-h200)）的[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor) 中的一种专用内存，用于存储 [Tensor Core](/gpu-glossary/device-hardware/tensor-core) 的输入和输出。

Tensor Memory 的访问受到严格限制。数据必须由 warpgroup 中的四个[线程束 (warp)](/gpu-glossary/device-software/warp) 共同移动，并且它们只能在 Tensor Memory 与[寄存器 (register)](/gpu-glossary/device-software/registers) 之间以特定模式移动内存、将[共享内存 (shared memory)](/gpu-glossary/device-software/shared-memory) 写入 Tensor Memory，或者向使用 Tensor Memory 作为特定操作数的 [Tensor Core](/gpu-glossary/device-hardware/tensor-core) 发出矩阵乘加 (MMA) 指令。这对于["统一计算"设备架构](/gpu-glossary/device-hardware/cuda-device-architecture)来说限制颇多！

具体来说，对于计算 `D += A @ B` 的 `tcgen05.mma` [并行线程执行 (Parallel Thread eXecution)](/gpu-glossary/device-software/parallel-thread-execution) 指令要使用 Tensor Memory，"累加器"矩阵 `D` *必须* 位于 Tensor Memory 中，左侧矩阵 `A` *可以* 位于 Tensor Memory 或[共享内存 (shared memory)](/gpu-glossary/device-software/shared-memory) 中，而右侧矩阵 B *必须* 位于[共享内存 (shared memory)](/gpu-glossary/device-software/shared-memory) 中，而非 Tensor Memory。这很复杂，但并非随意规定——在矩阵乘法运算期间，累加器的访问频率高于矩阵分块，因此它们从专用硬件（例如 [Tensor Core](/gpu-glossary/device-hardware/tensor-core) 与 Tensor Memory 之间更短、更简单的布线）中获益更多。请注意，所有矩阵都不在[寄存器 (register)](/gpu-glossary/device-software/registers) 中。

注意：Tensor Memory 与 [Tensor Memory Accelerator](/gpu-glossary/device-hardware/tensor-memory-accelerator) 没有直接关系，后者是将数据加载到 [L1 数据缓存](/gpu-glossary/device-hardware/l1-data-cache)中。粗略地说，数据从该缓存移动到 Tensor Memory 仅作为 [Tensor Core](/gpu-glossary/device-hardware/tensor-core) 操作的结果，然后被显式移出以进行后处理，例如神经网络中矩阵乘法之后的非线性激活。

有关张量内存及其在矩阵乘法中使用模式的详细信息，请参阅 [GTC 2025 的《使用 CUTLASS 编程 Blackwell Tensor Core》演讲](https://www.nvidia.com/en-us/on-demand/session/gtc25-s72720/)。