<!--
原文: 文件路径: gpu-glossary/perf/latency-hiding.md
翻译时间: 2025-11-06 18:47:39
-->

---
title: 什么是延迟隐藏？
---

延迟隐藏是一种通过[并发运行多个长延迟操作](/gpu-glossary/perf/littles-law)来掩盖长延迟操作的策略。

高性能 GPU 程序通过交错执行多个[线程 (thread)](/gpu-glossary/device-software/thread) 来隐藏延迟。这使得程序即使面对较长的指令延迟也能保持高吞吐量。当一个[线程束 (warp)](/gpu-glossary/perf/warp-execution-state) 因慢速内存操作而停顿 (stall) 时，GPU 会立即切换到执行另一个[符合条件的线程束 (eligible warp)](/gpu-glossary/perf/warp-execution-state) 的指令。

这使得所有执行单元都能保持并发忙碌状态。当一个[线程束 (warp)](/gpu-glossary/device-software/warp) 使用[张量核心 (Tensor Core)](/gpu-glossary/device-hardware/tensor-core) 进行矩阵乘法时，另一个线程束可能在 [CUDA 核心 (CUDA Core)](/gpu-glossary/device-hardware/cuda-core) 上执行算术运算（例如，[对矩阵乘数进行量化或反量化](https://arxiv.org/abs/2408.11743)），而第三个线程束可能正在通过[加载/存储单元 (load/store unit)](/gpu-glossary/device-hardware/load-store-unit) 获取数据。

具体来说，考虑以下[流式汇编器 (Streaming Assembler)](/gpu-glossary/device-software/streaming-assembler) 中的简单指令序列。

```nasm
LDG.E.SYS R1, [R0]        // 内存加载，400 个周期
IMUL R2, R1, 0xBEEF       // 整数乘法，6 个周期
IADD R4, R2, 0xAFFE       // 整数加法，4 个周期
IMUL R6, R4, 0x1337       // 整数乘法，6 个周期
```

如果顺序执行，这将需要 416 个周期才能完成。我们可以通过并发操作来隐藏这种延迟。如果我们假设每个周期可以发射一条指令，那么根据[利特尔定律 (Little's Law)](/gpu-glossary/perf/littles-law)，如果我们运行 416 个并发[线程 (thread)](/gpu-glossary/device-software/thread)，我们仍然可以平均每个周期完成一次该序列，从而对使用 `R6` 中数据的消费者隐藏了内存延迟。

请注意，指令发射的单位不是[线程 (thread)](/gpu-glossary/device-software/thread)，而是[线程束 (warp)](/gpu-glossary/device-software/warp)。每个[线程束 (warp)](/gpu-glossary/device-software/warp) 包含 32 个[线程 (thread)](/gpu-glossary/device-software/thread)，因此我们的代码片段需要 416 ÷ 32 = 13 个[线程束 (warp)](/gpu-glossary/device-software/warp)。当成功隐藏延迟时，GPU 的调度系统会维持这么多[线程束 (warp)](/gpu-glossary/device-software/warp) 在执行中，每当一个线程束停顿时就在它们之间切换，确保执行单元在等待慢速操作完成时永远不会空闲。

要深入了解[张量核心 (Tensor Core)](/gpu-glossary/device-hardware/tensor-core) 出现之前的 GPU 上的延迟隐藏，请参阅 [Vasily Volkov 的博士论文](https://arxiv.org/abs/2206.02874)。