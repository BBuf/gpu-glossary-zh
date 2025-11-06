<!--
原文: 文件路径: gpu-glossary/device-hardware/load-store-unit.md
翻译时间: 2025-11-06 19:08:47
-->

---
---
title: 什么是加载/存储单元？
abbreviation: LSU
---

加载/存储单元 (Load/Store Unit, LSU) 负责向 GPU 的内存子系统分派加载或存储数据的请求。

![](https://files.mdnice.com/user/59/24190e9b-c268-40b0-b7e0-116a7034c57c.png)

> H100 流式多处理器 (SM) 的内部架构。图中粉色部分展示了加载/存储单元以及[特殊功能单元](/gpu-glossary/device-hardware/special-function-unit)。改编自 NVIDIA 的 [H100 白皮书](https://modal-cdn.com/gpu-glossary/gtc22-whitepaper-hopper.pdf)。]

对于 [CUDA 程序员](/gpu-glossary/host-software/cuda-software-platform) 而言最重要的是，加载/存储单元直接与[流式多处理器 (Streaming Multiprocessor)](/gpu-glossary/device-hardware/streaming-multiprocessor) 的片上 SRAM [L1 数据缓存](/gpu-glossary/device-hardware/l1-data-cache)交互，并间接与片外设备上的[全局内存 (global RAM)](/gpu-glossary/device-hardware/gpu-ram) 交互，这两者分别在 [CUDA 编程模型 (CUDA programming model)](/gpu-glossary/device-software/cuda-programming-model) 中实现了[内存层次结构 (memory hierarchy)](/gpu-glossary/device-software/memory-hierarchy) 的最低层和最高层。