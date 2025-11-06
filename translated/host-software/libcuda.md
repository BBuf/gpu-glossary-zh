<!--
原文: 文件路径: gpu-glossary/host-software/libcuda.md
翻译时间: 2025-11-06 18:28:03
-->

---
title: 什么是 libcuda.so？
---

这是在 Linux 系统上实现 [CUDA 驱动程序 API](/gpu-glossary/host-software/cuda-driver-api) 的二进制共享对象文件的通用名称。CUDA 程序会动态链接该文件。如果该文件缺失，通常意味着驱动程序安装不正确。