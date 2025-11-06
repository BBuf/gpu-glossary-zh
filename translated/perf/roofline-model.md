<!--
原文: 文件路径: gpu-glossary/perf/roofline-model.md
翻译时间: 2025-11-06 18:50:59
-->

---
title: 什么是屋顶线模型？
---

屋顶线模型是一种简化的、可视化的性能模型，用于快速判断程序是受[内存带宽](/gpu-glossary/perf/memory-bandwidth)限制还是[算术带宽](/gpu-glossary/perf/arithmetic-bandwidth)限制。

![[内核](/gpu-glossary/device-software/kernel)位于脊点左侧时受[内存子系统带宽限制](/gpu-glossary/perf/memory-bound)，位于脊点右侧时受[算术子系统带宽限制](/gpu-glossary/perf/compute-bound)。图表改编自提出屋顶线模型的[Williams、Waterman 和 Patterson (2008)](https://people.eecs.berkeley.edu/~kubitron/cs252/handouts/papers/RooflineVyNoYellow.pdf)。](../images/roofline-model.svg)

在屋顶线模型中，两个硬件相关的"屋顶"为可能达到的性能设定了"上限"：

- "计算屋顶"——目标硬件（[CUDA 核心](/gpu-glossary/device-hardware/cuda-core)或[张量核心](/gpu-glossary/device-hardware/tensor-core)）的[峰值速率](/gpu-glossary/perf/peak-rate)，也称为[算术带宽](/gpu-glossary/perf/arithmetic-bandwidth)
- "内存屋顶"——目标硬件的峰值内存吞吐量，也称为[内存带宽](/gpu-glossary/perf/memory-bandwidth)

这些内容在坐标平面中可视化显示，其中 x 轴表示[算术强度](/gpu-glossary/perf/arithmetic-intensity)（单位：操作数/字节），y 轴表示性能（单位：操作数/秒）。 "计算屋顶"是一条水平线，高度等于[算术带宽](/gpu-glossary/perf/arithmetic-bandwidth)。 "内存屋顶"是一条斜线，斜率等于[内存带宽](/gpu-glossary/perf/memory-bandwidth)。斜率是"垂直变化量除以水平变化量"，因此该线的单位是字节/秒（操作数/秒除以操作数/字节）。

特定[内核](/gpu-glossary/device-software/kernel)的 x 坐标可以立即告诉你它本质上是[受计算限制](/gpu-glossary/perf/compute-bound)（位于平顶下方）还是[受内存限制](/gpu-glossary/perf/memory-bound)（位于斜顶下方）。由于[开销](/gpu-glossary/perf/overhead)的影响，[内核](/gpu-glossary/device-software/kernel)很少能达到任一屋顶的极限。

边界上的点，即斜屋顶和平屋顶相交处，称为"脊点"。其 x 坐标是摆脱内存[性能瓶颈](/gpu-glossary/perf/performance-bottleneck)所需的最小[算术强度](/gpu-glossary/perf/arithmetic-intensity)。脊点越靠左的计算机系统越容易实现最大性能，但内存相对于计算较差的扩展性总体上已随着时间的推移将系统的脊点推向了右侧。

计算和内存屋顶只需每个子系统推导一次（但重要的是它们因子系统而异，而不仅仅是系统；[张量核心](/gpu-glossary/device-hardware/tensor-core)比[CUDA 核心](/gpu-glossary/device-hardware/cuda-core)具有更高的 FLOPS）。

NVIDIA 用于[内核](/gpu-glossary/device-software/kernel)性能工程的 NSight Compute 工具会自动对分析的[内核](/gpu-glossary/device-software/kernel)执行屋顶线分析。

屋顶线模型看似简单。请注意，例如，系统延迟并未出现在图表中的任何位置，仅包含带宽和吞吐量。它之所以简单，是因为它具有很强的倾向性，理解这些倾向性及其背后的原理是理解屋顶线模型的威力和正确应用的关键。

屋顶线模型由 Samuel Williams、Andrew Waterman 和 David Patterson 在[这篇 2008 年的论文](https://people.eecs.berkeley.edu/~kubitron/cs252/handouts/papers/RooflineVyNoYellow.pdf)中提出。他们提出该模型时，面对的是在此之前及之后塑造系统架构的若干硬件扩展趋势。

首先，正如 Patterson 在 2004 年一篇著名论文中单独观察到的，["延迟滞后于带宽"](https://dl.acm.org/doi/pdf/10.1145/1022594.1022596)。更具体地说，在计算、内存和存储等子系统中，延迟的线性改进历史上一直伴随着带宽的二次改进。这表明未来的系统将像 GPU 一样，以吞吐量为导向。

其次，正如长期以来观察到的，计算子系统（如处理器核心）的性能扩展速度远快于内存子系统，如[缓存](/gpu-glossary/device-hardware/l1-data-cache)和[DRAM](/gpu-glossary/device-hardware/gpu-ram)。这在 1994 年被 Wulf 和 McKee 普及为["内存墙"](https://www.eecs.ucf.edu/~lboloni/Teaching/EEL5708_2006/slides/wulf94.pdf)。

最后，21 世纪初，由于晶体管固定漏电流带来的功耗和散热问题，[登纳德缩放比例定律](https://en.wikipedia.org/wiki/Dennard_scaling)（即在同等功耗下提高时钟速度）走到了尽头。此前，提高时钟速度一直支撑着像 CPU 这样的通用、面向延迟的系统，使其优于专用硬件。这种放缓并未伴随着[摩尔定律](https://en.wikipedia.org/wiki/Moore%27s_law)（即每芯片晶体管数量增加）的放缓。在晶体管丰富但电力稀缺的情况下，架构上的解决方案是硬件专业化：将计算机分解为专门完成不同任务的组件。关于一个记录详尽的例子，请参见[Pixel Visual Core](https://blog.google/products/pixel/pixel-visual-core-image-processing-and-machine-learning-pixel-2/)图像协处理器，该处理器在 Hennessy 和 Patterson 的第六版[_计算机体系结构_](https://archive.org/details/computerarchitectureaquantitativeapproach6thedition/page/n13/mode/2up)第 7 章中有详细解释。

综上所述，这些趋势正确地告诉作者，未来的系统将以吞吐量为导向，并且在各种起作用的带宽中，[内存子系统的带宽](/gpu-glossary/perf/memory-bandwidth)将是主要的[性能瓶颈](/gpu-glossary/perf/performance-bottleneck)。因此，希望在这些系统上达到峰值性能的应用程序，需要对该硬件的专用操作具有高操作强度——对于 GPU 而言，即针对[张量核心](/gpu-glossary/device-hardware/tensor-core)的[算术强度](/gpu-glossary/perf/arithmetic-intensity)，也就是说需要非常大的矩阵乘法。