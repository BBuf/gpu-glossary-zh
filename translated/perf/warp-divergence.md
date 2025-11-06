<!--
原文: 文件路径: gpu-glossary/perf/warp-divergence.md
翻译时间: 2025-11-06 18:54:57
-->

---
title: 什么是线程束发散？
---

线程束发散 (warp divergence) 发生在[线程束 (warp)](/gpu-glossary/device-software/warp) 内的线程由于控制流语句而采取不同执行路径时。

例如，考虑以下[内核 (kernel)](/gpu-glossary/device-software/kernel)：

```cpp
__global__ void divergent_kernel(float* data, int n) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < n) {
        if (data[idx] > 0.5f) {
		    // A
            data[idx] = data[idx] * 4.0f;
        } else {
		    // B
            data[idx] = data[idx] + 2.0f;
        }
        data[idx] = data[idx] * data[idx];
    }
}
```

当[线程束 (warp)](/gpu-glossary/device-software/warp) 内的[线程 (threads)](/gpu-glossary/device-software/thread) 遇到数据相关的条件语句时，根据 `data[idx]` 的值，一些[线程 (threads)](/gpu-glossary/device-software/thread) 必须执行代码块 A，而其他线程必须执行代码块 B。由于这种数据依赖性以及[CUDA 编程模型 (CUDA programming model)](/gpu-glossary/device-software/cuda-programming-model) 及其在[PTX 机器模型 (PTX machine model)](/gpu-glossary/device-software/parallel-thread-execution) 中实现的结构性约束，程序员或编译器无法避免[线程束 (warp)](/gpu-glossary/device-software/warp) 内部控制流的这种分裂。

相反，[线程束调度器 (warp scheduler)](/gpu-glossary/device-hardware/warp-scheduler) 必须处理这些发散代码路径的并发执行，它通过"屏蔽"一些[线程 (threads)](/gpu-glossary/device-software/thread) 使其不执行指令来实现这一点。这是通过使用谓词[寄存器 (registers)](/gpu-glossary/device-software/registers) 实现的。

让我们检查生成的[SASS (Streaming Assembler)](/gpu-glossary/device-software/streaming-assembler) ([Godbolt 链接](https://godbolt.org/z/EGWKb5oWr)) 来理解执行流程：

```nasm
LDG.E.SYS R4, [R2]                       // L1 加载 data[idx]
FSETP.GT.AND P0, PT, R4.reuse, 0.5, PT   // L2 设置 P0 为 data[idx] > 0.5
FADD R0, R4, 2                           // L3 将 2 + data[idx] 存储到 R0
@P0 FMUL R0, R4, 4                       // L4 在某些线程中，将 4 * data[idx] 存储到 R0
FMUL R5, R0, R0                          // L5 将 R0 * R0 存储到 R5
STG.E.SYS [R2], R5                       // L6 将 R5 存储到 data[idx]
```

将数据加载到 `R4` (`L1`) 后，[线程束 (warp)](/gpu-glossary/device-software/warp) 中的所有 32 个[线程 (threads)](/gpu-glossary/device-software/thread) 并发执行 `FSETP.GT.AND` (`L2`)，每个[线程 (thread)](/gpu-glossary/device-software/thread) 根据 `R4` 中的 `data` 值获得自己的 `P0` 值。然后，我们看到一点[编译器 (nvcc)](/gpu-glossary/host-software/nvcc) 的巧妙之处：在 `L3` 中，*所有*[线程 (threads)](/gpu-glossary/device-software/thread) 都执行代码块 A 的代码，写入 `R0`。只有那些 `P0` 为真的线程随后执行代码块 B 的代码 (`L4`)，覆盖在 `L3` 中写入 `R0` 的值。在这条指令上，[线程束 (warp)](/gpu-glossary/device-software/warp) 被称为"发散的"。在 `L5` 上，所有[线程 (threads)](/gpu-glossary/device-software/thread) 都回到执行相同的代码。一旦[线程束调度器 (warp scheduler)](/gpu-glossary/device-hardware/warp-scheduler) 通过在同一时钟周期发出相同指令使它们重新对齐，线程束就"收敛"了。

这可能比将分支天真地编码到[SASS (Streaming Assembler)](/gpu-glossary/device-software/streaming-assembler) 中更高效，后者会对 `L3` 和 `L4` 两行都进行谓词化 — 说"可能"是因为我们可以信任[编译器 (nvcc)](/gpu-glossary/host-software/nvcc)，并且启发式地看，我们是在用廉价、充足的[CUDA 核心 (CUDA Core)](/gpu-glossary/device-hardware/cuda-core) 计算来换取更昂贵的流控制。正如在 GPU 编程中常见的那样，即使只是简单的谓词化，浪费计算（每次执行 `L4` 时进行一次不必要的 `FADD`）也比增加复杂性要好！

编译器可能积极避免发散的一个原因是，在早期（Volta 架构之前）的 GPU 中，发散的[线程束 (warps)](/gpu-glossary/device-software/warp) 总是完全串行化的。虽然线程束发散仍然会降低效率，但具有独立线程调度的现代 GPU 不一定会经历完全的串行化惩罚。