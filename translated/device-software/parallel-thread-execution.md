<!--
原文: 文件路径: gpu-glossary/device-software/parallel-thread-execution.md
翻译时间: 2025-11-06 18:35:59
-->

---
title: 什么是并行线程执行？
abbreviation: PTX
---

并行线程执行 (Parallel Thread eXecution, PTX) 是一种用于在并行处理器（几乎总是 NVIDIA GPU）上运行的代码的中间表示 (intermediate representation, IR)。它是 `nvcc`（[NVIDIA CUDA 编译器驱动程序](/gpu-glossary/host-software/nvcc)）输出的格式之一。许多 NVIDIA 工程师将其发音为 "pee-tecks"，而其他人则发音为 "pee-tee-ecks"。

NVIDIA 文档将 PTX 同时称为"虚拟机"和"指令集架构"。

从程序员的角度来看，PTX 是一种针对虚拟机模型进行编程的指令集。生成 PTX 的程序员或编译器可以确信他们的程序将在许多不同的物理机器上以相同的语义运行，包括尚不存在的机器。通过这种方式，它也类似于 CPU 指令集架构，如 [x86_64](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html)、[aarch64](https://developer.arm.com/documentation/ddi0487/latest/) 或 [SPARC](https://www.gaisler.com/doc/sparcv8.pdf)。

与这些 ISA 不同，PTX 更像是一种[中间表示](https://en.wikipedia.org/wiki/Intermediate_representation)，类似于 LLVM-IR。[CUDA 二进制文件](/gpu-glossary/host-software/cuda-binary-utilities)的 PTX 组件将由主机 [CUDA 驱动程序](/gpu-glossary/host-software/nvidia-gpu-drivers) 即时 (just-in-time, JIT) 编译为特定设备的 [SASS](/gpu-glossary/device-software/streaming-assembler) 以供执行。

对于 NVIDIA GPU，PTX 是向前兼容的：由于这种 JIT 编译机制，具有匹配或更高[计算能力 (compute capability)](/gpu-glossary/device-software/compute-capability) 版本的 GPU 将能够运行该程序。通过这种方式，PTX 成为了分离硬件和软件世界的["窄腰"](https://www.oilshell.org/blog/2022/02/diagrams.html)。

一些 PTX 示例：

```ptx
.reg .f32 %f<7>;
```

- 这是给 PTX 到 [SASS](/gpu-glossary/device-software/streaming-assembler) 编译器的编译器指令，表明该内核 (kernel) 使用七个 32 位浮点[寄存器 (registers)](/gpu-glossary/device-software/registers)。寄存器是从 [流式多处理器 (Streaming Multiprocessor, SM)](/gpu-glossary/device-hardware/streaming-multiprocessor) 的[寄存器文件 (register file)](/gpu-glossary/device-hardware/register-file) 中动态分配给[线程 (threads)](/gpu-glossary/device-software/thread) 组（[线程束 (warps)](/gpu-glossary/device-software/warp)）的。

```ptx
fma.rn.f32 %f5, %f4, %f3, 0f3FC00000;
```

- 应用融合乘加 (`fma`) 操作，将寄存器 `f3` 和 `f4` 的内容相乘，并加上常量 `0f3FC00000`，将结果存储在 `f5` 中。所有数字均为 32 位浮点表示。FMA 操作的 `rn` 后缀将浮点舍入模式设置为 [IEEE 754 "向偶数舍入"](https://en.wikipedia.org/wiki/IEEE_754)（默认模式）。

```ptx
mov.u32 %r1, %ctaid.x;
mov.u32 %r2, %ntid.x;
mov.u32 %r3, %tid.x;
```

- 将协作线程阵列索引 (cooperative thread array index) 的 `x` 轴值、协作线程阵列维度索引 (`ntid`) 和线程索引 (thread index) 移动到三个 `u32` 寄存器 `r1` - `r3` 中。

PTX 编程模型向程序员暴露了多个级别的并行性。这些级别通过 PTX 机器模型直接映射到硬件上，如下图所示。

![PTX 机器模型。修改自 [PTX 文档](https://docs.nvidia.com/cuda/parallel-thread-execution/#ptx-machine-model)。](../images/ptx-machine-model.svg)

值得注意的是，在此机器模型中，多个处理器共享一个指令单元。虽然每个处理器运行一个[线程 (thread)](/gpu-glossary/device-software/thread)，但这些线程必须执行相同的指令——因此称为*并行*线程执行或 PTX。它们通过[共享内存 (shared memory)](/gpu-glossary/device-software/shared-memory) 相互协调，并通过私有[寄存器 (registers)](/gpu-glossary/device-software/registers) 产生不同的结果。

最新版本的 PTX 文档可从 NVIDIA [此处](https://docs.nvidia.com/cuda/parallel-thread-execution/) 获取。PTX 的指令集使用称为"[计算能力 (compute capability)](/gpu-glossary/device-software/compute-capability)"的数字进行版本控制，该数字与"最低支持的[流式多处理器架构 (Streaming Multiprocessor architecture)](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture) 版本"同义。

手动编写内联 PTX 除了在追求极致性能的前沿领域外并不常见，这类似于编写内联 `x86_64` 汇编，例如在分析数据库中的高性能向量化查询运算符以及操作系统内核的性能敏感部分中所做的那样。在 2025 年 9 月撰写本文时，内联 PTX 是利用某些 Hopper 架构特有硬件功能（如 `wgmma` 和 `tma` 指令）的唯一方式，例如在 [Flash Attention 3](https://arxiv.org/abs/2407.08608) 或 [Machete w4a16 内核](https://youtu.be/-4ZkpQ7agXM) 中。在 [Godbolt](https://godbolt.org/z/5r9ej3zjW) 上支持同时查看 [CUDA C/C++](/gpu-glossary/host-software/cuda-c)、[SASS](/gpu-glossary/device-software/streaming-assembler) 和 [PTX](/gpu-glossary/device-software/parallel-thread-execution)。详情请参阅 [NVIDIA "在 CUDA 中使用内联 PTX 汇编"指南](https://docs.nvidia.com/cuda/inline-ptx-assembly/)。