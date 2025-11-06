<!--
原文: 文件路径: gpu-glossary/host-software/cudnn.md
翻译时间: 2025-11-06 18:26:57
-->

---
title: 什么是 cuDNN？
---

NVIDIA 的 cuDNN（CUDA 深度神经网络）是一个用于构建 GPU 加速的深度神经网络的基元库。

cuDNN 为神经网络中频繁出现的操作提供了高度优化的[内核](/gpu-glossary/device-software/kernel)。这些操作包括卷积、自注意力（包括缩放点积注意力，又称 "Flash Attention"）、矩阵乘法、各种归一化、池化等。

cuDNN 是[CUDA 软件平台](/gpu-glossary/host-software/cuda-software-platform)应用层的关键库，与其姊妹库 [cuBLAS](/gpu-glossary/host-software/cublas) 并列。像 PyTorch 这样的深度学习框架通常利用 [cuBLAS](/gpu-glossary/host-software/cublas) 进行通用线性代数运算，例如构成密集（全连接）层核心的矩阵乘法。它们依赖 cuDNN 来处理更专业的基元，如卷积层、归一化例程和注意力机制。

在现代 cuDNN 代码中，计算被表示为操作图，可以使用开源的 [Python 和 C++ 前端 API](https://docs.nvidia.com/deeplearning/cudnn/frontend/latest/developer/overview.html) 通过声明式的 [Graph API](https://docs.nvidia.com/deeplearning/cudnn/frontend/v1.14.0/developer/graph-api.html) 来构建。

该 API 允许开发者将一系列操作定义为一个图，cuDNN 随后可以分析该图以执行优化，最重要的是操作融合。在操作融合中，像卷积 + 偏置 + ReLU 这样的操作序列被合并（"融合"）成一个单一操作，作为单个[内核](/gpu-glossary/device-software/kernel)运行。操作融合通过在整个操作序列中将程序中间结果保留在[共享内存](/gpu-glossary/device-software/shared-memory)中，有助于减少对[内存带宽](/gpu-glossary/perf/memory-bandwidth)的需求。

这些前端与一个较低级别的闭源 [C 后端](https://docs.nvidia.com/deeplearning/cudnn/backend/latest/api/overview.html)交互，该后端为传统用例或直接的 C FFI 暴露了一个 API。

对于任何给定的操作，cuDNN 维护多个底层实现，并使用（未知的）内部启发式方法为目标[流式多处理器 (SM) 架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)、数据类型和输入大小选择性能最佳的实现。

cuDNN 最初成名是因为在安培[SM 架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture) GPU 上加速了卷积神经网络。对于在 Hopper 尤其是 Blackwell [SM 架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)上的 Transformer 神经网络，NVIDIA 倾向于更强调 [CUTLASS](https://github.com/NVIDIA/cutlass) 库。

有关 cuDNN 的更多信息，请参阅[官方 cuDNN 文档](https://docs.nvidia.com/deeplearning/cudnn/)和[开源前端 API](https://github.com/NVIDIA/cudnn-frontend)。