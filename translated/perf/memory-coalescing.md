<!--
原文: 文件路径: gpu-glossary/perf/memory-coalescing.md
翻译时间: 2025-11-06 18:53:11
-->

---
title: 什么是内存合并？
---

内存合并是一种硬件技术，通过在单个*物理*内存访问中服务多个*逻辑*内存读取，来提高[内存带宽](/gpu-glossary/perf/memory-bandwidth)的利用率。

内存合并在访问[全局内存](/gpu-glossary/device-software/global-memory)期间发生。关于[共享内存](/gpu-glossary/device-software/shared-memory)的高效访问，请参阅关于[存储体冲突](/gpu-glossary/perf/bank-conflict)的文章。

在[CUDA](/gpu-glossary/device-hardware/cuda-device-architecture) GPU中，[全局内存](/gpu-glossary/device-software/global-memory)由[GPU显存](/gpu-glossary/device-hardware/gpu-ram)支持，该显存采用如GDDR或HBM等动态随机存取存储器 (DRAM) 技术构建。这些技术具有高[内存带宽](/gpu-glossary/perf/memory-bandwidth)，但访问延迟也很长（即使与CPU RAM中使用的同类技术DDR5相比）。DRAM的访问延迟受限于小型电容器对其访问线路充电的速度，这从根本上受到热、功耗和尺寸的限制。由于这种高延迟，如果所有逻辑内存访问都作为独立的物理访问来服务，GPU的[内存带宽](/gpu-glossary/perf/memory-bandwidth)将无法被充分利用。

内存合并利用DRAM技术的内部细节，为某些访问模式实现全带宽利用率。每次访问DRAM地址时，多个连续地址会在单个时钟周期内并行获取。更多细节请参阅[《大规模并行处理器编程》第四版](https://www.amazon.com/dp/0323912311)的第6.1节；全面细节请参阅Ulrich Drepper的优秀文章[_每个程序员应该了解的内存知识_](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf)。这些连续内存位置的访问和传输被称为*DRAM突发传输*。如果多个并发的逻辑访问由单个物理突发传输服务，则该访问被称为*已合并的*。请注意，物理访问是内存事务的一部分，这个术语您可能在内存合并的其他描述中看到。

在CPU上，类似的将突发传输映射到缓存线的机制提高了访问效率。正如GPU编程中常见的情况，在CPU中是自动的缓存行为，在这里则需要程序员管理。

这并不像听起来那么困难，因为DRAM突发传输与[CUDA PTX](/gpu-glossary/device-software/parallel-thread-execution)的单指令多线程 (SIMT) 执行模型优雅地对齐。也就是说，在正常执行中，一个[线程束](/gpu-glossary/device-software/warp)中的所有[线程](/gpu-glossary/device-software/thread)同时执行相同的指令。这使得[CUDA](/gpu-glossary/device-software/cuda-programming-model)程序员很容易编写具有合并访问的程序，并且内存管理硬件也很容易检测可以合并的访问。通常，单个突发传输可以服务128字节——这并非巧合，刚好足够一个[线程束](/gpu-glossary/device-software/warp)中的32个[线程](/gpu-glossary/device-software/thread)各加载一个32位浮点数。

为了演示内存合并对性能的影响，让我们考虑以下[内核](/gpu-glossary/device-software/kernel)，它从一个数组中读取值，该数组具有可变的`stride`（步长），即被访问元素之间的间距。随着步长的增加，服务每个[线程束](/gpu-glossary/device-software/warp)发出的读取请求所需的DRAM突发传输次数也会增加，导致每个逻辑访问对应的物理访问增多，从而降低内存吞吐量。

```cpp
__global__ void strided_read_kernel(const float* __restrict__ in,
                                    float* __restrict__ out,
                                    size_t N, int stride)
{
    const size_t t  = blockIdx.x * blockDim.x + threadIdx.x;
    const size_t T  = gridDim.x * (size_t)blockDim.x;

    float acc = 0.f;

    for (size_t j = (size_t)t * (size_t)stride; j < N; j += (size_t)T * (size_t)stride) {
        // 在一个线程束内，地址相差 (stride * sizeof(float))
        float v = in[j]; // 当 stride == 1 时实现完美合并
        acc = acc * 1.000000119f + v;  // 强制编译器保留加载操作
    }

    // 每个线程执行一次写入（与读取相比可忽略）
    if (t < N) out[t] = acc;
}
```

当我们在Godbolt上通过一个微基准测试运行这个内核时（您可以[在此处](https://godbolt.org/z/KbWhEWjcb)复现），我们观察到步长与吞吐量之间的预期关系：

```
# 设备: Tesla T4 (SM 75)
# N = 67108864 个浮点数 (256.0 MB), 迭代次数 = 10
步长        GB/秒
    1       206.0
    2       130.5
    4        68.8
    8        33.8
   16        16.8
   32        15.2
   64        13.6
  128        11.2
```

也就是说，步长增加为2会使吞吐量减半，因为服务每个[线程束](/gpu-glossary/device-software/warp)请求所需的DRAM突发传输次数翻倍。将步长加倍到4再次使吞吐量减半。一旦我们在步长为16时吞吐量降低了16倍，模式就发生了变化。从那里开始性能以不同的方式下降，大概是由于其他内存子系统组件的可见性增加以及它们因局部性降低（例如设备上的TLB未命中）而导致的性能下降。

关于全局内存访问的更多最佳实践，请参阅NVIDIA开发者博客上的文章[_如何在CUDA C/C++内核中高效访问全局内存_](https://developer.nvidia.com/blog/how-access-global-memory-efficiently-cuda-c-kernels/)。