<!--
原文: 文件路径: gpu-glossary/host-software/nvidia-ko.md
翻译时间: 2025-11-06 18:29:23
-->

---
title: 什么是 nvidia.ko？
---

`nvidia.ko` 是 [NVIDIA GPU 驱动程序](/gpu-glossary/host-software/nvidia-gpu-drivers) 在 Linux 系统中的核心二进制
[内核模块](https://wiki.archlinux.org/title/Kernel_module) 文件。

与其他内核模块类似，它以特权模式运行，并代表用户直接与硬件通信——在此场景下，硬件特指 GPU。

Linux 开放 GPU 内核模块是
[开源的](https://github.com/NVIDIA/open-gpu-kernel-modules)。