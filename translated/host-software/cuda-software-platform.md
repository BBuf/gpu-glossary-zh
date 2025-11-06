<!--
原文: 文件路径: gpu-glossary/host-software/cuda-software-platform.md
翻译时间: 2025-11-06 18:29:14
-->

---
title: CUDA 软件平台是什么？
---

CUDA 代表 _Compute Unified Device Architecture_（计算统一设备架构）。根据上下文，
"CUDA" 可以指代多个不同的概念：一种
[高层设备架构](/gpu-glossary/device-hardware/cuda-device-architecture)，
一种
[针对该架构设计的并行编程模型](/gpu-glossary/device-software/cuda-programming-model)，
或是一个扩展高级语言（如 C）以支持该编程模型的软件平台。

CUDA 的愿景在
[Lindholm 等人，2008 年](https://www.cs.cmu.edu/afs/cs/academic/class/15869-f11/www/readings/lindholm08_tesla.pdf)
白皮书中进行了阐述。我们强烈推荐这篇论文，它是英伟达文档中许多声明、图表甚至特定措辞的原始来源。

这里，我们重点介绍 CUDA _软件平台_。

CUDA 软件平台是用于开发 CUDA 程序的一系列软件集合。虽然也存在针对其他语言（如 FORTRAN）的 CUDA 软件平台，但我们将重点介绍主流的
[CUDA C++](/gpu-glossary/host-software/cuda-c) 版本。

该平台大致可分为用于 _构建_ 应用程序的组件（如
[NVIDIA CUDA 编译器驱动](/gpu-glossary/host-software/nvcc) 工具链），
以及在应用程序中 _使用_ 或 _调用_ 的组件（如
[CUDA 驱动 API](/gpu-glossary/host-software/cuda-driver-api) 和
[CUDA 运行时 API](/gpu-glossary/host-software/cuda-runtime-api)），如下图所示。

![CUDA 工具包。改编自《Professional CUDA C Programming Guide》。](https://modal.com/_next/image?url=%2Fgpu-glossary%2Fcuda-toolkit.svg&w=1920&q=75)

在这些 API 之上构建的是用于为通用和特定领域构建优化
[内核 (kernel)](/gpu-glossary/device-software/kernel) 的库，
例如用于线性代数的 [cuBLAS](/gpu-glossary/host-software/cublas)
和用于深度神经网络的 [cuDNN](/gpu-glossary/host-software/cudnn)。