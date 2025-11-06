<!--
原文: 文件路径: gpu-glossary/device-software/thread.md
翻译时间: 2025-11-06 18:38:09
-->

---
title: 什么是 CUDA 线程？
---


![](https://files.mdnice.com/user/59/e89a60c2-b91b-471e-a28a-3f62feddc41d.png)

> 线程是线程组层次结构中的最低层级（顶部、左侧），并被映射到[流式多处理器](/gpu-glossary/device-hardware/streaming-multiprocessor)的[核心](/gpu-glossary/device-hardware/core)上。改编自 NVIDIA 的 [CUDA 复习：CUDA 编程模型](https://developer.nvidia.com/blog/cuda-refresher-cuda-programming-model/) 和 NVIDIA [CUDA C++ 编程指南](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#programming-model) 中的图表。


_执行线程_（简称"线程"）是 GPU 编程的最低单位，是 [CUDA 编程模型](/gpu-glossary/device-software/cuda-programming-model) 的[线程层次结构](/gpu-glossary/device-software/thread-hierarchy)的基础和原子单位。线程拥有自己的[寄存器](/gpu-glossary/device-software/registers)，但除此之外几乎没有其他资源。

[SASS](/gpu-glossary/device-software/streaming-assembler) 和 [PTX](/gpu-glossary/device-software/parallel-thread-execution) 程序都以线程为目标。相比之下，POSIX 环境中的典型 C 程序以进程为目标，而进程本身是一个或多个线程的集合。与 POSIX 线程不同，[CUDA](/gpu-glossary/device-software/cuda-programming-model) 线程不用于进行系统调用。

与 CPU 上的线程类似，GPU 线程可以拥有私有的指令指针/程序计数器。然而，出于性能原因，GPU 程序通常被编写为让一个[线程束](/gpu-glossary/device-software/warp)中的所有线程共享相同的指令指针，以锁步方式执行指令（另请参阅[线程束调度器](/gpu-glossary/device-hardware/warp-scheduler)）。

同样类似于 CPU 上的线程，GPU 线程在[全局内存](/gpu-glossary/device-hardware/gpu-ram)中拥有栈，用于存储溢出的寄存器和函数调用栈，但高性能[内核](/gpu-glossary/device-software/kernel)通常限制两者的使用。

单个 [CUDA 核心](/gpu-glossary/device-hardware/cuda-core)执行来自单个线程的指令。