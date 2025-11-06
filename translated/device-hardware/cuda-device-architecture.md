<!--
原文: 文件路径: gpu-glossary/device-hardware/cuda-device-architecture.md
翻译时间: 2025-11-06 18:59:25
-->

---
title: 什么是 CUDA 设备架构？
---

CUDA 代表 _Compute Unified Device Architecture_（计算统一设备架构）。根据上下文，"CUDA" 可以指代多个不同的事物：一种高级设备架构、针对该架构设计的[并行编程模型](/gpu-glossary/device-software/cuda-programming-model)，或是扩展高级语言（如 C 语言）以添加该编程模型的[软件平台](/gpu-glossary/host-software/cuda-software-platform)。

CUDA 的愿景在 [Lindholm 等人于 2008 年](https://www.cs.cmu.edu/afs/cs/academic/class/15869-f11/www/readings/lindholm08_tesla.pdf)发布的白皮书中进行了阐述。我们强烈推荐这篇论文，它是 NVIDIA 文档中许多论断、图表乃至特定措辞的原始来源。

在此，我们重点关注 CUDA 的 _设备架构_ 部分。"计算统一设备架构"的核心特性是相对于先前的 GPU 架构而言的简洁性。

在 GeForce 8800 及其衍生的 Tesla 数据中心 GPU 之前，NVIDIA GPU 采用复杂的管线着色器架构设计，该架构将软件着色器阶段映射到异构的、专门的硬件单元上。这种架构对软件和硬件工程师都构成了挑战：它要求软件工程师将程序映射到固定管线，并迫使硬件工程师猜测管线各步骤间的负载比例。


![](https://files.mdnice.com/user/59/74675656-a0d7-4c7a-a354-67b33aa2e9b7.png)

> 固定管线设备架构示意图 (G71)。请注意存在用于处理片段和顶点着色的独立处理器组。改编自 [Fabien Sanglard 的博客](https://fabiensanglard.net/cuda/)。

采用统一架构的 GPU 设备则要简单得多：其硬件单元完全统一，每个单元都能够执行多种计算。这些单元被称为[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)，它们的主要子组件是 [CUDA 核心](/gpu-glossary/device-hardware/cuda-core)以及（对于近期的 GPU）[张量核心](/gpu-glossary/device-hardware/tensor-core)。

![](https://files.mdnice.com/user/59/be06d295-4bee-4c05-95b4-e4b9d119af99.png)

> 计算统一设备架构示意图 (G80)。请注意没有不同的处理器类型——所有有意义的计算都发生在图中央相同的[流式多处理器](/gpu-glossary/device-hardware/streaming-multiprocessor)中，这些处理器接收针对顶点、几何和像素线程的指令。修改自 [Peter Glazkowsky 2009 年关于 Fermi 架构的白皮书](https://www.nvidia.com/content/pdf/fermi_white_papers/p.glaskowsky_nvidia%27s_fermi-the_first_complete_gpu_architecture.pdf)。

关于 CUDA 硬件架构的历史和设计的通俗介绍，请参阅 Fabien Sanglard 的[这篇博客文章](https://fabiensanglard.net/cuda/)。该博客文章引用了其（高质量的）来源，例如 NVIDIA 的 [Fermi 计算架构白皮书](https://www.nvidia.com/content/pdf/fermi_white_papers/nvidia_fermi_compute_architecture_whitepaper.pdf)。由 [Lindholm 等人在 2008 年](https://www.cs.cmu.edu/afs/cs/academic/class/15869-f11/www/readings/lindholm08_tesla.pdf)介绍 Tesla 架构的白皮书既写得好又详尽。NVIDIA 关于 [Tesla P100 的白皮书](https://images.nvidia.com/content/pdf/tesla/whitepaper/pascal-architecture-whitepaper.pdf)学术性稍弱，但记录了对于当今大规模神经网络工作负载至关重要的一系列特性的引入，例如 NVLink 和[封装内高带宽内存](/gpu-glossary/device-hardware/gpu-ram)。