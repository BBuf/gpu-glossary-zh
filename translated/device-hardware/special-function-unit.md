<!--
原文: 文件路径: gpu-glossary/device-hardware/special-function-unit.md
翻译时间: 2025-11-06 18:59:43
-->

---
title: 什么是特殊功能单元？
abbreviation: SFU
---

特殊功能单元 (Special Function Units, SFU) 位于[流式多处理器 (Streaming Multiprocessors, SMs)](/gpu-glossary/device-hardware/streaming-multiprocessor)中，用于加速特定的算术运算。

![](https://files.mdnice.com/user/59/24190e9b-c268-40b0-b7e0-116a7034c57c.png)

> H100 SM 的内部架构。特殊功能单元以褐红色显示，与[加载/存储单元 (Load/Store Units)](/gpu-glossary/device-hardware/load-store-unit)一起展示。修改自 NVIDIA 的 [H100 白皮书](https://modal-cdn.com/gpu-glossary/gtc22-whitepaper-hopper.pdf)。

对于神经网络工作负载而言，最值得注意的是超越数学运算，例如 `exp`、`sin` 和 `cos`。

与特殊功能单元相关的[流式汇编器 (Streaming Assembler, SASS)](/gpu-glossary/device-software/streaming-assembler) 指令通常以 `MUFU` 开头：`MUFU.SQRT`、`MUFU.EX2`。有关使用 `MUFU.EX2` 指令在 [CUDA C++](/gpu-glossary/host-software/cuda-c) 中实现 `expf` 内置函数的示例汇编代码，请参阅 [此 Godbolt 链接](https://godbolt.org/z/WGh3rPe83)。