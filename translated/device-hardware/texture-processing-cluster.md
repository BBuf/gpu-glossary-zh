<!--
原文: 文件路径: gpu-glossary/device-hardware/texture-processing-cluster.md
翻译时间: 2025-11-06 19:04:07
-->

---
title: 什么是纹理处理集群？
abbreviation: TPC
---

纹理处理集群 (Texture Processing Cluster, TPC) 是一对相邻的[流式多处理器 (Streaming Multiprocessors, SMs)](/gpu-glossary/device-hardware/streaming-multiprocessor)。

在 Blackwell [SM 架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)之前，TPC 并未映射到 [CUDA 编程模型](/gpu-glossary/device-software/cuda-programming-model)的[内存层次结构](/gpu-glossary/device-software/memory-hierarchy)或[线程层次结构](/gpu-glossary/device-software/thread-hierarchy)的任何层级。

Blackwell [SM 架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)中的第五代 [Tensor Cores](/gpu-glossary/device-hardware/tensor-core) 在[并行线程执行 (Parallel Thread eXecution, PTX)](/gpu-glossary/device-software/parallel-thread-execution) 的[线程层次结构](/gpu-glossary/device-software/thread-hierarchy)中增加了 "CTA 对" 层级，该层级映射到 TPC。许多 `tcgen05` [PTX](/gpu-glossary/device-software/parallel-thread-execution) 指令包含一个 `.cta_group` 字段，可以使用单个 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) (`.cta_group::1`) 或 TPC 中的一对 [SMs](/gpu-glossary/device-hardware/streaming-multiprocessor) (`::2`)，这些分别映射到[流式汇编器 (Streaming Assembler, SASS)](/gpu-glossary/device-software/streaming-assembler) 指令（如 `MMA`）的 `1SM` 和 `2SM` 变体。