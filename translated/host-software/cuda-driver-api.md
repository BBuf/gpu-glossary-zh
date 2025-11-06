<!--
原文: 文件路径: gpu-glossary/host-software/cuda-driver-api.md
翻译时间: 2025-11-06 18:23:31
-->

---
title: 什么是 CUDA 驱动 API？
---

[CUDA 驱动 API](https://docs.nvidia.com/cuda/cuda-driver-api/index.html) 是 NVIDIA CUDA 驱动的用户空间组件。它为熟悉 C 标准库的用户提供了实用工具：例如用于在 GPU 设备上分配[内存](/gpu-glossary/device-software/global-memory)的 `cuMalloc` 函数。

![](https://files.mdnice.com/user/59/3bd3f864-14f2-4025-8c94-df57c6ea7302.png)

> CUDA 工具包。CUDA 驱动 API 位于应用程序或其他工具包组件与 GPU 之间。改编自《Professional CUDA C Programming Guide》。

很少有 CUDA 程序直接使用 CUDA 驱动 API 编写，它们通常使用 [CUDA 运行时 API](/gpu-glossary/host-software/cuda-runtime-api)。请参阅 CUDA 驱动 API 文档中的[此章节](https://docs.nvidia.com/cuda/cuda-driver-api/driver-vs-runtime-api.html#driver-vs-runtime-api)。

CUDA 驱动 API 通常不进行静态链接，而是动态链接，在 Linux 系统上通常名为 [libcuda.so](/gpu-glossary/host-software/libcuda)。

CUDA 驱动 API 具有二进制兼容性：针对旧版 CUDA 驱动 API 编译的应用程序可以在装有新版 CUDA 驱动 API 的系统上运行。也就是说，操作系统的二进制加载器可以加载新版 CUDA 驱动 API，而程序功能保持不变。

有关分发 [CUDA C/C++](/gpu-glossary/host-software/cuda-c) 应用程序的详细信息，请参阅 NVIDIA 的 [CUDA C/C++ 最佳实践指南](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide)。

CUDA 驱动 API 是闭源的，您可以在[此处](https://docs.nvidia.com/cuda/cuda-driver-api/index.html)找到其文档。

尽管不常用，但存在一些项目试图提供或使用 CUDA 驱动 API 的开源替代方案，例如 [LibreCuda](https://github.com/mikex86/LibreCuda) 和 [tinygrad](https://github.com/tinygrad)。详情请参阅[其源代码](https://github.com/tinygrad/tinygrad/blob/77f7ddf62a78218bee7b4f7b9ff925a0e581fcad/tinygrad/runtime/ops_nv.py)。