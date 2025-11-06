<!--
原文: 文件路径: gpu-glossary/device-software/streaming-assembler.md
翻译时间: 2025-11-06 18:33:51
-->

---
title: 什么是流式汇编器？
abbreviation: SASS
---

[流式汇编器](https://stackoverflow.com/questions/9798258/what-is-sass-short-for)
(SASS) 是运行在 NVIDIA GPU 上的程序的汇编格式。这是可编写人类可读代码的最低层级格式。它是 `nvcc`（[NVIDIA CUDA 编译器驱动程序](/gpu-glossary/host-software/nvcc)）输出的格式之一，与 [PTX](/gpu-glossary/device-software/parallel-thread-execution) 并列。它在执行期间被转换为特定设备的二进制微码。推测"流式汇编器"中的"流式"指的是该汇编语言程序所面向的[流式多处理器](/gpu-glossary/device-hardware/streaming-multiprocessor) (SM)。

SASS 是版本化的，并且与特定的 NVIDIA GPU [SM 架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)绑定。另请参阅[计算能力](/gpu-glossary/device-software/compute-capability)。

以下是适用于 Hopper GPU 的 SM90a 架构的 SASS 示例指令：

- `FFMA R0, R7, R0, 1.5 ;` - 执行`F`used `F`loating point `M`ultiply `A`dd（融合浮点乘加），将`R`egister 7 和`R`egister 0 的内容相乘，加上 `1.5`，并将结果存储在`R`egister 0 中。
- `S2UR UR4, SR_CTAID.X ;` - 将[协作线程阵列](/gpu-glossary/device-software/cooperative-thread-array) (CTA) 索引的 `X` 值从其`S`pecial `R`egister（特殊寄存器）复制到`U`niform `R`egister 4（统一寄存器）。

与 CPU 相比，手动编写这种"GPU 汇编器"更为罕见。在性能分析和编辑高级 [CUDA C/C++](/gpu-glossary/host-software/cuda-c) 代码或内联 [PTX](/gpu-glossary/device-software/parallel-thread-execution) 时查看编译器生成的 SASS [更为常见](https://docs.nvidia.com/gameworks/content/developertools/desktop/ptx_sass_assembly_debugging.htm)，尤其是在生产最高性能的内核时。[Godbolt](https://godbolt.org/z/5r9ej3zjW) 支持同时查看 [CUDA C/C++](/gpu-glossary/host-software/cuda-c)、SASS 和 [PTX](/gpu-glossary/device-software/parallel-thread-execution)。有关 SASS 的更多细节（重点关注性能调试工作流），请参阅 Arun Demeure 的[这个演讲](https://www.youtube.com/watch?v=we3i5VuoPWk)。

SASS 的文档记录*非常*少——指令列在 [NVIDIA CUDA 二进制工具文档](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html#instruction-set-ref) 中，但未定义其语义。从 ASCII 汇编器到二进制操作码和操作数的映射完全没有文档记录，但在某些情况下已被逆向工程（[Maxwell](https://github.com/NervanaSystems/maxas)、[Lovelace](https://kuterdinel.com/nv_isa_sm89/)）。