<!--
原文: 文件路径: gpu-glossary/host-software/cuda-binary-utilities.md
翻译时间: 2025-11-06 18:29:43
-->

---
title: CUDA 二进制工具是什么？
---

CUDA 二进制工具是一套用于检查二进制文件内容的工具集合，这些二进制文件包括由 [NVIDIA CUDA 编译器驱动程序 (nvcc)](/gpu-glossary/host-software/nvcc) 输出的文件。

其中一个工具 `cuobjdump` 可用于检查和操作整个主机二进制文件的内容，或者通常嵌入在这些二进制文件中的 CUDA 特定 `cubin` 文件。

另一个工具 `nvidisasm` 则专门用于操作 `cubin` 文件。它可以提取 [SASS 汇编器 (Streaming Assembler)](/gpu-glossary/device-software/streaming-assembler) 并对其进行操作，例如构建控制流图以及将汇编指令映射到 CUDA 程序文件中的代码行。

您可以在[此处](https://docs.nvidia.com/cuda/cuda-binary-utilities/index.html)找到相关文档。