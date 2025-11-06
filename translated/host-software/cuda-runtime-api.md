<!--
原文: 文件路径: gpu-glossary/host-software/cuda-runtime-api.md
翻译时间: 2025-11-06 18:24:53
-->

---
title: 什么是 CUDA 运行时 API？
---

CUDA 运行时 API (CUDA Runtime API) 封装了
[CUDA 驱动 API](/gpu-glossary/host-software/cuda-driver-api)，并为相同功能提供了
更高级别的 API。

![](https://files.mdnice.com/user/59/8a5a5606-71b8-47b0-88f4-3b35c2e5ecb1.png)

> CUDA 工具包。CUDA 运行时 API 封装了 CUDA 驱动 API，使其更适合应用程序编程。改编自《Professional CUDA C Programming Guide》。

通常更推荐使用运行时 API 而非
[驱动 API](/gpu-glossary/host-software/cuda-driver-api)，因为它具有更好的人体工程学设计，
但在内核启动控制和上下文管理方面存在一些小的注意事项。更多信息请参阅
CUDA 运行时 API 文档的
[此章节](https://docs.nvidia.com/cuda/cuda-runtime-api/driver-vs-runtime-api.html#driver-vs-runtime-api)。

虽然根据
[NVIDIA CUDA 工具包 EULA 的附件 A](https://docs.nvidia.com/cuda/eula/index.html#attachment-a)，
运行时 API 可以静态链接，但这不是必须的。在 Linux 系统上，用于动态链接的共享对象文件通常
名为 [libcudart.so](/gpu-glossary/host-software/libcudart)。

CUDA 运行时 API 是闭源的。您可以在
[此处](https://docs.nvidia.com/cuda/cuda-runtime-api/index.html)找到其文档。