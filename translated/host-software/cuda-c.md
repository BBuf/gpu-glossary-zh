<!--
原文: 文件路径: gpu-glossary/host-software/cuda-c.md
翻译时间: 2025-11-06 18:24:33
-->

---
title: 什么是 CUDA C++ 编程语言？
---

CUDA C++ 是 [CUDA 编程模型](/gpu-glossary/device-software/cuda-programming-model) 的一种实现，作为 C++ 编程语言的扩展。

CUDA C++ 向 C++ 添加了若干特性以实现 [CUDA 编程模型](/gpu-glossary/device-software/cuda-programming-model)，包括：

- 使用 **`__global__`** 定义**[内核 (Kernel)](/gpu-glossary/device-software/kernel)**。CUDA [内核 (Kernel)](/gpu-glossary/device-software/kernel) 被实现为接受指针参数且返回类型为 `void` 的 C++ 函数，并使用此关键字进行标注。
- 使用 **`<<<>>>`** 启动**[内核 (Kernel)](/gpu-glossary/device-software/kernel)**。[内核 (Kernel)](/gpu-glossary/device-software/kernel) 通过三重括号语法从 CPU 主机端执行，该语法用于设置[线程块网格 (Thread Block Grid)](/gpu-glossary/device-software/thread-block-grid) 的维度。
- 使用 `shared` 关键字分配**[共享内存 (Shared Memory)](/gpu-glossary/device-software/shared-memory)**，使用 `__syncthreads()` 内部函数进行**屏障同步**，以及使用 `blockDim` 和 `threadIdx` 内置变量进行**[线程块 (Thread Block)](/gpu-glossary/device-software/thread-block)** 和 **[线程 (Thread)](/gpu-glossary/device-software/thread)** 索引。

CUDA C++ 程序由主机端 C/C++ 编译器驱动（如 `gcc`）与 [NVIDIA CUDA 编译器驱动](/gpu-glossary/host-software/nvcc) `nvcc` 共同编译。

有关如何在 [Modal](https://modal.com) 上使用 CUDA C++ 的信息，请参阅[本指南](https://modal.com/docs/guide/cuda)。