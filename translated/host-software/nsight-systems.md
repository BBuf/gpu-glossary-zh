<!--
原文: 文件路径: gpu-glossary/host-software/nsight-systems.md
翻译时间: 2025-11-06 18:29:59
-->

---
title: 什么是 NVIDIA Nsight Systems？
---

NVIDIA Nsight Systems 是一款用于 [CUDA C++](/gpu-glossary/host-software/cuda-c) 程序的性能调试工具。它将性能分析、追踪和专家系统分析功能集成在图形用户界面 (GUI) 中。

没有人会一觉醒来就说"今天我要用专有软件栈在难以使用且昂贵的硬件上编写程序"。相反，当传统计算硬件无法以足够好的性能解决计算问题时，才会选择 GPU。因此[几乎所有 GPU 程序都对性能敏感](/gpu-glossary/perf)，而 Nsight Systems 或基于 [CUDA 性能分析工具接口](/gpu-glossary/host-software/cupti) 构建的其他工具所支持的性能调试工作流程就显得至关重要。

您可以在[此处](https://docs.nvidia.com/nsight-systems/index.html)找到其文档，但通常[观看他人使用该工具](https://www.youtube.com/watch?v=dUDGO66IadU)会更有帮助。有关如何在 Modal 上分析 GPU 应用程序的详细信息，请参阅[我们的文档](https://modal.com/docs/examples/nsys)。