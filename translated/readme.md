<!--
原文: 文件路径: gpu-glossary/readme.md
翻译时间: 2025-11-06 18:21:53
-->

---
title: README
---

<pre class="text-xs md:text-base font-mono whitespace-pre">
 ██████╗ ██████╗ ██╗   ██╗
██╔════╝ ██╔══██╗██║   ██║
██║  ███╗██████╔╝██║   ██║
██║   ██║██╔═══╝ ██║   ██║
╚██████╔╝██║     ╚██████╔╝
 ╚═════╝ ╚═╝      ╚═════╝
 ██████╗ ██╗      ██████╗ ███████╗███████╗ █████╗ ██████╗ ██╗   ██╗
██╔════╝ ██║     ██╔═══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
██║  ███╗██║     ██║   ██║███████╗███████╗███████║██████╔╝ ╚████╔╝
██║   ██║██║     ██║   ██║╚════██║╚════██║██╔══██║██╔══██╗  ╚██╔╝
╚██████╔╝███████╗╚██████╔╝███████║███████║██║  ██║██║  ██║   ██║
 ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
 </pre>

我们编写这个术语表是为了解决在 [Modal](/） 使用 GPU 时遇到的一个问题：文档内容分散，难以将不同技术栈层次的概念联系起来，比如[流式多处理器架构 (Streaming Multiprocessor Architecture)](/gpu-glossary/device-hardware/streaming-multiprocessor-architecture)、[计算能力 (Compute Capability)](/gpu-glossary/device-software/compute-capability) 和 [nvcc 编译器标志](/gpu-glossary/host-software)。

为此，我们研读了 [NVIDIA 的技术文档](https://docs.nvidia.com/cuda/pdf/PTX_Writers_Guide_To_Interoperability.pdf)，活跃在[优质的 Discord 社区](https://discord.gg/gpumode)，甚至购买了[纸质教科书](https://www.amazon.com/Professional-CUDA-Programming-John-Cheng/dp/1118739329)，只为汇编这份涵盖整个技术栈的综合性术语表。

与 PDF、Discord 或书籍不同，本术语表是一个*超文本文档*——所有页面都相互链接，因此您可以直接跳转阅读[线程束调度器 (Warp Scheduler)](/gpu-glossary/device-hardware/warp-scheduler) 来更好地理解在 [CUDA 编程模型](/gpu-glossary/host-software/cuda-c) 文章中遇到的[线程 (thread)](/gpu-glossary/device-software/thread) 概念。

您也可以线性阅读。要在页面间导航，可使用方向键、每页底部的箭头或目录（在桌面端显示于侧边栏，在移动端显示于汉堡菜单中）。

本术语表的源代码可在 [GitHub](https://github.com/modal-labs/gpu-glossary) 上获取。