<!--
原文: 文件路径: gpu-glossary/perf/branch-efficiency.md
翻译时间: 2025-11-06 18:42:38
-->

---
title: 什么是分支效率？
---

分支效率衡量的是当遇到条件语句时，[线程束 (warp)](/gpu-glossary/device-software/warp) 中的所有[线程 (thread)](/gpu-glossary/device-software/thread) 采用相同执行路径的频率。

分支效率的计算方式为统一控制流决策数量与执行的总分支指令数之比。控制流统一性是在[线程束 (warp)](/gpu-glossary/device-software/warp) 级别进行测量的，因此分支效率反映了[线程束发散 (warp divergence)](/gpu-glossary/perf/warp-divergence) 的缺失程度。

并非所有条件语句都会降低分支效率。大多数[内核 (kernel)](https://godbolt.org/z/d1PsYYPnW) 中常见的"边界检查"代码片段

```cpp
int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < n)
```

通常具有非常高的分支效率，因为大多数[线程束 (warp)](/gpu-glossary/device-software/warp) 由具有相同条件值的[线程 (thread)](/gpu-glossary/device-software/thread) 组成，只有一个[线程束 (warp)](/gpu-glossary/device-software/warp) 的[线程 (thread)](/gpu-glossary/device-software/thread) 索引会在 `n` 的上下两侧。

虽然 CPU 也关心分支行为的统一性，但它们主要关注的是随时间变化的分支行为统一性，这是硬件控制的分支预测和推测执行的一部分。也就是说，当 CPU 内部的电路在程序执行期间多次遇到某个分支并积累相关数据时，性能应该会提高。

而 GPU 关心的是空间上的统一性。也就是说，统一性是在[线程束 (warp)](/gpu-glossary/device-software/warp) 内部测量的，这些[线程束 (warp)](/gpu-glossary/device-software/warp) 的[线程 (thread)](/gpu-glossary/device-software/thread) 在时间上并发执行，但映射到不同的数据上，如果这些[线程 (thread)](/gpu-glossary/device-software/thread) 能够统一分支，性能就会提高。