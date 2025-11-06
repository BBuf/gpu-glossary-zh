<!--
原文: 文件路径: gpu-glossary/host-software/cupti.md
翻译时间: 2025-11-06 18:28:20
-->

---
title: 什么是 NVIDIA CUDA 性能分析工具接口？
abbreviation: CUPTI
---

NVIDIA CUDA 性能分析工具接口 (CUPTI) 提供了一组 API，用于分析在 GPU 上执行的 [CUDA C++](/gpu-glossary/host-software/cuda-c)、[PTX](/gpu-glossary/device-software/parallel-thread-execution) 和 [SASS](/gpu-glossary/device-software/streaming-assembler) 代码。关键在于，它能在 CPU 主机和 GPU 设备之间同步时间戳。

CUPTI 的接口被诸如 [NSight Systems 性能分析器](/gpu-glossary/host-software/nsight-systems) 和 [PyTorch Profiler](https://modal.com/docs/examples/torch_profiling) 等工具所使用。

您可以在[此处](https://docs.nvidia.com/cupti/)找到其文档。

有关在 Modal 上运行的 GPU 应用程序使用性能分析工具的详细信息，请参阅[我们文档中的此示例](/docs/examples/torch_profiling)。