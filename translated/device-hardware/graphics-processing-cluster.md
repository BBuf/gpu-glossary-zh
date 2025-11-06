<!--
原文: 文件路径: gpu-glossary/device-hardware/graphics-processing-cluster.md
翻译时间: 2025-11-06 19:02:38
-->

---
title: 什么是图形/GPU处理集群？
abbreviation: GPC
---

GPC 是一组[纹理处理集群 (TPC)](/gpu-glossary/device-hardware/texture-processing-cluster)（本身由[流式多处理器 (Streaming Multiprocessor)](/gpu-glossary/device-hardware/streaming-multiprocessor)或 SM 组成）加上一个光栅引擎的集合。显然，有些人使用 NVIDIA GPU 进行图形处理，这时光栅引擎就很重要。相关地，该名称过去代表图形处理集群 (Graphics Processing Cluster)，但现在（例如在[NVIDIA CUDA C++编程指南](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html)中）被扩展为"GPU 处理集群"。

自引入[计算能力 (compute capability)](/gpu-glossary/device-software/compute-capability) 9.0 GPU（如 H100）以来，[CUDA 编程模型 (CUDA programming model)](/gpu-glossary/device-software/cuda-programming-model)的[线程层次结构 (thread hierarchy)](/gpu-glossary/device-software/thread-hierarchy)增加了一个额外层级，即一个[线程块 (thread block)](/gpu-glossary/device-software/thread-block)的"集群"，这些线程块被调度到同一个 GPC 上，就像[线程块 (thread block)](/gpu-glossary/device-software/thread-block)的线程被调度到同一个[SM](/gpu-glossary/device-hardware/streaming-multiprocessor)上一样，并且它们拥有自己层级的[内存层次结构 (memory hierarchy)](/gpu-glossary/device-software/memory-hierarchy)——分布式共享内存。在其他地方，我们略去了对此功能的讨论。