<!--
原文: 文件路径: gpu-glossary/perf/bank-conflict.md
翻译时间: 2025-11-06 18:43:47
-->

---
title: 什么是存储体冲突？
---

当一个[线程束](/gpu-glossary/device-software/warp)中的多个[线程](/gpu-glossary/device-software/thread)同时请求访问[共享内存](/gpu-glossary/device-software/shared-memory)中同一存储体（bank）但不同地址的内存时，我们称之为发生了存储体冲突。

![当[线程](/gpu-glossary/device-software/thread)访问不同的[共享内存](/gpu-glossary/device-software/shared-memory)存储体时，访问是并行处理的（左图）。当它们都访问同一存储体但不同地址时，访问会被串行化（右图）。](../images/bank-conflict.svg)

当发生存储体冲突时，不同[线程](/gpu-glossary/device-software/thread)的访问会被串行化。这会大幅降低内存吞吐量，即按整数倍减少，从而无法饱和[内存带宽](/gpu-glossary/perf/memory-bandwidth)。

与其他SRAM缓存存储器类似，[流式多处理器](/gpu-glossary/device-hardware/streaming-multiprocessor)中的[共享内存](/gpu-glossary/device-software/shared-memory)被组织成称为"存储体"的组。这些存储体可以同时访问，从而增加带宽。

在GPU中，有32个存储体，每个存储体宽度为4字节，连续的32位字（不是64位；GPU设计时考虑的是32位浮点数和整数）映射到连续的存储体。

```
地址:  0x00  0x04  0x08  0x0C  0x10  0x14  0x18  0x1C  ...  0x7C
存储体:   0     1     2     3     4     5     6     7   ...    31

地址:  0x80  0x84  0x88  0x8C  0x90  0x94  0x98  0x9C  ...  0xFC

存储体:   0     1     2     3     4     5     6     7   ...    31
```

相差32 × 4 = 128字节的地址会映射到同一存储体。[共享内存](/gpu-glossary/device-software/shared-memory)的容量大致在千字节级别，因此多个地址会映射到同一存储体。

如果我们在共享内存中访问数组的连续元素，[线程束](/gpu-glossary/device-software/warp)中的每个[线程](/gpu-glossary/device-software/thread)都会命中不同的存储体：

```cpp
__shared__ float data[1024];  // 共享内存中的数组

// 所有32个线程访问data的连续元素
int tid = threadIdx.x;
float value = data[tid];  // 地址最低有效位: 0x00, 0x04, 0x08, ...
```

所有32次访问在一个内存事务中完成，因为每个[线程](/gpu-glossary/device-software/thread)都命中了不同的存储体。这在上图的左侧有所描绘。

但假设我们希望[线程](/gpu-glossary/device-software/thread)访问行优先[共享内存](/gpu-glossary/device-software/shared-memory)数组中的一列，每行有32个元素，于是我们这样写：

```cpp
float value = data[tid * 32];  // 地址最低有效位: 0x000, 0x080, 0x100 ...
// 注意：浮点数宽度为4字节
```

如上图右侧所示，所有访问都命中了同一存储体（存储体0），因此必须串行化，导致延迟增加了32倍，从大约十几个周期增加到数百个周期。我们可以通过转置[共享内存](/gpu-glossary/device-software/shared-memory)数组来解决这个存储体冲突。有关解决存储体冲突的更多技术，请参阅[GTC 2024的《CUDA编程与性能优化入门》演讲](https://www.nvidia.com/en-us/on-demand/session/gtc24-s62191/)。

请注意，如果[线程](/gpu-glossary/device-software/thread)访问同一存储体中的相同地址，即完全相同的数据，则不会发生冲突，因为数据可以进行多播/广播。