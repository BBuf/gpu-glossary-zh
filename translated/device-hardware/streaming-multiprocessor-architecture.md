<!--
原文: 文件路径: gpu-glossary/device-hardware/streaming-multiprocessor-architecture.md
翻译时间: 2025-11-06 19:00:40
-->

---
title: 什么是流式多处理器架构？
---

[流式多处理器 (SM)](/gpu-glossary/device-hardware/streaming-multiprocessor)
采用特定"架构"进行版本管理，该架构定义了它们与
[流式汇编器 (SASS)](/gpu-glossary/device-software/streaming-assembler)
代码的兼容性。

![](https://files.mdnice.com/user/59/24190e9b-c268-40b0-b7e0-116a7034c57c.png)

> 采用"Hopper" SM90 架构的流式多处理器。修改自 NVIDIA 的 [H100 白皮书](https://modal-cdn.com/gpu-glossary/gtc22-whitepaper-hopper.pdf)。

![](https://files.mdnice.com/user/59/05ba2835-b3f1-4b45-9882-55c6f63c89f3.png)

> 采用原始"Tesla" SM 架构的流式多处理器。修改自 [Fabien Sanglard 的博客](https://fabiensanglard.net/cuda)。

大多数 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 版本包含两个组成部分：主版本和次版本。

主版本_几乎_等同于 GPU 架构系列。例如，所有 `6.x` 版本的 SM 都属于 Pascal 架构。一些 NVIDIA 文档甚至
[直接声称这一点](https://docs.nvidia.com/cuda/ptx-writers-guide-to-interoperability/index.html)。
但举例来说，Ada GPU 的
[SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 架构版本为 `8.9`，
与 Ampere GPU 的主版本相同。

在调用 [NVIDIA CUDA 编译器驱动程序 (nvcc)](/gpu-glossary/host-software/nvcc) 时，
可以指定 [SASS](/gpu-glossary/device-software/streaming-assembler) 编译的目标
[SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 版本。
明确不保证跨主版本的兼容性。有关跨次版本兼容性的更多信息，请参阅
[nvcc](/gpu-glossary/host-software/nvcc) 的
[文档](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html#gpu-feature-list)。