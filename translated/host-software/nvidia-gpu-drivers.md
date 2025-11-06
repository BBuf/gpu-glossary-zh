<!--
原文: 文件路径: gpu-glossary/host-software/nvidia-gpu-drivers.md
翻译时间: 2025-11-06 18:25:05
-->

---
title: 什么是 NVIDIA GPU 驱动程序？
---

NVIDIA GPU 驱动程序负责协调主机程序或主机操作系统与 GPU 设备之间的交互。应用程序访问 GPU 驱动程序的主要接口按层级依次为：
[CUDA 运行时 API](/gpu-glossary/host-software/cuda-runtime-api) 和
[CUDA 驱动程序 API](/gpu-glossary/host-software/cuda-driver-api)。

![CUDA 工具包示意图。NVIDIA GPU 驱动是唯一直接与 GPU 通信的组件。改编自《Professional CUDA C Programming Guide》。](https://modal.com/_next/image?url=%2Fgpu-glossary%2Fcuda-toolkit.svg&w=1920&q=75)

NVIDIA 已开源其 Linux 开放 GPU [内核模块](/gpu-glossary/host-software/nvidia-ko)的
[源代码](https://github.com/NVIDIA/open-gpu-kernel-modules)。