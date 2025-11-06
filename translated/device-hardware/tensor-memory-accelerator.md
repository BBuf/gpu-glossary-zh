<!--
原文: 文件路径: gpu-glossary/device-hardware/tensor-memory-accelerator.md
翻译时间: 2025-11-06 19:06:53
-->

---
title: 什么是张量内存加速器？
abbreviation: TMA
---

张量内存加速器 (Tensor Memory Accelerator, TMA) 是 Hopper 和 Blackwell [架构](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture) GPU 中的专用硬件，旨在加速对 [GPU 内存](/gpu-glossary/device-hardware/gpu-ram) 中多维数组的访问。

![](https://files.mdnice.com/user/59/24190e9b-c268-40b0-b7e0-116a7034c57c.png)

> H100 SM 的内部架构。注意位于 [SM](/gpu-glossary/device-hardware/streaming-multiprocessor) 底部、在四个子单元之间共享的张量内存加速器。改编自 NVIDIA 的 [H100 白皮书](https://modal-cdn.com/gpu-glossary/gtc22-whitepaper-hopper.pdf)。

TMA 将数据从 [全局内存](/gpu-glossary/device-software/global-memory)/[GPU 内存](/gpu-glossary/device-hardware/gpu-ram) 加载到 [共享内存](/gpu-glossary/device-software/shared-memory)/[L1 数据缓存](/gpu-glossary/device-hardware/l1-data-cache)，完全绕过了 [寄存器](/gpu-glossary/device-software/registers)/[寄存器文件](/gpu-glossary/device-hardware/register-file)。

TMA 的第一个优势来自减少对其他计算和内存资源的使用。TMA 硬件为批量仿射内存访问（即对许多基地址和偏移量并发执行的 `addr = width * base + offset` 形式的访问，这是数组最常见的访问方式）计算地址。将这项工作卸载给 TMA 可以节省 [寄存器文件](/gpu-glossary/device-hardware/register-file) 中的空间，减少"[寄存器压力](/gpu-glossary/perf/register-pressure)"，并降低对 [CUDA 核心](/gpu-glossary/device-hardware/cuda-core) 提供的 [算术带宽](/gpu-glossary/perf/arithmetic-bandwidth) 的需求。对于具有两个或更多维度数组的大规模（KB 级别）访问，这种节省更为显著。

第二个优势来自 TMA 拷贝的异步执行模型。单个 [CUDA 线程](/gpu-glossary/device-software/thread) 可以触发一个大型拷贝，然后重新加入其所在的 [线程束](/gpu-glossary/device-software/warp) 以执行其他工作。随后，这些 [线程](/gpu-glossary/device-software/thread) 以及同一 [线程块](/gpu-glossary/device-software/thread-block) 中的其他线程可以异步检测 TMA 拷贝的完成情况，并对结果进行操作（类似于生产者-消费者模型）。

有关详细信息，请参阅 [Luo 等人的 Hopper 微基准测试论文](https://arxiv.org/abs/2501.12084v1) 和 [NVIDIA Hopper 调优指南](https://docs.nvidia.com/cuda/hopper-tuning-guide/index.html#tensor-memory-accelerator) 中关于 TMA 的部分。

请注意，尽管名称相似，但张量内存加速器并不加速使用 [张量内存](/gpu-glossary/device-hardware/tensor-memory) 的操作。